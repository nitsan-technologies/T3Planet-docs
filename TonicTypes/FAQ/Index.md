---
title: "FAQ"
description: "Answers to common Tonictypes questions: Core vs Pro, installation, empty frontend, missing fields, generated classes, templates and export/import."
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
| **Tonictypes Pro** (`k3n/tonictypes_pro`) | Premium — advanced fields, toolbar, MCP, … (needs Core, `ns_license`, and **AI Foundation** / `ns_t3af`) |
| **Tonictypes** (Core) | Free required base — fields, datatypes, plugins, export/import |

Extension Manager titles: *Tonictypes - Rapid TCA & Advanced Plugins* and *Tonictypes Pro: Enterprise Edition – Full Stack*.

## Core vs Pro?

- **Core** — Datatypes, fields, plugins, ViewHelpers, export/import, dashboard import widget. Free on [TER](https://extensions.typo3.org/extension/tonictypes).  
- **Pro** — FlexForm and other advanced fields, toolbar, DocHeader, MCP, link handler, branding. Needs Core, `ns_license`, and **AI Foundation** (`ns_t3af`). [License](/en/latest/License/Index).

## How do I install?

1. License (Pro): [License docs](/en/latest/License/Index)  
1. Composer packages (`k3n/tonictypes`, `nitsan/ns-t3af`, `k3n/tonictypes_pro`): [Installation → Composer](/en/latest/TonicTypes/Installation/Index#composer)  
1. Site Sets (`config.yaml`) or static templates, then clear caches: [Installation → Activate configuration](/en/latest/TonicTypes/Installation/Index#3-activate-configuration)  

Pro’s `composer.json` requires **AI Foundation** `nitsan/ns-t3af` in addition to Core and `nitsan/ns-license`.

## Which TYPO3 / PHP?

TYPO3 12.4–14.9 · PHP 8.2–8.5. Pro needs Core, `nitsan/ns-license`, and `nitsan/ns-t3af`.

## Own templates?

See [Templating](/en/latest/TonicTypes/GettingStarted/Templating/Index). Namespace: **`dv:`** (not old `t:`).

## Is export/import Pro-only?

No — Core from 2.1.0, module **System > Export / Import**. Steps: [Import / Export](/en/latest/TonicTypes/ExportImport/Index).

## “New records are disabled by default”?

Datatype → **Appearance** (`default_hidden`): new records start hidden until an editor enables them. Use it when new records need a review before they appear on the website.

## Why is my frontend empty?

Check, in this order: the plugin has a **Datatype** and a **Startingpoint**; the Startingpoint is the folder that actually contains the records (or **Recursive** is set); the records are not hidden or outside their start/stop time; a template is selected. Then clear all caches. The **Debug Template** shows what the plugin found. Details: [Frontend Plugins → Minimum settings](/en/latest/TonicTypes/FrontendPlugins/Index#minimum-settings).

## I added a field, but the record form does not show it

After changing the fields of a datatype, click **Update Table** and **Update Class** on the datatype and clear all caches — the generated TCA is cached. If the field is not even offered on the datatype's **Fields** tab, it is stored on another page or lacks a Frontend Label, variable name or Field Value. See [Creating a Datatype](/en/latest/TonicTypes/GettingStarted/CreatingADatatype/Index#what-create-table-and-create-class-do).

## Where are the generated table and classes?

The table is `tx_tonictypes_domain_model_record_<name>` in the TYPO3 database. The PHP model and repository are written into the `tonictypes` extension under `Classes/Domain/Model/Record/` and `Classes/Domain/Repository/Record/`. On Composer sites, make sure this folder is writable for the web server user.

## More help

[Support](/en/latest/TonicTypes/Support/Index)
