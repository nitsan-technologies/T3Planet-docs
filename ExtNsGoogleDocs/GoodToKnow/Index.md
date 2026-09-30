---
title: "Good to know"
description: "Important points about imports with Google Docs (EXT:ns_googledocs): language, undo, overriding content, element order and per-editor settings."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "ns_GoogleDocs"
  - "Good to know"
sidebarTitle: "Good to know"
---

- Imports create content in the **default language** only.
- Imported records are written directly and are **not listed in the record history**, so an import cannot be undone with "Undo". Use **Save as Draft** in [Global Settings](/ExtNsGoogleDocs/NSGoogleDocsModule/Index#record-settings) to review imported content before it goes live.
- **Override existing column content** deletes the existing elements of the column permanently. Make a backup first if you are not sure.
- New elements are always added **after** the existing content of the column.
- Each editor has their own Google connection and settings.
