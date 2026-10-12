---
title: "Example requests"
description: "Ready-to-use AI agent requests that use only tools shipped with AI Foundation, plus the / and @ input helpers for tools and records."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AF"
  - "ns_t3af"
  - "AI agent"
sidebarTitle: "Example requests"
---

<a id="ask-ai-agent-examples"></a>

The following requests use only tools that ship with AI Foundation. Open the AI agent on the page you are editing; "this page" means the page shown in the context line.

| Request | Tool | Result |
|---|---|---|
| `What can you do on this page?` | `explain_capabilities` | Lists the actions available to you on the current page. |
| `Show me the details of this page.` | `pages_get` | Shows the properties of the current page. |
| `List the content elements on this page.` | `content_list` | Lists the content elements of the page. |
| `Find all pages with "contact" in the title.` | `pages_search` | Lists matching pages with their IDs. |
| `Show the page tree below this page.` | `pages_tree` | Shows the subpages as a tree. |
| `Add a text element with a short welcome text to this page.` | `write_table` | Prepares a change card. Nothing is saved until you click **Apply**. |

Two input helpers let you be more precise:

- Type `/` to pick a tool directly, for example `/pages_tree`.
- Type `@` to point at a record, for example `@pages:12` or `@tt_content:198`.

Both helpers also work when the AI provider cannot call tools.
