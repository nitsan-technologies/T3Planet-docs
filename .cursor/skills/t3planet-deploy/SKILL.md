---
name: t3planet-deploy
description: >-
  Production deployment for T3Planet Mintlify docs: inspect, validate, commit as
  Nitsan, push nitsan-technologies/T3Planet-docs, verify Mintlify/live, full QA.
  Use when the user says start deployment, start the deployment process, deploy
  latest docs, push docs live, or release documentation.
---

# T3Planet docs production deploy

Source of truth for humans: [`docs/deployment/deploy.md`](../../../docs/deployment/deploy.md).  
Safety guardrails: [`.cursor/rules/deployment-safety.mdc`](../../rules/deployment-safety.mdc) and [`.cursor/rules/mintlify-deployment.mdc`](../../rules/mintlify-deployment.mdc).

## Triggers

- start the deployment process / start deployment
- deploy the documentation / deploy latest docs
- push latest docs live / release the documentation

## Hard exclusions (never stage/commit/push/deploy)

```text
docs-master/
workshops/
backup/
```

Also exclude unless explicitly requested: `scripts/remigration/**`, QA dumps, secrets, `node_modules/`.

**Never** `git add .` / `git add -A` without printing and verifying `git diff --cached --name-only`.

Do not delete, reset, or stash excluded directories.

## State machine

```text
BACKUP (if sync risk) → DISCOVERY → VERIFY NITSAN IDENTITY
→ VERIFY origin = nitsan-technologies/T3Planet-docs · master
→ FETCH / COMPARE → SAFE SYNC → CHANGE REVIEW → LOCAL VALIDATION
→ MANIFEST → STAGE → COMMIT (Nitsan) → PUSH origin master
→ VERIFY GITHUB → VERIFY MINTLIFY → WAIT BUILD → LIVE QA → REPORT
```

Never jump from `PUSH` to `PASS`. Never force-push `master`.

**Never** delete/recreate the Cloudflare custom hostname for `docs.t3planet.de` to flush cache (breaks SSL). See `.cursor/rules/custom-domain-ssl-safety.mdc`.

## Procedure

1. **Backup** — if about to pull/merge/sync over dirty work, snapshot under `backup/pre-deployment-YYYYMMDD-HHMMSS/` (mintignored).
2. **Discovery** — `git rev-parse --show-toplevel`, `remote -v`, branch, status, log.
3. **Remote** — must be `nitsan-technologies/T3Planet-docs`. Mismatch → STOP.
4. **Identity** — commit as **Nitsan** `<sanjay@nitsantech.com>` via env (do not rewrite git config unless asked). Verify with `git config user.name` / `user.email` and/or env. Git identity ≠ GitHub auth.
5. **Fetch / compare** — `git fetch origin`; inspect ahead/behind; sync safely (`pull --ff-only` or merge). Preserve uncommitted work.
6. **Classify diffs** — PRODUCTION vs EXCLUDED vs TEMPORARY.
7. **Validate** — links/images/Supademos on changed pages; `mintlify validate` (Node 20); `compute_doc_stats.py` if nav/pages changed.
8. **Manifest** — list Included/Excluded; stage only Included paths.
9. **Gate** — abort if cached names include `docs-master/` or `workshops/`.
10. **Commit** — meaningful `docs: …` message as Nitsan.
11. **Push** — re-check `git remote -v` then `git push origin HEAD:master` (no force).
12. **Mintlify** — Activity must show org repo `master`. Prefer reconnect if still on a fork; emergency same-SHA fork sync only if live is blocked. Tell user which path was used.
13. **Wait** — Successful + content markers on live (not HTTP 200 alone).
14. **QA** — sitemap/llms/nav inventory; HTTP; blank pages; nav; search; responsive; light/dark; images/icons/Supademos; latest-change regression.
15. **Report** — template in `deploy.md`; status exactly one of `PASS` | `PASS WITH NON-BLOCKING WARNINGS` | `BLOCKED` | `FAILED`. Use `NOT VERIFIED` when needed.
16. **History** — append `docs/deployment/deployment-history.md`.

## Definition of done

GitHub push **and** Mintlify deploy **and** live verification **and** post-deploy QA evidence. Do not claim PASS without evidence.
