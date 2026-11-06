---
title: PerkScout
description: Discover free APIs, recurring quotas and developer perks by API type and access conditions.
type: index
date: 2026-11-06
---

# PerkScout

**Find free resources. Build for less.**

An English-language catalog of free APIs and developer offers from around the world, including China. Browse by API type, then by offer and signup conditions.

> Generated from [data/resources.json](data/resources.json), the single source of truth for resource facts. Edit the data, then run `python scripts/build.py`.

## Browse

- [Web Search](#web-search)
- [Web Scraping](#web-scraping)
- [LLM](#llm)
- [Multimodal](#multimodal)
- [Embeddings](#embeddings)
- [Browse by conditions](#browse-by-conditions)
- [Pending review](#pending-review)

## How to read this list

Free access and signup conditions are independent. Ongoing free access can still require registration, have rate limits, or restrict eligible regions. Unknown means not confirmed, not unrestricted.

Verified means the core offer was reviewed in official material on the listed date; it does not mean we tested signup or API calls. Entries older than 90 days move to pending review when regenerated. Credits from different providers are not directly comparable. Read the details before enabling billing or paid fallbacks.

8 reviewed offers; 18 pending; 0 retired. A provider may offer more than one distinct free route.

## Web Search

| Offer | Free allowance | Offer type | Registration | Credit card | Reviewed |
|---|---|---|---|---|---|
| [Exa](#exa) | $10/month plus a one-time $10 onboarding bonus. | Recurring free quota | Required | Not required | 2026-11-06 |
| [Firecrawl](#firecrawl) | 1,000 credits/month: up to 500 searches or 1,000 scraped pages. | Recurring free quota | Required | Not required | 2026-11-06 |
| [Tavily](#tavily) | $0 plan: 1,000 credits/month; resets on the first day of the month. | Recurring free quota | Required | Not required | 2026-11-06 |
| [Jina Search Foundation (free key)](#jina-key) | New keys include 10M free tokens shared across products; expiry not confirmed. | One-time trial | Unknown | Unknown | 2026-11-06 |

## Web Scraping

| Offer | Free allowance | Offer type | Registration | Credit card | Reviewed |
|---|---|---|---|---|---|
| [Jina Reader (no key)](#jina-reader) | 20 requests/minute without an API key. | Ongoing free access | Not required | Not required | 2026-11-06 |
| [Exa](#exa) | $10/month plus a one-time $10 onboarding bonus. | Recurring free quota | Required | Not required | 2026-11-06 |
| [Firecrawl](#firecrawl) | 1,000 credits/month: up to 500 searches or 1,000 scraped pages. | Recurring free quota | Required | Not required | 2026-11-06 |
| [Tavily](#tavily) | $0 plan: 1,000 credits/month; resets on the first day of the month. | Recurring free quota | Required | Not required | 2026-11-06 |
| [Jina Search Foundation (free key)](#jina-key) | New keys include 10M free tokens shared across products; expiry not confirmed. | One-time trial | Unknown | Unknown | 2026-11-06 |

## LLM

| Offer | Free allowance | Offer type | Registration | Credit card | Reviewed |
|---|---|---|---|---|---|
| [Google Gemini API](#gemini) | Free input/output for selected models, subject to model-specific quotas. | Ongoing free access | Required | Not required | 2026-11-06 |
| [OpenRouter free models](#openrouter) | Selected models with a listed :free variant; limits and availability vary. | Ongoing free access | Required | Unknown | 2026-11-06 |
| [Zhipu GLM-4.7-Flash](#glm-flash) | Official announcement offers free API calls; account limits apply. | Ongoing free access | Required | Unknown | 2026-11-06 |

## Multimodal

| Offer | Free allowance | Offer type | Registration | Credit card | Reviewed |
|---|---|---|---|---|---|
| [Google Gemini API](#gemini) | Free input/output for selected models, subject to model-specific quotas. | Ongoing free access | Required | Not required | 2026-11-06 |

## Embeddings

| Offer | Free allowance | Offer type | Registration | Credit card | Reviewed |
|---|---|---|---|---|---|
| [Jina Search Foundation (free key)](#jina-key) | New keys include 10M free tokens shared across products; expiry not confirmed. | One-time trial | Unknown | Unknown | 2026-11-06 |

## Browse by conditions

These views link to the same canonical offers; they do not maintain separate quotas.

- **No registration:** [Jina Reader (no key)](#jina-reader)
- **No credit card:** [Tavily](#tavily), [Exa](#exa), [Firecrawl](#firecrawl), [Jina Reader (no key)](#jina-reader), [Google Gemini API](#gemini)
- **Ongoing free access:** [Jina Reader (no key)](#jina-reader), [Google Gemini API](#gemini), [OpenRouter free models](#openrouter), [Zhipu GLM-4.7-Flash](#glm-flash)
- **Recurring free quota:** [Tavily](#tavily), [Exa](#exa), [Firecrawl](#firecrawl)
- **One-time trial:** [Jina Search Foundation (free key)](#jina-key)
- **Application / promotion:** No reviewed entries yet.

## Offer details

<a id="tavily"></a>

### Tavily

- Eligibility: Not confirmed; consult provider signup and regional terms.
- Overage: Free-plan requests stop until reset or upgrade.
- Notes: Search, extract and crawl share credits; request costs vary by operation.
- Official sources: [Source 1](https://www.tavily.com/pricing)

<a id="exa"></a>

### Exa

- Eligibility: Not confirmed; consult provider signup and regional terms.
- Overage: Not confirmed; check billing settings before enabling paid usage.
- Notes: Search and content retrieval; do not convert dollar credits to a universal request count.
- Official sources: [Source 1](https://exa.ai/pricing)

<a id="firecrawl"></a>

### Firecrawl

- Eligibility: Not confirmed; consult provider signup and regional terms.
- Overage: Not confirmed; check billing settings before enabling paid usage.
- Notes: Free plan lists two concurrent requests; operations share the same balance.
- Official sources: [Source 1](https://www.firecrawl.dev/pricing)

<a id="jina-reader"></a>

### Jina Reader (no key)

- Eligibility: Not confirmed; consult provider signup and regional terms.
- Overage: Rate limits apply; anonymous access has no payment method attached.
- Notes: Hosted URL-to-text API. Rate-limited, not unlimited. Key-based products have separate balances.
- Official sources: [Source 1](https://jina.ai/reader/)

<a id="jina-key"></a>

### Jina Search Foundation (free key)

- Eligibility: Not confirmed; consult provider signup and regional terms.
- Overage: Not confirmed; check billing settings before enabling paid usage.
- Notes: Reader: 500 RPM; search: 100 RPM; embeddings: 100 RPM and 100K TPM. These are rate ceilings, not recurring token grants. Includes reranking; image embeddings depend on the chosen model.
- Official sources: [Source 1](https://jina.ai/reader/)

<a id="gemini"></a>

### Google Gemini API

- Eligibility: Not confirmed; consult provider signup and regional terms.
- Overage: Free-tier quotas apply; enabling billing changes applicable rates.
- Notes: Google account/project required. Supported regions, age restrictions and model availability apply. Free-tier content may be used to improve products. Multimodal input support does not mean every image/audio/video generation API is free.
- Official sources: [Source 1](https://ai.google.dev/gemini-api/docs/pricing), [Source 2](https://ai.google.dev/gemini-api/docs/billing)

<a id="openrouter"></a>

### OpenRouter free models

- Eligibility: Not confirmed; consult provider signup and regional terms.
- Overage: Not confirmed; check billing settings before enabling paid usage.
- Notes: Only models with a free catalog entry qualify. Paid fallbacks can incur charges; use only free fallbacks or openrouter/free.
- Official sources: [Source 1](https://openrouter.ai/docs/guides/routing/model-variants/free)

<a id="glm-flash"></a>

### Zhipu GLM-4.7-Flash

- Eligibility: Not confirmed; consult provider signup and regional terms.
- Overage: Not confirmed; check billing settings before enabling paid usage.
- Notes: China-based BigModel platform. Text input/output; phone and identity requirements need confirmation. GLM-4.5-Flash has been superseded.
- Official sources: [Source 1](https://www.zhipuai.cn/zh/news/148), [Source 2](https://docs.bigmodel.cn/cn/guide/models/free/glm-4.7-flash)

## Pending review

Earlier research claims are preserved here for follow-up, not presented as current recommendations. Some offers may have changed or ended. Provider names and URLs also require confirmation where noted.

<a id="bocha"></a>

### Bocha (博查)

**Pending review — not a confirmed current free offer.**

- Reported allowance: Promotional free credits may be offered; no fixed public grant confirmed.
- Reported offer type: Application / promotion
- Registration: Required; credit card: Unknown.
- Last verified: Not verified.
- Eligibility: Not confirmed; consult provider signup and regional terms.
- Overage: Not confirmed; check billing settings before enabling paid usage.
- Notes: Official terms allow promotional credits and contacting support to request more. Pricing documentation could not be read during this review; confirm eligibility, amount, expiry and phone requirements.
- Official sources: [Source 1](https://open.bochaai.com/), [Source 2](https://open.bochaai.com/terms-of-service)

<a id="searchx"></a>

### SearchX

**Pending review — not a confirmed current free offer.**

- Reported allowance: 3,000 queries/day (about 90K/month).
- Reported offer type: Recurring free quota
- Registration: Required; credit card: Not required.
- Last verified: Not verified.
- Eligibility: Not confirmed; consult provider signup and regional terms.
- Overage: Not confirmed; check billing settings before enabling paid usage.
- Notes: UNVERIFIED MIGRATION: Provider-reported; do not assume production reliability.
- Official sources: [Source 1](https://searchx.dev)

<a id="unsearch"></a>

### UnSearch

**Pending review — not a confirmed current free offer.**

- Reported allowance: 5,000 queries/month.
- Reported offer type: Recurring free quota
- Registration: Required; credit card: Not required.
- Last verified: Not verified.
- Eligibility: Not confirmed; consult provider signup and regional terms.
- Overage: Not confirmed; check billing settings before enabling paid usage.
- Notes: UNVERIFIED MIGRATION: Earlier notes describe Apache-2.0 licensing, Tavily/Exa compatibility and self-hosting. Verify repository/license; self-hosting still costs infrastructure and is not unlimited hosted access.
- Official sources: [Source 1](https://unsearch.dev)

<a id="nimble"></a>

### Nimble

**Pending review — not a confirmed current free offer.**

- Reported allowance: 5,000 requests/month.
- Reported offer type: Recurring free quota
- Registration: Required; credit card: Not required.
- Last verified: Not verified.
- Eligibility: Not confirmed; consult provider signup and regional terms.
- Overage: Not confirmed; check billing settings before enabling paid usage.
- Notes: UNVERIFIED MIGRATION: Search, extraction and structured output; confirm SDK and Web Search Agents availability.
- Official sources: [Source 1](https://www.nimbleway.com/pricing)

<a id="you"></a>

### You.com

**Pending review — not a confirmed current free offer.**

- Reported allowance: Earlier pricing: MCP 100 queries/day; FAQ: $100 signup credits, conflicting with an older $10 figure.
- Reported offer type: Recurring free quota
- Registration: Required; credit card: Not required.
- Last verified: Not verified.
- Eligibility: Not confirmed; consult provider signup and regional terms.
- Overage: Not confirmed; check billing settings before enabling paid usage.
- Notes: UNVERIFIED MIGRATION: MCP and HTTP API conditions differ. Earlier Web Search price: $5/1K. Prior notes mention keyless MCP and SOC 2; confirm current terms.
- Official sources: [Source 1](https://you.com/pricing)

<a id="parallel"></a>

### Parallel AI

**Pending review — not a confirmed current free offer.**

- Reported allowance: $5/month (earlier estimate: about 5,000 Search calls).
- Reported offer type: Recurring free quota
- Registration: Required; credit card: Required.
- Last verified: Not verified.
- Eligibility: Not confirmed; consult provider signup and regional terms.
- Overage: Not confirmed; check billing settings before enabling paid usage.
- Notes: UNVERIFIED MIGRATION: Prior notes require a credit card and describe keyless MCP and evidence provenance. Do not infer API registration conditions from MCP access.
- Official sources: [Source 1](https://parallel.ai)

<a id="linkup"></a>

### Linkup

**Pending review — not a confirmed current free offer.**

- Reported allowance: 4,000 credits/month.
- Reported offer type: Recurring free quota
- Registration: Required; credit card: Unknown.
- Last verified: Not verified.
- Eligibility: Not confirmed; consult provider signup and regional terms.
- Overage: Not confirmed; check billing settings before enabling paid usage.
- Notes: UNVERIFIED MIGRATION: Standard and deep search have different costs.
- Official sources: [Source 1](https://www.linkup.so)

<a id="brightdata"></a>

### Bright Data

**Pending review — not a confirmed current free offer.**

- Reported allowance: 5,000 credits/month.
- Reported offer type: Recurring free quota
- Registration: Required; credit card: Unknown.
- Last verified: Not verified.
- Eligibility: Not confirmed; consult provider signup and regional terms.
- Overage: Not confirmed; check billing settings before enabling paid usage.
- Notes: UNVERIFIED MIGRATION: Proxy-backed search/scraping; verify product-specific offer.
- Official sources: [Source 1](https://brightdata.com)

<a id="searlo"></a>

### Searlo

**Pending review — not a confirmed current free offer.**

- Reported allowance: 3,000 signup credits, valid for one year.
- Reported offer type: One-time trial
- Registration: Required; credit card: Not required.
- Last verified: Not verified.
- Eligibility: Not confirmed; consult provider signup and regional terms.
- Overage: Not confirmed; check billing settings before enabling paid usage.
- Notes: UNVERIFIED MIGRATION: Earlier paid bundle claim: as low as $0.20/1K; not verified. Search/SERP service.
- Official sources: [Source 1](https://searlo.tech/pricing)

<a id="brave"></a>

### Brave Search API

**Pending review — not a confirmed current free offer.**

- Reported allowance: $5/month (earlier estimate: about 1,000 requests).
- Reported offer type: Recurring free quota
- Registration: Required; credit card: Required.
- Last verified: Not verified.
- Eligibility: Not confirmed; consult provider signup and regional terms.
- Overage: Not confirmed; check billing settings before enabling paid usage.
- Notes: UNVERIFIED MIGRATION: Earlier notes conflict on whether the free tier was restricted in late 2025. Independent index; index-size claims are not verified.
- Official sources: [Source 1](https://brave.com/search/api/)

<a id="youtube"></a>

### YouTube Data API v3

**Pending review — not a confirmed current free offer.**

- Reported allowance: Earlier notes: 100 search.list calls/day plus 10,000 units/day for other operations.
- Reported offer type: Recurring free quota
- Registration: Required; credit card: Unknown.
- Last verified: Not verified.
- Eligibility: Not confirmed; consult provider signup and regional terms.
- Overage: Not confirmed; check billing settings before enabling paid usage.
- Notes: UNVERIFIED MIGRATION: Requires a Google Cloud project and API credentials; that alone does not imply a card requirement. Confirm quota accounting and Pacific-time reset. For known channels consider playlistItems; quota extension policy needs review.
- Official sources: [Source 1](https://developers.google.com/youtube/v3/getting-started)

<a id="serpapi"></a>

### SerpApi

**Pending review — not a confirmed current free offer.**

- Reported allowance: 250 queries/month; no rollover.
- Reported offer type: Recurring free quota
- Registration: Required; credit card: Not required.
- Last verified: Not verified.
- Eligibility: Not confirmed; consult provider signup and regional terms.
- Overage: Not confirmed; check billing settings before enabling paid usage.
- Notes: UNVERIFIED MIGRATION: Hosted SERP retrieval; original notes focused on Google results.
- Official sources: [Source 1](https://serpapi.com/pricing)

<a id="serper"></a>

### Serper

**Pending review — not a confirmed current free offer.**

- Reported allowance: 2,500 one-time queries.
- Reported offer type: One-time trial
- Registration: Required; credit card: Not required.
- Last verified: Not verified.
- Eligibility: Not confirmed; consult provider signup and regional terms.
- Overage: Not confirmed; check billing settings before enabling paid usage.
- Notes: UNVERIFIED MIGRATION: Google SERP API; not a monthly allowance. Earlier speed/price superlatives were unsupported.
- Official sources: [Source 1](https://serper.dev)

<a id="llmlayer"></a>

### LLMLayer

**Pending review — not a confirmed current free offer.**

- Reported allowance: $1 in free credits.
- Reported offer type: One-time trial
- Registration: Required; credit card: Unknown.
- Last verified: Not verified.
- Eligibility: Not confirmed; consult provider signup and regional terms.
- Overage: Not confirmed; check billing settings before enabling paid usage.
- Notes: UNVERIFIED MIGRATION: Search, scraping and answer generation bundle; verify domain, terms and expiry.
- Official sources: [Source 1](https://llmlayer.com)

<a id="google-cse"></a>

### Google Custom Search JSON API

**Pending review — not a confirmed current free offer.**

- Reported allowance: Earlier notes: 100 queries/day.
- Reported offer type: Recurring free quota
- Registration: Required; credit card: Unknown.
- Last verified: Not verified.
- Eligibility: Not confirmed; consult provider signup and regional terms.
- Overage: Not confirmed; check billing settings before enabling paid usage.
- Notes: UNVERIFIED MIGRATION: Earlier notes state closed to new customers and ending 2027-01-01. Confirm current eligibility and shutdown date before use.
- Official sources: [Source 1](https://developers.google.com/custom-search/v1/overview)

<a id="perplexity"></a>

### Perplexity API

**Pending review — not a confirmed current free offer.**

- Reported allowance: Earlier notes: no standard free API; prepaid pay-as-you-go.
- Reported offer type: No free offer reported
- Registration: Required; credit card: Unknown.
- Last verified: Not verified.
- Eligibility: Not confirmed; consult provider signup and regional terms.
- Overage: Not confirmed; check billing settings before enabling paid usage.
- Notes: UNVERIFIED MIGRATION: Earlier notes date removal of Pro monthly $5 API credits to 2026-02-12; confirm. Answer synthesis is distinct from a free search API.
- Official sources: [Source 1](https://docs.perplexity.ai)

<a id="fal"></a>

### fal.ai

**Pending review — not a confirmed current free offer.**

- Reported allowance: Earlier notes: no standard free tier; startup program $1K-$5K by application.
- Reported offer type: Application / promotion
- Registration: Required; credit card: Unknown.
- Last verified: Not verified.
- Eligibility: Not confirmed; consult provider signup and regional terms.
- Overage: Not confirmed; check billing settings before enabling paid usage.
- Notes: UNVERIFIED MIGRATION: Earlier Builder Grant $25-$250 was no longer shown. Program availability and eligibility need confirmation.
- Official sources: [Source 1](https://fal.ai)

<a id="unifuncs"></a>

### UniFuncs

**Pending review — not a confirmed current free offer.**

- Reported allowance: Earlier notes: Web Search/Reader APIs are paid.
- Reported offer type: No free offer reported
- Registration: Required; credit card: Unknown.
- Last verified: Not verified.
- Eligibility: Not confirmed; consult provider signup and regional terms.
- Overage: Not confirmed; check billing settings before enabling paid usage.
- Notes: UNVERIFIED MIGRATION: A free Deep Research web UI does not imply a free API.
- Official sources: [Source 1](https://unifuncs.com)

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md) for the data format, evidence requirements and review policy. No affiliate links. Never submit API keys or personal account details.

## License

[MIT](LICENSE). Provider services remain subject to their own terms.
