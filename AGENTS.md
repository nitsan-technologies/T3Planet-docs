# AGENTS.md — T3Planet Docs

> Internal only — excluded from Mintlify publishing via `.mintignore`.

## Production deployment

When the operator says **start the deployment process**, **start deployment**, **deploy latest docs**, or **push docs live**:

1. Follow [`.cursor/skills/t3planet-deploy/SKILL.md`](.cursor/skills/t3planet-deploy/SKILL.md).
2. Human SOP: [`docs/deployment/deploy.md`](docs/deployment/deploy.md).
3. Safety: [`.cursor/rules/deployment-safety.mdc`](.cursor/rules/deployment-safety.mdc), [`.cursor/rules/mintlify-deployment.mdc`](.cursor/rules/mintlify-deployment.mdc), and [`.cursor/rules/custom-domain-ssl-safety.mdc`](.cursor/rules/custom-domain-ssl-safety.mdc).

**Repository:** `nitsan-technologies/T3Planet-docs` (`master`) via `origin`.  
**Commit author:** **Nitsan** `<sanjay@nitsantech.com>` (identity ≠ GitHub auth).  
**Never deploy** `docs-master/` or `workshops/`. Never force-push. Never claim success from GitHub push alone — verify Mintlify + live QA.  
**Never** delete/recreate the `docs.t3planet.de` Cloudflare custom hostname to flush cache (breaks SSL).

## Day-to-day docs

See [`.cursor/context.md`](.cursor/context.md) and [`.cursor/rules/t3planet-client.mdc`](.cursor/rules/t3planet-client.mdc) for voice, paths (`TonicTypes/`), and local LAN preview (`:3000`).
