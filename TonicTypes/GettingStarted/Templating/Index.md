---
title: "Templating"
description: "Write Fluid templates for Tonictypes plugins: the dv namespace, available variables like records and record, a list example, and TypoScript templates."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "Tonictypes"
  - "tonictypes"
  - "tonictypes_pro"
sidebarTitle: "Templating"
---

Tonictypes uses normal TYPO3 Fluid.

Every Tonictypes plugin loads the records, prepares a set of variables and hands them to a Fluid template that you choose in the plugin. You can start with the built-in **Debug Template**, which prints all available variables, and then switch to your own template file, inline Fluid in the plugin, or a template registered in TypoScript. The choices themselves are described in [Plugin configuration → Templates](/en/latest/TonicTypes/FrontendPlugins/DisplayRecordsPlugin/Index#templates).

## Namespace

Use **`dv:`** (`K3n\Tonictypes\ViewHelpers`). Registered automatically with Core. For the optional `xmlns` snippet (IDE autocompletion) see [ViewHelpers → Namespace](/en/latest/TonicTypes/ViewHelpers/Index#namespace).

## Variables

| Context | Default variable |
| --- | --- |
| List | `{records}` — all records the plugin found, ready for `f:for` |
| Detail | `{record}` — the one record of a Detail or Dynamic Detail plugin |
| One field | `{record.fieldname}` — the value of a field, by its variable name |

The plugins also provide:

| Variable | Contains |
| --- | --- |
| `{datatype}` | The selected datatype object (name, table, fields) |
| `{detailPid}` | The page set as **Page for Detail View**, for building detail links |
| `{overallCount}` | Number of records found (List) |
| `{settings}` | All plugin settings |
| `{cObj}` | Data of the current content element (e.g. its uid or header) |
| `{p_paginator}`, `{p_paging}`, `{p_pages}` | Pagination objects, only when **Enable Pagination** is on |

Injected [Template Variables](/en/latest/TonicTypes/GettingStarted/CreatingATemplateVariable/Index) appear under their own names.

Debug with `<f:debug>{_all}</f:debug>` or `<f:debug>{record.fieldname}</f:debug>`.

### Example: list template for Demo Articles

```html
<f:for each="{records}" as="record">
  <article>
    <h2>
      <dv:link.record record="{record}" pageUid="{detailPid}">{record.title}</dv:link.record>
    </h2>
    <f:if condition="{record.subtitle}"><p class="lead">{record.subtitle}</p></f:if>
    <p>{record.description}</p>
  </article>
</f:for>
```

`title`, `subtitle` and `description` are the variable names of the fields from the [Getting Started example](/en/latest/TonicTypes/GettingStarted/Index). The link points to the detail page, where a **Record Dynamic Detail** plugin renders the same record as `{record}`.

## Predefine templates in TypoScript

Register templates under `plugin.tx_tonictypes.templates` — TypoScript example: [Installation → Predefined templates](/en/latest/TonicTypes/Installation/Index#predefined-templates). They then appear in the plugin under **Predefined Templates**.

This is the recommended way for sites with several plugins: editors pick a named template from a list instead of typing file paths, and the integrator can change the file in one place. The `group`, `name` and `icon` settings only control how the template is presented in the selector.

![Template selector](Images/template_selection.webp)

*Debug · custom path · inline Fluid · TypoScript templates*

The same identifier can be rendered anywhere in Fluid, for example to reuse a "teaser" template inside another template:

```html
<dv:template.render template="myTemplateIdentifier" arguments="{record:record}" />
```

More ViewHelpers: [ViewHelpers](/en/latest/TonicTypes/ViewHelpers/Index).

## Next

[Frontend Plugins](/en/latest/TonicTypes/FrontendPlugins/Index)
