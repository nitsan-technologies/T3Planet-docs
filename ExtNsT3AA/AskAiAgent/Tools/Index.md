---
title: "T3AA tools"
description: "Reference of the 14 T3AA MCP tools in the AI agent: the name shown in the agent, the tool name, what it does, whether it reads or asks before changing, and the matching Feature Guide page."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AA"
  - "AI agent"
  - "MCP tools"
  - "Accessibility"
sidebarTitle: "T3AA tools"
---

T3AA adds **14 tools** to the AI agent when AI Foundation is present. You do not have to name a tool: the agent picks it from your request. The tables below show:

- **In the agent**: the name you see in the `/` picker, in steps, and on preview cards. You can also describe the task in your own words.
- **Tool**: the technical name (`t3aa_…`), shown when you expand a step, in **AI Foundation > AI Agent > Audit**, and in external MCP clients.
- **Kind**: **Only reads** or **Asks before changing**.

![The / picker in the AI agent lists tools by their name in the agent](../images/t3aa-agent-slash-menu.webp)

## Alt text and file metadata

| In the agent | Tool | What it does | Kind | Feature |
|---|---|---|---|---|
| Find images without alt text | `t3aa_list_files_missing_alt_text` | Lists image files with empty alt text (**decorative images are left out**). | Only reads | [AI Alt Text](/ExtNsT3AA/FeatureGuide/AIAltText/Index) |
| Show alt text drafts | `t3aa_alt_text_drafts_list` | Lists AI alt text drafts that wait for approval. The reply can show **Showing X of Y drafts**. | Only reads | [AI Alt Text](/ExtNsT3AA/FeatureGuide/AIAltText/Index) |
| Queue folder for alt text | `t3aa_alt_text_queue_folder` | Queues a fileadmin folder so AI alt drafts are generated in the background. | Asks before changing | [AI Alt Text](/ExtNsT3AA/FeatureGuide/AIAltText/Index) |
| Approve alt text drafts | `t3aa_alt_text_approve` | Approves drafts so they become the live alternative text. You can approve selected drafts or **all** pending drafts. | Asks before changing | [AI Alt Text](/ExtNsT3AA/FeatureGuide/AIAltText/Index) |
| Read file metadata | `t3aa_get_file_metadata` | Reads alt text, title, description, and **`public_url`**. The agent must quote `public_url` and never invent a URL. | Only reads | [AI Alt Text](/ExtNsT3AA/FeatureGuide/AIAltText/Index) |
| Update file metadata | `t3aa_update_file_metadata` | Generates or updates alt text, title, and description (DualMode + previewable). If the file already has texts, the agent can offer **Regenerate all**, **Fill empty fields only**, or **Keep current texts**. | Asks before changing | [AI Alt Text](/ExtNsT3AA/FeatureGuide/AIAltText/Index) |
| Mark an image as decorative | `t3aa_mark_image_decorative` | Marks an image as decorative (or clears the mark). Accepts a **file UID** or a **file path**. | Asks before changing | [AI Alt Text](/ExtNsT3AA/FeatureGuide/AIAltText/Index) |
| Get file for metadata *(MCP)* | `t3aa_get_file_for_metadata` | Returns a fetchable image URL plus current metadata for external vision. Hidden from the agent UI; available to MCP clients. | Only reads | [AI Alt Text](/ExtNsT3AA/FeatureGuide/AIAltText/Index) |

Alt-text flow: **list missing** → **queue folder** → **drafts list** → **approve** / **mark decorative**.

## Accessibility scans and Fix Hub

| In the agent | Tool | What it does | Kind | Feature |
|---|---|---|---|---|
| Run accessibility scan | `t3aa_accessibility_scan_run` | Runs a WCAG accessibility scan for a page and returns score and issues. Uses the scan quota of the license. | Asks before changing | [Scanner](/ExtNsT3AA/FeatureGuide/Scans/Index) |
| Show accessibility issues | `t3aa_accessibility_issues` | Shows score and issues from the **last** scan of a page. **Only reads** — it never starts a new scan. | Only reads | [Fix Hub](/ExtNsT3AA/FeatureGuide/FixHub/Index) |
| Suggest accessibility fixes | `t3aa_accessibility_fix_suggestions` | AI fix suggestions for issues from the last scan (what to change, corrected HTML, why). Does not mutate the page. | Only reads | [Fix Hub](/ExtNsT3AA/FeatureGuide/FixHub/Index) |

Asking *"What accessibility issues does this page have?"* or *"Check this page for accessibility problems"* **only reads** the last scan result. Asking *"Scan this page for accessibility problems"* or *"Run a WCAG scan on this page"* opens a **scan** preview and asks you to confirm before it runs.

## Performance, content, and media

| In the agent | Tool | What it does | Kind | Feature |
|---|---|---|---|---|
| Check page speed | `t3aa_get_page_speed` | Fetches Google PageSpeed Insights scores (performance, accessibility, SEO, best practices) for a page URL. The result is **not** saved to the T3AA Lighthouse report in the backend. | Only reads | [Lighthouse / PageSpeed](/ExtNsT3AA/FeatureGuide/Scans/Lighthouse/Index) |
| Summarize content | `t3aa_summarize_content` | Summarizes or **simplifies** content (DualMode). A named page number is passed as `pageId`; a named language (for example German) is passed on. The tool **returns text** — it does not write the page by itself. If the agent then offers to save the text on the page, that is a separate write preview (**Apply** / **Cancel**). | Only reads (write only after a later Apply) | [Content](/ExtNsT3AA/FeatureGuide/Content/Index) · [Simplified Text](/ExtNsT3AA/FeatureGuide/SimplifiedText/Index) |
| Generate voice-over | `t3aa_generate_voice_over` | Creates an MP3 voice-over with AI text-to-speech from text or from a page. Uses the editor’s **default audio provider** (OpenAI or ElevenLabs). | Asks before changing | [AI Voiceover](/ExtNsT3AA/FeatureGuide/AIVoiceover/Index) |

## Related

- [Example requests](/ExtNsT3AA/AskAiAgent/ExampleRequests/Index)
- [AI Foundation MCP Tools](/ExtNsT3AF/Integrations/MCPTools/Index): core tools the agent combines with T3AA tools (pages, content, files, workspaces).
- [AI Foundation MCP Server](/ExtNsT3AF/Integrations/MCPServer/Index): use the same T3AA tools from external MCP clients.
