---
title: "Known Problems"
description: "Known Problems for EXT:ns_t3af (T3AF)."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AF"
  - "ns_t3af"
sidebarTitle: "Known Problems"
---

Common problems with AI Foundation and how to fix them.

## Installation

**Composer conflicts with another MCP package**

T3AF includes an MCP server and conflicts with other MCP server packages such as `marekskopal/typo3-mcp-server` and `hn/typo3-mcp-server`. Remove those packages before installing `nitsan/ns-t3af`.

**Backend module is missing**

1. Check that AI Foundation (`ns_t3af`) is active in **Admin Tools → Extensions** (on TYPO3 v14: **System → Extensions**).
2. Clear all caches.
3. Still missing? Ask your developer to run:

  ```bash
  ./vendor/bin/typo3 extension:setup
  ./vendor/bin/typo3 cache:flush
  ```

Also confirm `scheduler` and `workspaces` are available. See [Installation](/en/latest/ExtNsT3AF/Installation/Index).

## Providers

**Provider request or Test connection fails**

1. Go to **AI Universe → AI Foundation → AI Providers**.
2. Check that the provider exists and **Provider enabled** is on.
3. Open the provider and click **Test connection**.
4. Check the API key, the model and the **Endpoint URL** (only for Custom / Other providers).
5. Ask your hosting provider whether the server may connect to the AI service (HTTPS).
6. Look for the exact error in **AI Logs**.

**Unexpected model or provider behavior**

- Check that the **default** provider is the one you expect.
- Check the model on the provider.
- Check the overrides in **AI Features**.

**No usage statistics shown**

- For OpenAI organisation charts, an OpenAI admin key is needed (see [Configuration](/en/latest/ExtNsT3AF/Configuration/Index)).
- Clear all caches and open **AI Usage** / **AI Logs** again.
- Ask your developer to check that `extension:setup` ran.

## Configuration

**HTTP 401 / 403 when fetching a protected URL**

The page is behind a browser login.

1. Go to **AI Universe → AI Foundation → AI Features**.
2. Open **Access & Notifications**.
3. Turn on **Enable Basic Authentication Support**.
4. Enter **Basic Auth Username** and **Basic Auth Password**.
5. Save and try again.

## MCP

**MCP client cannot connect**

- Confirm the MCP server is enabled in Extension Configuration.
- Prefer HTTPS on the site base URL.
- For Cursor and similar clients, follow [MCP Testing](/en/latest/ExtNsT3AF/Integrations/MCPTesting/Index).
- For stdio setups, keep the working directory and user/workspace flags correct.

**MCP writes fail after a successful connect**

Confirm the backend user has the required module, table, and workspace rights. See [AI Permissions](/en/latest/ExtNsT3AF/Configuration/AIPermissions/Index).

## Report an issue

Include TYPO3 version, PHP version, `ns_t3af` version, exact error text, and whether MCP is enabled. Submit via [Support](/en/latest/ExtNsT3AF/Support/Index).

{/* Original text before the 8 Oct 2026 simplification (kept for reference):

Verified issues and checks for **T3AF** (`EXT:ns_t3af`).

1. Confirm `ns_t3af` is active.
2. Flush all caches.
3. Run:

- Confirm the provider row exists and is **enabled** in T3AF > AI Providers.
- Run **Test connection** from the provider drawer.
- Check the API key, model ID, and endpoint URL (for custom/OpenAI-compatible rows).
- Confirm outbound HTTPS to the provider API works from the server.
- Review backend logs for entries from T3AF request logging.

- Confirm the **default** provider matches the feature you expect.
- Confirm the model ID on the provider row.
- Check feature-level provider overrides in T3AF > AI Features.

- Confirm an OpenAI admin/organization key is set where org usage charts are required.
- Clear caches and open T3AF > AI Usage / T3AF > AI Logs again.
- Confirm the dashboard analytics cache is available after `extension:setup`.

If you use the Basic Auth helper in Extension Configuration (`ns_t3af`):

- Enable `basicAuthEnabled`.
- Set `basicAuthUsername` and `basicAuthPassword`.
- Retry the protected URL fetch.
*/}
