---
title: "Scheduler & CLI"
description: "Scheduler tasks and console commands of T3AI: Mass Translation, Mass Re-translation, Mass SEO, glossary, AI error solutions, and cache, with Composer and non-Composer examples."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AI"
  - "Scheduler"
  - "CLI"
sidebarTitle: "Scheduler & CLI"
---

The mass features only fill a queue. A Scheduler task, or the matching command, processes the queued pages. The Scheduler only runs if a cron job triggers it on the server.

## Scheduler tasks

| Task | Processes | Task settings |
|---|---|---|
| **T3AF: Bulk Translate (queue)** | [Mass Translation](/en/latest/ExtNsT3AI/Translation/MassTranslation/Index) queue | **Batch size** (default 10), **Pages per run** (0 = whole queue) |
| **T3AF: Bulk Re-translate (queue)** | [Mass Translation](/en/latest/ExtNsT3AI/Translation/MassTranslation/Index) entries queued with mode **Re-translate** | **Batch size**, **Pages per run** |
| **T3AF: Mass SEO Optimization (queue)** | [Mass SEO](/en/latest/ExtNsT3AI/MassSEO/Index) queue | **SEO fields to generate** (meta title, meta description, keywords, OG title, OG description), limit, provider, dry run |

On TYPO3 v14 these are native Scheduler tasks. On TYPO3 v13, create an **Execute console commands** task and select the command from the table below.

## Console commands

| Command | What it does | Options |
|---|---|---|
| `t3af:bulk:translate` | Translates the pages in the Mass Translation queue | `--batch-size`, `--limit` / `-l` |
| `t3af:bulk:retranslate` | Re-translates the pages in the re-translation queue | `--batch-size`, `--limit` / `-l` |
| `t3af:bulk:seo-optimize` | Generates SEO data for the pages in the Mass SEO queue | `--fields` / `-f` (`metaTitle,metaDescription,keywords,ogTitle,ogDescription`), `--limit` / `-l`, `--page`, `--provider` / `-p`, `--model` / `-m`, `--dry-run` |
| `t3af:glossary:list` | Lists the glossary entries | |
| `t3af:glossary:remove` | Deletes all glossary entries after a confirmation | `--yes` / `-y` skips the confirmation |
| `t3af:exception:solve` | Asks the AI for a solution to an exception message | `problem` argument, `--code`, `--file`, `--line`, `--identifier`, `--refresh`, `--json` |
| `t3af:cache:flush` | Flushes the cached AI error solutions | optional `identifier` argument |

The older `nst3ai:*` names (for example `nst3ai:bulk:translate`) still work as aliases.

`--limit 0` means no limit. With `--limit 10`, one run processes up to 10 pending pages; the rest stay in the queue for the next run.

## Examples

Composer:

```bash
vendor/bin/typo3 t3af:bulk:translate --batch-size=10 --limit=10
vendor/bin/typo3 t3af:bulk:seo-optimize --fields=metaTitle,metaDescription --limit=20 --dry-run
vendor/bin/typo3 scheduler:run --task=<taskUid> -f
```

Non-Composer:

```bash
php typo3/sysext/core/bin/typo3 t3af:bulk:translate --batch-size=10 --limit=10
php typo3/sysext/core/bin/typo3 t3af:bulk:seo-optimize --fields=metaTitle,metaDescription --limit=20 --dry-run
php typo3/sysext/core/bin/typo3 scheduler:run --task=<taskUid> -f
```

Replace `<taskUid>` with the task UID from the Scheduler module.

**Related:** [Mass Translation](/en/latest/ExtNsT3AI/Translation/MassTranslation/Index) · [Mass SEO](/en/latest/ExtNsT3AI/MassSEO/Index) · [AI Usage & AI Logs](/en/latest/ExtNsT3AI/Configuration/AIUsageAndLogs/Index) · [Scheduler & CLI in AI Foundation](/en/latest/ExtNsT3AF/Configuration/Index#scheduler-and-cli)
