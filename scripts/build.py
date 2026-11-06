"""Validate the canonical catalog and render its GitHub reading view."""
import argparse
from datetime import date
import json
from pathlib import Path
import sys
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = {'web-search': 'Web Search', 'web-scraping': 'Web Scraping',
              'url-fetch': 'URL Fetch', 'browser-infrastructure': 'Browser Infrastructure',
              'site-search': 'Site Search', 'web-data': 'Web Data',
              'llm': 'LLM', 'multimodal': 'Multimodal', 'embeddings': 'Embeddings'}
OFFERS = {'ongoing': 'Ongoing free access', 'recurring': 'Recurring free quota',
          'trial': 'One-time trial', 'application': 'Application / promotion', 'none': 'No free offer reported'}
CONDITIONS = {'required': 'Required', 'not-required': 'Not required', 'unknown': 'Unknown'}


def validate(rows):
    assert isinstance(rows, list) and rows, 'Catalog must be a nonempty array'
    ids = set()
    fields = {'id', 'name', 'categories', 'offer', 'allowance', 'registration',
              'credit_card', 'eligibility', 'overage', 'notes', 'sources', 'status', 'checked_on'}
    for r in rows:
        assert set(r) == fields, f'Unexpected fields: {r.get("id")}'
        assert r['id'] not in ids, f'Duplicate ID: {r["id"]}'
        ids.add(r['id'])
        assert r['categories'] and len(set(r['categories'])) == len(r['categories'])
        assert set(r['categories']) <= CATEGORIES.keys()
        assert r['offer'] in OFFERS and r['status'] in {'verified', 'pending', 'not-free', 'retired'}
        assert r['registration'] in CONDITIONS and r['credit_card'] in CONDITIONS
        for key in fields - {'categories', 'sources', 'checked_on'}:
            assert isinstance(r[key], str) and r[key].strip(), f'Empty {key}'
        assert r['sources'] and all(urlparse(s).scheme == 'https' and urlparse(s).netloc for s in r['sources'])
        if r['checked_on'] is not None:
            assert date.fromisoformat(r['checked_on']) <= date.today(), 'Future review date'
        if r['status'] == 'verified':
            assert r['checked_on'] and r['offer'] != 'none', 'Verified offer needs a date and free access'
        if r['status'] in {'not-free', 'retired'}:
            assert r['checked_on'] and r['offer'] == 'none', 'Excluded offers need a review date and no free offer'


def cell(s):
    return str(s).replace('|', '&#124;').replace('\n', ' ')


def fresh(r):
    return r['status'] == 'verified' and (date.today() - date.fromisoformat(r['checked_on'])).days <= 90


def read_audit(rows):
    """Coverage contains references, never a second copy of offer terms."""
    path = ROOT / 'data/search-audit.json'
    if not path.exists():
        return None
    audit = json.loads(path.read_text(encoding='utf-8'))
    assert audit['fact_source'] == 'resources.json'
    assert date.fromisoformat(audit['audited_on']) <= date.today()
    ids = {r['id'] for r in rows}
    seen = set()
    for item in audit['items']:
        assert item['registry_id'] not in seen, 'Duplicate audit candidate'
        seen.add(item['registry_id'])
        assert set(item['catalogs']) <= {'registry', 'awesome-ai-tools'}
        if item['offer_ids']:
            assert set(item) == {'registry_id', 'name', 'catalogs', 'offer_ids'}, 'Linked coverage must not duplicate offer facts'
            assert set(item['offer_ids']) <= ids, 'Dangling canonical offer reference'
        else:
            assert item['finding'] and item['note'] and item['sources']
            assert all(urlparse(s).scheme == 'https' and urlparse(s).netloc for s in item['sources'])
    return audit


