---
title: "ViewHelpers"
description: "Tonictypes Fluid ViewHelpers (dv:) — template, datatype, record, link, filter, group."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "Tonictypes"
  - "tonictypes"
  - "tonictypes_pro"
sidebarTitle: "ViewHelpers"
---

All ViewHelpers use the **`dv:`** namespace. Core registers it automatically. Pro does not ship a separate ViewHelper package.

```html
<html
    lang="en"
    data-namespace-typo3-fluid="true"
    xmlns:f="http://typo3.org/ns/TYPO3/CMS/Fluid/ViewHelpers"
    xmlns:dv="http://typo3.org/ns/K3n/Tonictypes/ViewHelpers">
</html>
```

## template.render

Renders a TypoScript template identifier or a file path.

| Argument | Meaning |
| --- | --- |
| `template` | Identifier or file path |
| `arguments` | Variables passed in |
| `variables` | Extra Template Variable UIDs |
| `cache` / `lifetime` / `cacheIdentifier` | Optional cache |

```html
{dv:template.render(template:'movieMini',arguments:'{record:record}')}

<dv:template.render template="movieMini" arguments="{record:record}" variables="{0:12,1:35}" />
<dv:template.render template="fileadmin/templates/tonictypes/movies/mini.html" arguments="{record:record}" />
```

## datatype.get

Fetches a Datatype by UID (`uid`, `onlyEnabled`).

```html
<dv:datatype.get uid="1" onlyEnabled="0" />
```

## record.get

Fetches a record by UID (`uid`, `datatype`, `onlyEnabled`).

```html
<dv:record.get uid="1" datatype="{datatype}" onlyEnabled="0" />
```

## link.record / uri.record

Link or URL to a detail page (usually `{detailPid}` from the plugin).

```html
<dv:link.record record="{record}" pageUid="{detailPid}">Link</dv:link.record>
<dv:uri.record record="{record}" pageUid="{detailPid}" />
```

## filter.records

Filter an already injected list (`condition`, `filters` / `rules`).

```html
<dv:filter.records records="{records}" filters="{condition:'AND',rules:{0:{field:'title',operator:'contains',value:'sales'}}}" />
```

Operators include: `equal`, `not_equal`, `in`, `contains`, `begins_with`, `ends_with`, `is_empty`, `is_null`, and related variants.

## group.recordsByProperty

Groups records by a property.

```html
{dv:group.recordsByProperty(records:records,property:'propertyName')}
```

## Also available

`dv:backend.*`, `dv:format.*`, string/array helpers, `dv:typo3.isVersion`.

Predefined templates: [Templating](/en/latest/TonicTypes/GettingStarted/Templating/Index).
