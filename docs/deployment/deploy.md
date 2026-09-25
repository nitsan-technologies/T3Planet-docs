# T3Planet Documentation Deployment Guide

Human-readable SOP for production docs releases. Cursor agents follow the same flow via `.cursor/skills/t3planet-deploy/SKILL.md` when you say **start the deployment process**, **start deployment**, or **deploy latest documentation**.

## 1. Purpose

Move **verified production documentation** from the local Git worktree → GitHub → Mintlify → [https://docs.t3planet.de/en/latest/](https://docs.t3planet.de/en/latest/), then prove the live site is healthy (HTTP, navigation, search, responsive, themes, latest-change regression). A green `git push` alone is **not** a successful deployment.

## 2. Production URL

```text
https://docs.t3planet.de/en/latest/
```

Also useful:

```text
https://docs.t3planet.de/en/latest/sitemap.xml
https://docs.t3planet.de/en/latest/llms.txt
```

## 3. GitHub Repository (source of truth)

```text
https://github.com/nitsan-technologies/T3Planet-docs.git
```

| Field | Value |
| --- | --- |
| Organization | `nitsan-technologies` |
| Repository | `T3Planet-docs` |
| Production branch | `master` |
| Local remote name | `origin` |

Verify before every push (do **not** assume `origin` is correct):

```bash
git remote -v
git branch --show-current
git rev-parse --show-toplevel
```

Expected:

```text
origin  https://github.com/nitsan-technologies/T3Planet-docs.git
```

If the remote is not the org repo: **STOP**. Do not silently change remotes. Report current vs expected.

**Do not** use a personal fork (`markus-neumannn/T3Planet-docs` or any other) as the production Mintlify source.

## 4. Mintlify Project

| Field | Expected / verified |
| --- | --- |
| Project | **T3Planet Docs** (workspace **nitsan-81630f36**) |
| Live status | Live |
| Production URL | `docs.t3planet.de/en/latest` |
| **Required** Git connection | `nitsan-technologies/T3Planet-docs` · `master` |
| Dashboard | [Mintlify Activity](https://app.mintlify.com/t3planet/t3planet/activity) |

**Always re-verify** Activity / Git settings before treating a push as live.

### Architecture

```text
Nitsan organization
        ↓
nitsan-technologies/T3Planet-docs
        ↓
master
        ↓
Mintlify (T3Planet Docs)
        ↓
https://docs.t3planet.de/en/latest/
```

If Activity still shows a personal fork while we push only to the org repo, live will **not** update from `origin`. Prefer reconnecting Mintlify Git to the org repo. Emergency same-SHA fork sync is temporary only (see `.cursor/rules/mintlify-deployment.mdc`). Tell the operator when emergency sync was used.

Do **not** change domain, org, env vars, or Git connection without explicit authorization.

## 5. Git identity vs authentication (Nitsan)

These are **different**:

| Concept | What it controls |
| --- | --- |
| Git commit identity | Author/committer **name + email** in the commit metadata |
| GitHub authentication | Permission to **push** (token / SSH / `gh` login) |
| Repository ownership | Where the commit lands (`nitsan-technologies/T3Planet-docs`) |
| Mintlify Git source | Which repo/branch Mintlify **builds** for live |

### Approved Nitsan commit identity

Use the **Nitsan** author for production deployment commits. Verified on org history as:

```text
Nitsan <sanjay@nitsantech.com>
```

Before committing, verify:

```bash
git config user.name
git config user.email
```

Prefer one-shot env for the commit (do **not** rewrite global `git config` unless the operator asks):

```bash
GIT_AUTHOR_NAME='Nitsan' \
GIT_AUTHOR_EMAIL='sanjay@nitsantech.com' \
GIT_COMMITTER_NAME='Nitsan' \
GIT_COMMITTER_EMAIL='sanjay@nitsantech.com' \
git commit -m "…"
```

**Do not:**

- Invent or forge emails / tokens
- Commit as Cursor / ChatGPT / OpenAI / a personal agent name
- Confuse commit author with a personal **fork** owner
- Assume `git config user.name "Nitsan"` authenticates GitHub (it does not)

## 6. Backup before sync

Before pull, reset, rebase, merge, checkout that discards work, or any other sync that could overwrite local work:

1. Record `git status`, remotes, `HEAD`, branch
2. Prefer a timestamped snapshot under `backup/pre-deployment-YYYYMMDD-HHMMSS/` (Git-only; must stay in `.mintignore`)
3. Keep uncommitted production work recoverable

Never publish `backup/` through Mintlify.

## 7. Pull before push (safe sync)

Never push local changes before synchronizing with organization `master`.

```bash
git fetch origin
git status -sb
git rev-list --left-right --count origin/master...HEAD
git log --oneline --decorate --graph --all -20
```

- If **behind**: preserve local work → `git pull --ff-only origin master` (or merge safely) → resolve → test
- If **diverged**: **STOP**, backup, compare both sides, do not force-push
- If **uncommitted changes**: preserve them before sync; do not `git reset --hard` / `git clean` blindly

**Never** `git push --force` / `git push -f` on production `master`.

## 8. Production source vs exclusions

### Production source

Repository root of `nitsan-technologies/T3Planet-docs` (Mintlify docs at repo root: `docs.json`, product folders, `custom.css`, `_static/`, etc.).

### Never deploy

```text
docs-master/
workshops/
```

Also never deploy by default (unless explicitly requested):

```text
scripts/remigration/**
RST Format */**
*.env / credentials / tokens
node_modules/
backup/
local QA dumps, screenshots-only artifacts, debug JSON
```

**NEVER use `git add .` or `git add -A` without validating the exact staging set.**

## 9. Pre-deployment checklist

- [ ] Backup recorded if sync risk exists
- [ ] Correct worktree / remote / branch (`nitsan-technologies/T3Planet-docs` · `master`)
- [ ] Nitsan author identity verified
- [ ] `git fetch` + divergence reviewed; pull/synchronize safely if needed
- [ ] Diff reviewed; exclusions confirmed absent from staging
- [ ] No secrets
- [ ] `mintlify validate` (Node 20) when possible
- [ ] Stats regenerated if nav/pages changed (`python3 scripts/compute_doc_stats.py`)
- [ ] Intended pages/assets/Supademos spot-checked locally

## 10. Git status and review

```bash
git status --short
git status -sb
git diff --stat
git diff
git diff --cached --stat
git diff --cached
```

Classify each path: `PRODUCTION` | `EXCLUDED` | `UNRELATED` | `GENERATED` | `TEMPORARY` | `UNKNOWN`.

## 11. Validate documentation

- Markdown/MDX, frontmatter, `docs.json` nav, redirects
- Internal links, images, icons, Supademo embeds on **changed** pages
- `mintlify validate` on Node 20

## 12. Deployment manifest

Before commit, list **Included** and **Excluded**. Final gate:

```bash
git diff --cached --name-only
```

Abort if any path under `docs-master/` or `workshops/` appears.

## 13. Commit

Meaningful message, e.g. `docs: ship Media/TonicTypes updates and footer flush CSS`.

```bash
# after commit
git log -1 --format='%h %an <%ae> %s'
```

Confirm author is **Nitsan**.

## 14. Push to GitHub

Re-verify remotes, then:

```bash
git remote -v
git branch -vv
git log --oneline -5
git push origin HEAD:master
```

**Never** force-push `master` unless the operator explicitly authorizes it.

Record commit hash, message, branch, remote.

## 15. Mintlify deployment

1. Open Activity; confirm connected repo/branch = org `master`
2. Confirm new commit appears
3. Wait for **Successful** + Live — do not start final QA while building

## 16–28. Post-deploy QA

Confirm `https://docs.t3planet.de/en/latest/` reflects the release (not localhost). Inventory routes from `docs.json` / sitemap / hubs. Check HTTP (no unexpected 404/5xx), navigation, search, responsive (1440/1280/1024/768/390/375), light/dark, images, icons, Supademos, and latest-change regression. Use **NOT VERIFIED** when a check could not be done.

## 29. Hotfix process

Reproduce → minimal fix → validate → commit as **Nitsan** → push `origin` → wait → retest. No drive-by refactors. No force-push.

## 30. Final deployment checklist

Success requires GitHub + Mintlify + LIVE + QA evidence. See Definition of Done in `.cursor/skills/t3planet-deploy/SKILL.md`.

## 31. Deployment report template

```text
Deployment date:
Operator:
Repository: nitsan-technologies/T3Planet-docs
Branch: master
Commit / message / author:
Git push:
Mintlify project / connected repo / branch:
Deployment status:
Production URL:
Pages discovered / checked:
404 / 500 / 502 / 503:
Blank pages:
Navigation / Search / Responsive / Theme:
Images / Icons / Supademos:
Latest changes verified:
Issues / Fixes:
Final status: PASS | PASS WITH NON-BLOCKING WARNINGS | BLOCKED | FAILED
```

## 32. Troubleshooting

| Symptom | Check |
| --- | --- |
| Push OK, live stale | Mintlify Git still on fork? Activity SHA? CDN cache? |
| Build failed | Mintlify logs, MDX/`docs.json`, `mintlify validate` |
| Many 404s | Nav vs files, redirects, path renames |
| Search empty | Index lag after deploy; retry later; confirm pages in sitemap |
| Footer / CSS missing | `custom.css` in commit? hard refresh |

## 33. Deployment history

Append each release to [deployment-history.md](./deployment-history.md).

## Trigger phrases

When the operator says any of:

- start the deployment process
- start deployment
- deploy the documentation / latest docs
- push latest docs live
- release the documentation

run this SOP via `.cursor/skills/t3planet-deploy/SKILL.md`.
