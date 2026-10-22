---
title: "2.0.1 - 12 October 2026"
description: "AI Foundation (EXT:ns_t3af) v2.0.1 release notes."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AF"
  - "2.0.1 - 12 October 2026"
sidebarTitle: "2.0.1"
---

Patch release on the 2.0 line.

Here is the list of features and updates introduced in this release:

- 12-10-2026 [BUGFIX] MCP records_apply: defer DataHandler cache flush until after commit so TRUNCATE cannot end the transaction (sys_category / dryRun)
- 12-10-2026 [BUGFIX] MCP records_apply: refuse dryRun when the batch includes sys_category (interim: staging must prove deferred flush on MariaDB; remove the refusal in a follow-up once check #1 passes)
- 12-10-2026 [BUGFIX] MCP records_apply: if the DB transaction is gone after DataHandler, return ok:false with new ids (partial write), do not pretend to roll back
- 12-10-2026 [BUGFIX] MCP records_apply / write_table: attach the TYPO3 site on TYPO3_REQUEST for page writes (shared McpSiteRequestBootstrap); warn when a page has no site instead of failing the batch
- 12-10-2026 [BUGFIX] MCP file_upload_from_url: pinned-DNS downloads must not set Guzzle stream together with curl (regression guard + unit test; 2.0.0 still combined them)
- 12-10-2026 [FEATURE] MCP pages_search / content_search / record_search: selectFields (same semantics as content_list)
- 12-10-2026 [FEATURE] MCP pages_get / content_get: selectFields may include tstamp, crdate, cruser_id
- 12-10-2026 [BUGFIX] MCP uploads: allow woff/woff2 in mediafile_ext; map application/octet-stream and application/font-woff* to font/woff and font/woff2; surface TYPO3 consistency errors; file_upload_from_url failures throw (isError)
- 12-10-2026 [BUGFIX] MCP uploads: SHA-1 dedupe only reuses a file in the same folder and refuses a mismatched extension (JPEG bytes as .woff2 no longer return the existing jpg)
- 12-10-2026 [TASK] MCP initialize serverInfo.version reports 2.0.1
- 12-10-2026 [TASK] AI Agent QA (separate commits on feature/ai-agent): attachment handling, SEO/page-structure fixes, news guard, and related editor UX
