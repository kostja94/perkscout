---
title: Contributing to PerkScout
description: How to add, verify and maintain resource records without duplicating facts.
type: spec
date: 2026-11-06
---

# Contributing to PerkScout

Edit `data/resources.json`, the sole editable source of resource facts. Never edit generated README tables. Run `python scripts/build.py` and commit both data and generated README. Run `python scripts/build.py --check` before opening a pull request. Python 3.11+ and the standard library are sufficient.

Each record describes one offer; a provider may have multiple distinct offers. Use a stable unique ID. Assign any applicable categories: `web-search`, `web-scraping`, `llm`, `multimodal`, `embeddings`. Add new categories in the generator only when there are real entries.

Offer values: `ongoing` (a standing free service, still subject to limits), `recurring` (a resetting allowance), `trial` (one-time credits), `application` (requires approval or a promotion), `none` (no free offer reported). Never label a service unlimited without explicit evidence. Self-hosting and open source do not imply free infrastructure.

Registration and credit-card fields independently use `required`, `not-required`, or `unknown`. Explain phone, identity, student, organization and regional requirements in eligibility. Do not infer card requirements from API-key or Cloud-project requirements. Record quotas, reset/expiry, shared balances and overage behavior separately.

Use official pricing, documentation or announcements in sources. Preserve conflicting claims as pending until resolved. `verified` means the core offer was reviewed in official material on checked_on, not that signup or an API call was tested; unknown conditions remain explicit. Pending records have checked_on null. Record the actual review date, never a future date or the date of a formatting change. Flag verified entries older than 90 days for review; the generator moves them out of the main list automatically.

Keep old offers as pending or retired when policy changes rather than losing context. Do not add affiliate links, secret keys, personal account states or local filesystem paths. The project covers global providers including China; write descriptions in English and preserve the official Chinese name when useful.
