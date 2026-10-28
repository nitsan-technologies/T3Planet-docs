---
title: "Example requests"
description: "Friendly AI agent requests for T3AA: missing alt text, drafts, decorative images, accessibility scans, Fix Hub suggestions, PageSpeed, summaries, and voice-over — including English and German examples."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AA"
  - "AI agent"
  - "Prompts"
  - "Accessibility"
sidebarTitle: "Example requests"
---

Talk to the AI agent the way you would ask a colleague. Copy an example below, change the names or file UIDs, and send it.

- Select the page first. *This page* means the page shown in the agent's context line.
- For every change, you get a preview first. Nothing is saved until you click **Apply**.

## Try these first

Three safe requests to get to know T3AA in the agent:

```text
Which images have no alt text?
```

```text
What accessibility issues does this page have?
```

```text
Summarize the content of this page.
```

The first two **only read**. The third returns a summary; nothing is saved until you approve a later write preview.

## Alt text

**"Which images still need alt text?"**

```text
Which images have no alt text?
```

```text
Welche Bilder haben keinen Alt-Text?
```

Decorative images are left out of this list.

**"Show drafts waiting for approval."**

```text
Which alt text drafts wait for approval?
```

```text
Welche Alt-Text-Entwürfe warten auf Freigabe?
```

The reply can show **Showing X of Y drafts**.

**"Generate drafts for a folder."** (asks before changing)

```text
Generate alt text for all images in this folder.
```

```text
Fill missing alt texts in user_upload/team.
```

```text
Queue alt text for "user_upload" folder, then show me the drafts. Do not approve them until I say so.
```

**"Approve drafts."** (asks before changing)

```text
Approve these alt text drafts.
```

```text
Approve all pending alt text drafts.
```

```text
Alt-Text-Entwürfe freigeben.
```

**"This image is only decoration."** (asks before changing)

```text
Mark this image as decorative.
```

```text
Mark file 141 as decorative.
```

```text
Mark this "/user_upload/hero.webp" image as decorative.
```

```text
Dieses Bild als dekorativ markieren.
```

**"Read or update metadata for one file."**

```text
What is the alt text of file 128?
```

```text
What is the public URL of file UID 21? Quote public_url from the metadata exactly.
```

```text
Generate alt text, title, and description for file 128.
```

```text
Write alt text for this "/user_upload/photo.webp" image and save it.
```

If a file already has image texts, the agent may ask whether to **Regenerate all**, **Fill empty fields only**, or **Keep current texts**.

<Note>
Asking to **delete** images without alt text only **lists** them. The agent does not delete files.
</Note>

## Accessibility scans and Fix Hub

**"Scan this page."** (asks before changing; uses scan quota)

```text
Scan this page for accessibility problems.
```

```text
Run a WCAG scan on this page.
```

```text
Run a WCAG scan on the homepage.
```

```text
Führe einen WCAG-Scan auf dieser Seite aus.
```

*"Scan this page…"* and *"Run a WCAG scan…"* open a **scan** preview (confirmation required). *"Check this page for accessibility problems"* / *"What accessibility issues…"* **only read** the last scan result.

**"Show the last scan."** (only reads)

```text
What accessibility issues does this page have?
```

```text
Show the last accessibility scan result.
```

```text
Welche Barrierefreiheitsprobleme hat diese Seite?
```

This only reads the last scan result. The agent offers a scan, and asks you to confirm it, only when you ask it to scan.

**"How do I fix them?"** (only reads; AI suggestions)

```text
How do I fix these accessibility issues?
```

```text
Suggest a fix for the missing alt text issues on this page.
```

## PageSpeed

```text
How fast is this page?
```

```text
Check the PageSpeed score of the homepage.
```

```text
Wie schnell lädt diese Seite?
```

<Note>
Google PageSpeed must be able to reach the public URL of the page. On local DDEV hosts such as `*.ddev.site`, the tool often fails with *Unable to resolve …*. Use a publicly reachable staging or production URL for real scores. The agent’s PageSpeed result is **not** saved to the T3AA Lighthouse report in the backend. See [Troubleshooting](/ExtNsT3AA/AskAiAgent/Troubleshooting/Index#pagespeed-unable-to-resolve).
</Note>

## Summaries, simplify, and voice-over

```text
Summarize the content of this page.
```

```text
Give me a short summary of content element 412.
```

```text
Create a simplified text version of this page in German.
```

```text
Fasse den Inhalt dieser Seite zusammen.
```

```text
Create a voice-over for this page.
```

```text
Erstelle ein Voice-over für diese Seite.
```

- **Summarize / simplify** use `t3aa_summarize_content` and **return text** (they do not write the page by themselves). A named page number is passed as `pageId`; a named language (for example German) is passed on. If the agent then offers to save the text on the page, you get a separate write preview — nothing is stored until **Apply**.
- **Voice-over** asks before changing and uses the editor’s default audio provider (OpenAI or ElevenLabs) and AI text-to-speech credits.

## Related

- [T3AA tools](/ExtNsT3AA/AskAiAgent/Tools/Index)
- [Your first accessibility request](/ExtNsT3AA/AskAiAgent/StepByStep/Index)
- [Feature Guide](/ExtNsT3AA/FeatureGuide/Index)
