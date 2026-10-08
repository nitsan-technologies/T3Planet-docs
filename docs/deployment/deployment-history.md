# T3Planet documentation deployment history

Append one entry per production release.

---


## 2026-09-28 — TonicTypes 2.2.x + AI Foundation dependency

- **Status:** PASS
- **Commit:** `7680755` — docs: update TonicTypes guides for 2.2.x and AI Foundation dependency
- **Author:** Nitsan <sanjay@nitsantech.com>
- **Remote:** origin → nitsan-technologies/T3Planet-docs (`master`)
- **Included:** `TonicTypes/**` (33 files: content, new Pro images dashboard_import / field_repeater / link_handler, refreshed screenshots, quickstart gif)
- **Excluded:** docs-master/ (gitignored, 0 paths in commit), workshops/, scripts/remigration/**, unreferenced `datatype_description.png`
- **Validate:** mintlify validate PASS (Node 20); no broken images/internal links in TonicTypes
- **Live QA:** 16/16 TonicTypes nav pages 200 with correct titles on docs.t3planet.de; 2.2.x / ns-t3af / User TSconfig markers on live + origin; new Pro images and quickstart gif 200 via mintcdn; `/ExtTypoTonic/Index` 308 → `/TonicTypes/Index`
- **Mintlify Activity dashboard:** NOT VERIFIED via MCP; inferred from live/origin content match after push

## 2026-09-25 — T3AC Feature Guide remigration

- **Status:** PASS
- **Commit:** `4a6af21` — docs: remigrate T3AC Feature Guide hub and restore Chatbot Save step
- **Author:** Nitsan <sanjay@nitsantech.com>
- **Remote:** origin → nitsan-technologies/T3Planet-docs (`master`)
- **Included:** ExtNsT3AC FeatureGuide Index + Chatbot, Installation include-static image, t3-stats JSON/JS
- **Excluded:** docs-master/, workshops/, scripts/remigration/**
- **Validate:** mintlify validate PASS (Node 20)
- **Live QA:** Feature Guide card hub markers present; legacy Train GPT/Sitemap/Chunk gone; Chatbot Save Configuration sentence present on live + origin
- **Mintlify Activity dashboard:** NOT VERIFIED via MCP; inferred from live/origin content match after push

## Template

```text
### YYYY-MM-DD — <short title>
- Commit:
- Push remote:
- Mintlify connected repo (verified):
- Live URL check:
- QA summary:
- Final status:
```

---

<!-- entries below -->

### 2026-09-24 — Media / TonicTypes / footer / deploy SOP
- Commit tip: `36cf8f0` (content `105c568`, SOP `0f3974d`, gitignore `018a601`/`58ec5b0`)
- Push remote: `origin` → `nitsan-technologies/T3Planet-docs` (`master`)
- Mintlify connected repo: Activity still showed `markus-neumannn/t3planet-docs` — emergency same-SHA sync to fork so live updated
- Live URL check: markers OK (`tonictypes_em_search_free`, footer CSS rule)
- QA: sitemap 841 routes (834×200, 7×308 redirects, 0 blank); Playwright search/responsive/theme + changed-page regression
- Final status: PASS WITH NON-BLOCKING WARNINGS (reconnect Mintlify Git to org repo)

### 2026-09-25 — Deployment SOP: Nitsan identity + org-only Mintlify source
- Docs updated: `docs/deployment/deploy.md`, deploy skill/checklist, deployment rules, README deploy section, AGENTS stubs, context runbooks
- Policy: production commits as **Nitsan** `<sanjay@nitsantech.com>`; push only `origin` → `nitsan-technologies/T3Planet-docs` / `master`
- Mintlify production Git source must remain the org repo (not a personal fork)
- Final status: documentation update (this entry)

### 2026-09-25 — Incident lesson: do not delete custom hostname to flush cache
- Cause: Cloudflare custom hostname for `docs.t3planet.de` was deleted/recreated to clear a stuck `/context.md` edge response; SSL cert invalidated; ACME DNS lagged → live HTTPS down (`ERR_SSL_VERSION_OR_CIPHER_MISMATCH`)
- Recovery: correct `_acme-challenge.docs` / ownership TXT on Kasserver + retrigger validation; https://docs.t3planet.de/en/latest restored
- Policy added: `.cursor/rules/custom-domain-ssl-safety.mdc` + updates to deploy SOP / deployment-safety / mintlify-deployment / t3planet-client / deploy skill checklist
- Rule: never use hostname delete/recreate as a cache fix; prefer origin check, wait for deploy, hard refresh, content Git fix
- Final status: LIVE RESTORED + SOP hardened

### 2026-09-25 — Deployment permission gate (local-only default)
- Policy: no `git push` / Mintlify production deploy unless operator says exactly `start the deployment process`
- Added `.cursor/rules/deployment-permission-gate.mdc`; updated deploy SOP, skill (exact-phrase trigger only), checklist, AGENTS, README, safety rules
- Final status: documentation update (local until authorized deploy)

### 2026-09-25 — TonicTypes docs refresh + Import/Export page
- Scope: `TonicTypes/**` content/images + new `TonicTypes/ExportImport/Index` + `docs.json` nav entry
- Also ships local-ready deployment permission gate SOP (if included in same commit)
- Push remote: `origin` → `nitsan-technologies/T3Planet-docs` (`master`)
- Final status: pending live QA after push

### 2026-09-29 — Single-link hub cards, feedback widget hidden, navigation + QA fixes
- Authorization: operator said `start the deployment process`
- Commit: `ccf9a51` by Nitsan `<sanjay@nitsantech.com>` (33 files; `7921c8d..ccf9a51`)
- Scope: `noAnchor` on 18 hub card titles; `custom.css` hides "Was this page helpful?"; MCP testing guide code blocks restored; TonicTypes / T3AA / T3AI / T3AF / HelpDesk / Personio / Event / FriendlyCaptcha / Karma / Shop content fixes; `t3-docs.js` navigation fixes; CSS minifier fix
- Excluded: `docs-master/`, `workshops/`, `backup/`, `scripts/remigration/**`, QA report JSON, unreferenced `datatype_description.png`
- Push remote: `origin` → `nitsan-technologies/T3Planet-docs` (`master`), no force
- Mintlify: GitHub check "Mintlify Deployment" completed/success on `ccf9a51` (org repo); live and `t3planet.mintlify.app` show the new markup
- QA: full crawl 833 pages 200 + valid content, 0 soft 404, 7×308 known T3AA redirects, 10×404 are local-only `backup/` / `.cursor/` files (expected); React #418 gone on hubs; card HTML 7/7 + 11/11; 90/90 live card clicks; 104/104 changed-page checks (desktop/mobile × light/dark); search OK; HTTPS valid
- Known open item: external link rot (old demo/shop/Site Kit URLs) not in this release
- Final status: PASS WITH NON-BLOCKING WARNINGS

### 2026-09-30 — Google Docs v14 remigration, T3AA Credits/quota/version fixes, perf assets
- Authorization: operator said `start the deployment process`
- Commits: `b717dce` (136 files) + merge `1d4f808` of 7 upstream Mintlify-editor commits (FAQ pages, Site Kit shop name); all by Nitsan `<sanjay@nitsantech.com>`; pushed `d48604b..1d4f808`
- Scope: Google Docs — 4 new pages (GoodToKnow, Reformation, Screenshots, Troubleshooting), new screenshots, root-relative links, unreleased embed element + v15 note removed, composer `only` without ns-license; T3AA — AI Credits setup, scan quota vs AI credits, credit usage per action, generator under Credits, one version matrix, current demo showcase (ClickUp 86d4c7nmr + earlier tickets); hub/footer product entry links; 372 legacy redirects; minified `t3-docs.js` / `custom.css`
- Merge conflicts: `ExtNsT3AA/ExtNsT3AC/ExtNsT3AS/Index.md` — kept upstream layout + FAQ card, re-applied T3AF → `ExtNsT3AF/Introduction/Index`; `docs.json` auto-merged (both nav sets present)
- Excluded: `docs-master/`, `workshops/`, `backup/`, `scripts/remigration/**`, QA report JSON, `scripts/live_e2e_qa/`
- Push remote: `origin` → `nitsan-technologies/T3Planet-docs` (`master`), no force
- Mintlify: GitHub check "Mintlify Deployment" completed/success on `1d4f808` (org repo)
- QA: `mintlify validate` pass; full live crawl 810/810 nav pages 200 with content, 0 soft 404; 40/40 sampled new redirects 308; content markers 11/11 on docs.t3planet.de and t3planet.mintlify.app; desktop/mobile × light/dark on changed pages (0 broken images, 0 page errors, no horizontal scroll); search finds new T3AA sections; sitemap lists new pages; TLS valid
- Final status: PASS

### 2026-09-30 — Sidebar: product page tree no longer stays open on Home
- Authorization: operator said `start the deployment process`
- Commit: `8537545` by Nitsan `<sanjay@nitsantech.com>` (2 files; `a16303f..8537545`)
- Cause: Mintlify keeps sidebar group open state across client-side navigation; returning to Home (Back to all docs, browser Back, logo, footer link, back/forward) left the visited product tree expanded
- Scope: `scripts/src/custom.src.css` + rebuilt `custom.css` — on hub context, product rows without the current page render collapsed (no JS change)
- Excluded: `docs-master/`, `workshops/`, `backup/`, `scripts/remigration/**` (incl. new `sidebar_home_collapse_regression.py`), QA report JSON
- Push remote: `origin` → `nitsan-technologies/T3Planet-docs` (`master`), no force
- Mintlify: GitHub check "Mintlify Deployment" completed/success on `8537545` (org repo); new CSS on `t3planet.mintlify.app` and `docs.t3planet.de`
- QA: `mintlify validate` pass; pre-deploy baseline 14/50 (bug on all SPA return paths); live after deploy 50/50 desktop (7 products × 7 Home methods + chevron entry), 16/16 mobile (390/375), 11/11 dark; sitemap 851 URLs, llms.txt 200, 44/44 sampled pages 200 with content; only console error is pre-existing Mintlify CDN 403 for `lucide/v1.16.0/circle-help.svg`
- Final status: PASS WITH NON-BLOCKING WARNINGS

### 2026-10-02 — T3AI / T3AF migration from legacy docs + AI Providers Supademo
- Authorization: operator said `start the deployment process`
- Commit: `7b58d0b` by Nitsan `<sanjay@nitsantech.com>` (29 files; `0622725..7b58d0b`)
- Scope: 17 `ExtNsT3AI/**` + 10 `ExtNsT3AF/**` pages reconciled against legacy docs-master and extension code (ns_t3ai 14.5.0, ns_t3af 1.2.2); outdated sections removed, dead Sphinx anchors removed, "AI Foundation" naming; AI Providers Supademo moved to top of page (duplicate removed); UpdateGuide client notes (Mistral provider, News extension) preserved; `_static/t3-stats*` timestamp only (pre-commit hook, counts unchanged 803/70)
- Excluded: `docs-master/`, `workshops/`, `backup/`, `scripts/remigration/**`, `scripts/*` QA JSON, `scripts/live_e2e_qa/`, `scripts/supademo_audit/`, `docs/migration/` audit
- Push remote: `origin` → `nitsan-technologies/T3Planet-docs` (`master`), no force; local and origin were in sync before commit (0/0)
- Mintlify: GitHub check "Mintlify Deployment" completed/success on `7b58d0b` (org repo); content markers on `t3planet.mintlify.app` and `docs.t3planet.de`
- QA: `mintlify validate` pass; 0 broken internal links / 0 missing images on changed pages; live sitemap 851 URLs → 844×200 + 7×308 known T3AA redirects (all resolve 200), 0 small/blank pages; 54/54 changed-page checks (desktop light + mobile dark), 0 broken images, 0 console errors; Supademos render (AI Providers 1, SEO 14, Pages 16, Media 7, AISettings 6, …); UpdateGuide notes live; search finds AI Providers; llms.txt 200; HTTPS valid
- Note: `ExtNsT3AF/T3Planet-Credit-System/Dashboard/Index` is an intentional one-line stub linking to AI Usage (not blank)
- Final status: PASS

### 2026-10-02 — General FAQ removed, T3AF AI Providers updates, T3AC list/link fixes
- Authorization: operator said `Start the deployment process`
- Commit: `f4dbd2f` by Nitsan `<sanjay@nitsantech.com>` (21 files; `2e45ff8..f4dbd2f`)
- Scope: root `FAQ/Index.mdx` removed (nav entry removed, redirect `/FAQ/Index` → `/License/Index`, general-FAQ sentence removed from 8 product FAQs); T3AF AI Providers — "Capabilities and Their Purpose" table, capabilities marked required, DeepL API-key link, `tool_use` removed, Governance and status section removed, replaced provider-02 screenshot; T3AC — nested lists restored (AI Logs, AI Statistics, Data Source, Installation, Custom LLM Prerequisites) and History cleanup link on DPA & GDPR after old-vs-new comparison; stats regenerated (803 pages / 70 products)
- Excluded: `docs-master/`, `workshops/`, `backup/`, `scripts/remigration/**`, `scripts/*` QA JSON, `scripts/live_e2e_qa/`, `scripts/supademo_audit/`
- Push remote: `origin` → `nitsan-technologies/T3Planet-docs` (`master`), no force; local and origin were in sync before commit (0/0)
- Mintlify: GitHub check "Mintlify Deployment" completed/success on `f4dbd2f` (org repo)
- QA: `mintlify validate` pass; content markers on docs.t3planet.de (capabilities table, DeepL link, Governance/tool_use gone, DPA link, nested lists); `/FAQ/Index` 308 → `/License/Index`, absent from sitemap; new screenshot 200; 84/84 live checks (7 pages × 1440/1280/1024/768/390/375 × light/dark): 0 blank, 0 overflow, 0 broken images, 0 page errors; search works; sitemap and llms.txt 200
- Warning: `.md` export of product FAQ pages on docs.t3planet.de still served the old general-FAQ sentence right after deploy (edge cache); origin `t3planet.mintlify.app` and rendered HTML already correct
- Final status: PASS WITH NON-BLOCKING WARNINGS

### 2026-10-08 — Karma Site Sets Supademo, AI extensions remigration, TonicTypes updates
- Authorization: operator said `Start the deployment process`
- Commit: `f0ef27a` by Nitsan `<sanjay@nitsantech.com>` (33 files; `c4ebaf3..f0ef27a`)
- Scope: EXTKarma Theme Options — Site Sets Supademo switched from `?preview=true&step=1` (File Not Found for logged-out visitors) to public `?utm_source=link`; T3AI/T3AC/T3AS/T3AA/T3AL/T3AF remigration (missing content restored, flattened lists/anchors/code blocks fixed, 21 pages); TonicTypes — Predefined Datatype Import dashboard widget + `dashboard_import.webp`, FlexForm Field example, Repeater marked as planned for 2.2.0 (8 pages); `_static/t3-stats*` timestamp only (803 pages / 70 products)
- Excluded: `docs-master/`, `workshops/`, `backup/`, `scripts/**` QA artifacts, `docs/migration/` report, `dashboard_import.jpg` (unreferenced source)
- Push remote: `origin` → `nitsan-technologies/T3Planet-docs` (`master`), no force; local and origin in sync before commit (0/0)
- Mintlify: GitHub check "Mintlify Deployment" completed/success on `f0ef27a` (org repo)
- QA: `mintlify validate` pass; 30/30 changed pages on local preview and on docs.t3planet.de — HTTP 200, 0 broken images, 0 broken internal links, no `preview=true` Supademos; content markers 9/9 live; Karma Site Sets demo renders on live (desktop light + mobile dark); origin `t3planet.mintlify.app` matches; homepage 803 pages; sitemap and llms.txt 200
- Note: local preview returned 500 after `mintlify broken-links` ran (shared cache); restarted, not a content issue
- Final status: PASS
