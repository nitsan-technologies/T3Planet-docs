---
title: "Troubleshooting"
description: "Solve common problems with T3AI tools in the AI agent: missing tools, wrong tool or page selected, failed previews, queues that do not run, busy agent, credit and request limits, and stopped turns."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AI"
  - "AI agent"
  - "Troubleshooting"
sidebarTitle: "Troubleshooting"
---

For general AI agent messages, see [AI agent troubleshooting](https://docs.typo3.org/p/nitsan/ns-t3af/main/en-us/AskAiAgent/Troubleshooting.html) in the AI Foundation manual.

## T3AI tools are missing

**AI Foundation > AI Agent > Overview** does not list **T3AI** under **Tools by owning extension**, or the AI agent never uses T3AI tools.

- Check that `ns_t3ai` is installed and active, then clear all caches.
- Compare **Executable** and **Locked** for T3AI on the Overview tab. AI Foundation applies entitlement rules, so check that the T3AI license is active.
- Check **AI Foundation > AI Agent > Severity policy**. Tools that are listed as **Unclassified** are locked.
- Check that the backend user group has AI agent access in [AI Permissions](/en/latest/ExtNsT3AF/Configuration/AIPermissions/Index).

## The AI agent uses a generic tool instead of T3AI

For example, *Create a news article* runs **Change a record** and fails with `data must be a JSON object of field values`.

- Repeat the request with *Use T3AI to …*, for example *Use T3AI to create a simple news record about …*.
- Use a model with reliable tool calling. Smaller models choose the wrong tool more often. You can switch the model in the AI agent footer.

## "I can't find a page called …"

The model read part of the request as a page title, for example the word *Add* in *Add this page to the Mass SEO queue*.

- Use a different verb: *Queue this page for Mass SEO*.
- Pick the correct page from the suggestions, or reference it directly with `@pages:<uid>`.

## The preview is not what I asked for

- Click **Cancel** or **Discard**. The AI agent confirms *Nothing was written*. It may then ask a follow-up question or prepare a new preview.
- For SEO fields, choose **Custom** and enter your own value before **Apply selected**.
- Each SEO preview uses AI credits. Regenerating uses them again.

## Translation does not show the language I need

`t3ai_translate_page` uses the languages that are configured for the site.

- Add the language to the site configuration first.
- Name the language in the request, for example *Translate this page into French*.
- Check the provider and glossary setup in [Translation](/en/latest/ExtNsT3AI/Translation/Index) and [Language Glossary](/en/latest/ExtNsT3AI/Translation/LanguageGlossary/Index).

## Queued pages are not processed

Queue tools only add, remove, or requeue entries. The pages are processed by the Scheduler.

- Mass SEO: create and run a Scheduler task with `nst3ai:bulk:seo-optimize`. See [Mass SEO](/en/latest/ExtNsT3AI/MassSEO/Index).
- Mass Translation: configure the Scheduler task described in [Mass Translation](/en/latest/ExtNsT3AI/Translation/MassTranslation/Index).
- Ask *Show the Mass Translation queue* to see the status and attempts for each entry. Use *Retry the failed entries in the Mass Translation queue* after you fix the cause.

## "The AI Agent is still working on your previous request"

A previous turn is still running, for example a page translation. Wait until it finishes, then send the message again.

## The turn is blocked or stops

| Message or behavior | Cause | Fix |
|---|---|---|
| Turn blocked, monthly credits exhausted | Monthly credit cap of the user group | Raise the cap in [AI Permissions](/en/latest/ExtNsT3AF/Configuration/AIPermissions/Index) or wait for the next period |
| Turn blocked after many requests today | Daily request cap | Raise the cap in AI Permissions |
| Provider or model rejected | Provider allowlist or model override | Allow the provider, or enable model override for the group |
| Warning at 20 tool calls, turn stops at 40 | Turn guard of the AI agent runtime | Split large jobs into smaller requests, or use [Mass SEO](/en/latest/ExtNsT3AI/MassSEO/Index) and [Mass Translation](/en/latest/ExtNsT3AI/Translation/MassTranslation/Index) |

## Applied by mistake

After **Apply**, the result card offers **Undo**. In a draft workspace, the change stays in that workspace until it is published.
