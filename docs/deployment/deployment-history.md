# T3Planet documentation deployment history

Append one entry per production release.

---

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