def render(rows):
    audit = read_audit(rows)
    active = [r for r in rows if fresh(r)]
    pending = [r for r in rows if r['status'] in {'verified', 'pending'} and not fresh(r)]
    paid = [r for r in rows if r['status'] == 'not-free']
    retired = [r for r in rows if r['status'] == 'retired']
    out = ['---', 'title: PerkScout',
           'description: Discover free APIs, recurring quotas and developer perks by API type and access conditions.',
           'type: index', 'date: 2026-11-06', '---', '', '# PerkScout', '',
           '**Find free resources. Build for less.**', '',
           'An English-language catalog of free APIs and developer offers from around the world, including China. Browse by API type, then by offer and signup conditions.', '',
           '> Generated from [data/resources.json](data/resources.json), the single source of truth for resource facts. Edit the data, then run `python scripts/build.py`.', '',
           '## Browse', '']
    for slug, title in CATEGORIES.items():
        out.append(f'- [{title}](#{slug})')
    out += ['- [Browse by conditions](#browse-by-conditions)', '- [Pending review](#pending-review)',
            '- [No confirmed free offer](#no-confirmed-free-offer)', '- [Retired offers](#retired-offers)',
            '- [Search and fetch audit coverage](#search-and-fetch-audit-coverage)', '',
            '## How to read this list', '',
            'Free access and signup conditions are independent. Ongoing free access can still require registration, have rate limits, or restrict eligible regions. Unknown means not confirmed, not unrestricted.', '',
            'Verified means the core offer was reviewed in official material on the listed date; it does not mean we tested signup or API calls. Entries older than 90 days move to pending review when regenerated. Credits from different providers are not directly comparable. Read the details before enabling billing or paid fallbacks.', '',
            f'{len(active)} reviewed offers; {len(pending)} pending; {len(paid)} with no confirmed free offer; {len(retired)} retired. A provider may offer more than one distinct free route.', '']
    for slug, title in CATEGORIES.items():
        out += [f'## {title}', '', '| Offer | Free allowance | Offer type | Registration | Credit card | Reviewed |',
                '|---|---|---|---|---|---|']
        for r in sorted((r for r in active if slug in r['categories']), key=lambda r: (r['offer'], r['name'])):
            out.append('| ' + ' | '.join(map(cell, [f'[{r["name"]}](#{r["id"]})', r['allowance'], OFFERS[r['offer']], CONDITIONS[r['registration']], CONDITIONS[r['credit_card']], r['checked_on']])) + ' |')
        if not any(slug in r['categories'] for r in active):
            out += ['', 'No reviewed offers yet. Contributions welcome.']
        out += ['']
    out += ['## Browse by conditions', '', 'These views link to the same canonical offers; they do not maintain separate quotas.', '']
    filters = [('No registration', lambda r: r['registration'] == 'not-required'),
               ('No credit card', lambda r: r['credit_card'] == 'not-required')]
    filters += [(label, lambda r, value=value: r['offer'] == value) for value, label in OFFERS.items() if value != 'none']
    for label, predicate in filters:
        links = ', '.join(f'[{r["name"]}](#{r["id"]})' for r in active if predicate(r))
        out += [f'- **{label}:** {links or "No reviewed entries yet."}']
    out += ['', '## Offer details', '']

    def detail(r, pending=False):
        result = [f'<a id="{r["id"]}"></a>', '', f'### {r["name"]}', '']
        if pending:
            label = {'not-free': 'No confirmed free offer — excluded from the free catalog.',
                     'retired': 'Retired — unavailable as a current API offer.'}.get(r['status'],
                     'Pending review — not a confirmed current free offer.')
            result += [f'**{label}**', '',
                       f'- Reported allowance: {r["allowance"]}',
                       f'- Reported offer type: {OFFERS[r["offer"]]}',
                       f'- Registration: {CONDITIONS[r["registration"]]}; credit card: {CONDITIONS[r["credit_card"]]}.',
                       f'- Last verified: {r["checked_on"] or "Not verified"}.']
        result += [f'- Eligibility: {r["eligibility"]}', f'- Overage: {r["overage"]}',
                   f'- Notes: {r["notes"]}',
                   '- Official sources: ' + ', '.join(f'[Source {i}]({s})' for i, s in enumerate(r['sources'], 1)), '']
        return result

    for r in active:
        out += detail(r)
    out += ['## Pending review', '',
            'Earlier research claims are preserved here for follow-up, not presented as current recommendations. Some offers may have changed or ended. Provider names and URLs also require confirmation where noted.', '']
    for r in pending:
        out += detail(r, True)
    out += ['## No confirmed free offer', '',
            'Reviewed services without an established standing free offer. Account-specific promotions may differ. These are excluded from the free catalog.', '']
    for r in paid:
        out += detail(r, True)
    out += ['## Retired offers', '']
    for r in retired:
        out += detail(r, True)
    out += ['## Search and fetch audit coverage', '']
    if audit:
        out += [f'Catalog audit dated {audit["audited_on"]}: {len(audit["items"])} candidates from registry and awesome-ai-tools. Quotas are maintained only in the linked canonical offers; this coverage index records decisions for every candidate.', '',
                'Scope: public-web search, URL retrieval, scraping, browser infrastructure and adjacent site/enterprise retrieval. Consumer search apps are checked separately; a free website or local tool does not establish a hosted API grant.', '',
                '| Candidate | Canonical offer or review finding |', '|---|---|']
        by_id = {r['id']: r for r in rows}
        for item in audit['items']:
            if item['offer_ids']:
                finding = ', '.join(f'[{by_id[id]["name"]}](#{id})' for id in item['offer_ids'])
            else:
                finding = f'{item["finding"]}: {item["note"]} [Official source]({item["sources"][0]})'
            out.append(f'| {cell(item["name"])} | {cell(finding)} |')
        out += ['', 'Machine-readable coverage: [data/search-audit.json](data/search-audit.json). Audit findings are based on public documentation; no account creation or authenticated calls were performed.', '']
    else:
        out += ['No coverage audit has been recorded yet.', '']
    out += ['## Contribute', '',
            'See [CONTRIBUTING.md](CONTRIBUTING.md) for the data format, evidence requirements and review policy. No affiliate links. Never submit API keys or personal account details.', '',
            '## License', '', '[MIT](LICENSE). Provider services remain subject to their own terms.', '']
    return '\n'.join(out)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    rows = json.loads((ROOT / 'data/resources.json').read_text(encoding='utf-8'))
    validate(rows)
    expected = render(rows)
    target = ROOT / 'README.md'
    if args.check:
        if not target.exists() or target.read_text(encoding='utf-8') != expected:
            sys.exit('README is stale. Run python scripts/build.py and commit the result.')
        print(f'Validated {len(rows)} offers and generated README consistency.')
    else:
        target.write_text(expected, encoding='utf-8', newline='\n')
        print(f'Generated README from {len(rows)} canonical records.')


if __name__ == '__main__':
    main()
