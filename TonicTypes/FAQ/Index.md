---
title: "FAQ"
description: "Common Tonictypes questions — Core vs Pro, install, templates, export/import."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "Tonictypes"
  - "tonictypes"
  - "tonictypes_pro"
sidebarTitle: "FAQ"
---

## What is Tonictypes?

Custom record types in TYPO3 without writing a separate extension per type.

| Package | Role |
| --- | --- |
| **Tonictypes Pro** | Premium — advanced fields, toolbar, MCP, … |
| **Tonictypes** (Core) | Free required base — fields, datatypes, plugins, export/import |

Extension Manager titles: *Tonictypes* and *Tonictypes Pro: Enterprise Edition*.

## Core vs Pro?

- **Core** — Datatypes, fields, plugins, ViewHelpers, export/import, dashboard import widget. Free on [TER](https://extensions.typo3.org/extension/tonictypes).  
- **Pro** — Repeater and other advanced fields, toolbar, DocHeader, MCP, link handler, branding. [License](/en/latest/License/Index).

## How do I install?

1. License (Pro): [License docs](/en/latest/License/Index)  
1. Composer:

```bash
composer require k3n/tonictypes
composer require k3n/tonictypes_pro
```

1. Site Sets or static templates → clear caches  

Full steps: [Installation](/en/latest/TonicTypes/Installation/Index).

## Which TYPO3 / PHP?

TYPO3 12.4–14.9 · PHP 8.2–8.5 · packages **2.1.x**. Pro needs Core `^2.0`.

## Own templates?

Predefine under `plugin.tx_tonictypes.templates`, select in the plugin, or use `dv:template.render`.  
Namespace: **`dv:`** (not old `t:`). See [Templating](/en/latest/TonicTypes/GettingStarted/Templating/Index).

## Is export/import Pro-only?

No — Core from 2.1.0, module **System > Export / Import**. Steps: [Import / Export](/en/latest/TonicTypes/ExportImport/Index).

## “New records are disabled by default”?

Datatype → **Appearance** (`default_hidden`): new records start hidden until an editor enables them.

## More help

[Support](/en/latest/TonicTypes/Support/Index)
