# Deployment checklist (quick)

- [ ] Backup if sync could overwrite local work (`backup/pre-deployment-…`, mintignored)
- [ ] `git remote -v` → `https://github.com/nitsan-technologies/T3Planet-docs.git`
- [ ] Branch `master`
- [ ] `git fetch origin` + ahead/behind reviewed; sync safely before push
- [ ] Nitsan author for commit (`Nitsan <sanjay@nitsantech.com>`) — identity ≠ GitHub auth
- [ ] Diff reviewed; no secrets
- [ ] **No** `docs-master/` or `workshops/` in staging
- [ ] No blind `git add .`
- [ ] `mintlify validate` (Node 20) when possible
- [ ] Push `origin HEAD:master` (no force)
- [ ] Mintlify Activity: **org** repo + Successful build
- [ ] Live URL shows new content (not HTTP 200 alone)
- [ ] HTTP / nav / search / responsive / theme / latest-change QA
- [ ] History entry + final status
