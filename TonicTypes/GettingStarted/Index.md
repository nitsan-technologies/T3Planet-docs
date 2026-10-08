---
title: "Getting Started"
description: "Build your first Tonictypes record type step by step: create fields, a datatype, its table and class, records, and a frontend Record List plugin."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "Tonictypes"
  - "tonictypes"
  - "tonictypes_pro"
sidebarTitle: "Getting Started"
---

Follow this order for the first custom record type. The steps build on each other: a datatype can only list fields that already exist, records can only be created once the datatype has a table, and a plugin can only show records that exist.

## Checklist

| Step | Where | Doc |
| --- | --- | --- |
| 1. Install | Composer / EM | [Installation](/en/latest/TonicTypes/Installation/Index) |
| 2. Create fields | Records on a **storage folder** | [Creating a Field](/en/latest/TonicTypes/GettingStarted/CreatingAField/Index) |
| 3. Create datatype | Same folder → Create Table / Class | [Creating a Datatype](/en/latest/TonicTypes/GettingStarted/CreatingADatatype/Index) |
| 4. Create records | Same folder → your datatype name | — |
| 5. (Optional) templates | Files / TypoScript | [Templating](/en/latest/TonicTypes/GettingStarted/Templating/Index) |
| 6. Place plugin | Page module → Tonictypes | [Frontend Plugins](/en/latest/TonicTypes/FrontendPlugins/Index) |

**Remember:** configuration and records → **Records** module. Plugins → **Page** module.

## Worked example: a "Demo Article" record type

This example builds a small article type with a title, a subtitle and a description, and lists the articles on a page. The screenshots in this documentation were taken from exactly this setup.

1. **Create a storage folder.** In the page tree add a page of type *Folder*, for example "Tonictypes Demo". Everything below (fields, datatype, records) goes into this folder.
1. **Create three fields.** In the Records module on that folder: **Create new record** → **Field**.
   - Type *Input Field*, Frontend Label `Title`
   - Type *Input Field*, Frontend Label `Subtitle`
   - Type *Textarea*, Frontend Label `Description`

   The Fluid variable name is filled in from the label (`title`, `subtitle`, `description`). It also becomes the database column name.
1. **Create the datatype.** **Create new record** → **Datatype**, Name `Demo Article`. On the **Fields** tab move the three fields to the selected side in the order they should appear in the form. Save.
1. **Generate table and class.** Click **Create Table**, then **Create Class** (after later changes the buttons read **Update Table** / **Update Class**). Tonictypes now creates the table `tx_tonictypes_domain_model_record_demo_article` and the PHP class `Demo/Article.php`. Clear all caches.
1. **Create records.** Still on the folder: **Create new record** → **Demo Article**. Add "First Demo Article" and "Second Demo Article".
1. **Show them on a page.** Open a normal page in the Page module → **New content element** → **Tonictypes** → **Record List**. Set **Datatype** = Demo Article, **Startingpoint** = the storage folder, template = **Debug Template**. Save and view the page.

The debug template prints every record with all its properties, so you can see the variable names before you write a real template. Continue with [Templating](/en/latest/TonicTypes/GettingStarted/Templating/Index) to replace it with your own markup.

## Minimum plugin settings

After you insert a plugin, set:

1. **Datatype** — tells the plugin which record class and table to query  
1. **Startingpoint** (the storage folder) — tells it where the records are stored  
1. **Template** (start with the debug template if unsure) — tells it how to render them  

Then save and clear caches if the frontend is empty.

## Shortcuts

- Sample datatype: dashboard **Predefined Datatype Import** widget ([details](/en/latest/TonicTypes/ExportImport/Index#dashboard-widget-predefined-datatype-import)) — imports a bundled, ready-made datatype into a storage folder you choose, useful to explore a working setup  
- Copy structures between sites: [Import / Export](/en/latest/TonicTypes/ExportImport/Index)  

<CardGroup cols={2}>
  <Card title="Creating a Field" icon="pencil" href="/en/latest/TonicTypes/GettingStarted/CreatingAField/Index" />
  <Card title="Creating a Datatype" icon="database" href="/en/latest/TonicTypes/GettingStarted/CreatingADatatype/Index" />
  <Card title="Creating a Template Variable" icon="braces" href="/en/latest/TonicTypes/GettingStarted/CreatingATemplateVariable/Index" />
  <Card title="Templating" icon="file-code-2" href="/en/latest/TonicTypes/GettingStarted/Templating/Index" />
</CardGroup>
