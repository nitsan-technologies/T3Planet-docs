---
title: "Ask AI agent"
description: "Use the AI agent in the TYPO3 backend to run T3AA accessibility features in plain language: missing alt text, alt drafts, WCAG scans, Fix Hub suggestions, PageSpeed, summaries, and voice-over. Nothing is saved until you approve."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AA"
  - "AI agent"
  - "MCP"
  - "Accessibility"
sidebarTitle: "Ask AI agent"
---

The **AI agent** is a chat window inside the TYPO3 backend. You describe an accessibility task in plain language, for example *"Which images have no alt text?"* or *"What accessibility issues does this page have?"*. The agent reads the page you are working on, picks the right T3AA tool, and prepares the change. You review the change and decide whether it is saved.

The AI agent UI ships with **AI Foundation** (`ns_t3af`). When **T3AA** (`ns_t3aa`) is installed with AI Foundation, it adds **14 T3AA MCP tools** to the agent: alt text, accessibility scans and issues, Fix Hub suggestions, PageSpeed, content summary, and voice-over.

<Note>
The chat window, providers, preview/Apply flow, and keyboard shortcut are part of AI Foundation. T3AA only adds the accessibility tools. For the shared UI chrome, see [AI Foundation: Ask AI agent](/ExtNsT3AF/AskAiAgent/Index).
</Note>

![TYPO3 backend top bar with the Ask AI Agent button and Ctrl/Cmd+Shift+K](./images/t3aa-agent-topbar-button.webp)

![Empty AI agent window on Non-Composer TYPO3 v14 — Start a conversation](./images/t3aa-agent-window-empty.webp)

## Agent chat vs the AI Accessibility module

| Surface | What it is |
|---|---|
| **Ask AI Agent** (top bar) | Chat on the current page. Uses T3AA MCP tools plus AI Foundation core tools. |
| **AI Accessibility** module | Standalone tabs: Dashboard, AI Alt Text, Scans, Fix Hub, Voiceover, and related screens. See the [Feature Guide](/ExtNsT3AA/FeatureGuide/Index). |

Both paths use the same T3AA business logic. Prefer the agent when you want a quick, page-scoped request; prefer the module for bulk queues, dashboards, and long-running jobs.

## Get started in three steps

<Steps>
  <Step title="Select the page">
    Select the page you want to work on in the page tree, for example in **Content > Layout**. The AI agent uses this page as its context.
  </Step>
  <Step title="Click Ask AI Agent">
    Click **Ask AI Agent** in the center of the backend top bar, or press `Ctrl/Cmd+Shift+K`. The AI agent window opens on top of the page.
  </Step>
  <Step title="Ask, review, apply">
    Type your request, for example *"Which images have no alt text?"*, and press Enter. For a change, review the preview card, then click **Apply** to save it or **Cancel** to discard it.
  </Step>
</Steps>

<Warning>
- Nothing is saved until you click **Apply**. **Cancel** or **Discard** writes nothing.
- An applied change is saved in the **selected workspace**. In **Live**, it is public immediately. See [Live or draft workspace](/ExtNsT3AF/AskAiAgent/HowItWorks/Index#live-or-draft-workspace) in the AI Foundation manual.
- The AI agent has **your** backend permissions, never more.
- T3AA tools also need an active T3AA license and a configured AI provider in AI Foundation.
</Warning>

## Read the pages in this order

| Page | What you learn |
|---|---|
| [Where the AI agent opens](/ExtNsT3AA/AskAiAgent/WhereOpens/Index) | Where to find the AI agent, and what each part of its window does. |
| [How it works](/ExtNsT3AA/AskAiAgent/HowItWorks/Index) | How a request runs, read vs write tools, and what you need before you start. |
| [Your first accessibility request](/ExtNsT3AA/AskAiAgent/StepByStep/Index) | Step by step: find missing alt text, review a write preview, and cancel safely. |
| [T3AA tools](/ExtNsT3AA/AskAiAgent/Tools/Index) | All 14 T3AA tools, their names in the agent, and the matching feature pages. |
| [Example requests](/ExtNsT3AA/AskAiAgent/ExampleRequests/Index) | Ready-to-use requests for alt text, scans, Fix Hub, PageSpeed, and voice-over. |
| [Troubleshooting](/ExtNsT3AA/AskAiAgent/Troubleshooting/Index) | Verified failures and how to solve them. |

## Related

- [AI Foundation: Ask AI agent](/ExtNsT3AF/AskAiAgent/Index): UI, settings, and AI Agent module tabs.
- [Feature Guide](/ExtNsT3AA/FeatureGuide/Index): Dashboard, AI Alt Text, Scanner, Fix Hub, Voiceover, and other module workflows.
- [AI Foundation MCP Server](/ExtNsT3AF/Integrations/MCPServer/Index): use the same T3AA tools from Cursor, Claude Desktop, or other MCP clients.
