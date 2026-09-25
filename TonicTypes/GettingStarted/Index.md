---
title: "Getting Started"
description: "Create your first Tonictypes record type — fields, datatype, records, then a frontend plugin."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "Tonictypes"
  - "tonictypes"
  - "tonictypes_pro"
sidebarTitle: "Getting Started"
---

Follow this order for the first custom record type.

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

## Minimum plugin settings

After you insert a plugin, set:

1. **Datatype**  
1. **Startingpoint** (the storage folder)  
1. **Template** (start with the debug template if unsure)

Then save and clear caches if the frontend is empty.

## Shortcuts

- Sample datatype: dashboard **Predefined Datatype Import** widget  
- Copy structures between sites: [Import / Export](/en/latest/TonicTypes/ExportImport/Index)  

<CardGroup cols={2}>
  <Card title="Creating a Field" icon="pencil" href="/en/latest/TonicTypes/GettingStarted/CreatingAField/Index" />
  <Card title="Creating a Datatype" icon="database" href="/en/latest/TonicTypes/GettingStarted/CreatingADatatype/Index" />
  <Card title="Creating a Template Variable" icon="braces" href="/en/latest/TonicTypes/GettingStarted/CreatingATemplateVariable/Index" />
  <Card title="Templating" icon="file-code-2" href="/en/latest/TonicTypes/GettingStarted/Templating/Index" />
</CardGroup>
