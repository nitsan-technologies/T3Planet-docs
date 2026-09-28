---
title: "ViewHelpers"
description: "Reference for the Tonictypes Fluid ViewHelpers (dv:): render templates, load datatypes and records, build detail links, filter and group records."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "Tonictypes"
  - "tonictypes"
  - "tonictypes_pro"
sidebarTitle: "ViewHelpers"
---

All ViewHelpers use the **`dv:`** namespace. Core registers it automatically. Pro does not ship a separate ViewHelper package.

A ViewHelper is a Fluid tag that runs PHP code while the template is rendered. The Tonictypes ViewHelpers let a template do things that normally need a plugin setting: load a datatype or record by uid, filter or group a list of records, build links to detail pages, and render other Tonictypes templates. They work in every Fluid template of the site, not only in Tonictypes plugins.

## Namespace

`dv` maps to `K3n\Tonictypes\ViewHelpers`. Declaring it in the template is optional, but helps IDE autocompletion:

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

Use it to split templates into reusable parts — for example one "teaser" template used by a list, a slider and a search result — and to cache expensive parts of the output.

| Argument | Type | Default | Meaning |
| --- | --- | --- | --- |
| `template` | string | *required* | Identifier under `plugin.tx_tonictypes.templates`, or a file path |
| `arguments` | array | `[]` | Variables passed into the template |
| `variables` | array | `[]` | UIDs of additional Template Variables to inject |
| `pid` | int | — (treated as `0`) | Page ID used to read the plugin TypoScript settings, e.g. the default cache lifetime `plugin.tx_tonictypes.developer.cache_lifetime` |
| `cache` | bool | `false` | Cache the rendered output |
| `lifetime` | int | — | Cache lifetime in seconds (falls back to `developer.cache_lifetime`) |
| `cacheIdentifier` | string | — | Custom cache identifier |

```html
{dv:template.render(template:'movieMini',arguments:'{record:record}')}

<dv:template.render template="movieMini" arguments="{record:record}" variables="{0:12,1:35}" />
<dv:template.render template="fileadmin/templates/tonictypes/movies/mini.html" arguments="{record:record}" pid="12" />
```

## datatype.get

Fetches a Datatype by UID.

You need the datatype object for `dv:record.get` and `dv:filter.records` when the template is not rendered by a plugin that already provides `{datatype}`.

| Argument | Type | Default | Meaning |
| --- | --- | --- | --- |
| `uid` | int | *required* | Datatype UID |
| `onlyEnabled` | bool | `true` | Only enabled datatypes |

```html
<dv:datatype.get uid="1" onlyEnabled="0" />
```

## record.get

Fetches a record by UID.

Use it to show one specific record anywhere, for example a highlighted article in a sidebar template.

| Argument | Type | Default | Meaning |
| --- | --- | --- | --- |
| `uid` | int | *required* | Record UID |
| `datatype` | `K3n\Tonictypes\Domain\Model\Datatype` | *required* | Datatype of the record |
| `onlyEnabled` | bool | `true` | Only enabled records |

```html
<dv:record.get uid="1" datatype="{datatype}" onlyEnabled="0" />
```

## link.record / uri.record

Link or URL to a detail page (usually `{detailPid}` from the plugin).

`dv:link.record` renders an `<a>` tag, `dv:uri.record` returns only the URL (for example for a `data-href` attribute). Both add the record uid as `tx_tonictypes_dynamic[record]`, which the **Record Dynamic Detail** plugin on the target page reads — see [Frontend Plugins](/en/latest/TonicTypes/FrontendPlugins/Index#how-list-and-detail-work-together).

```html
<dv:link.record record="{record}" pageUid="{detailPid}">Link</dv:link.record>
<dv:uri.record record="{record}" pageUid="{detailPid}" />
```

## filter.records

Filter an already injected list (or load via `datatype`).

Use it when one plugin should show the same records in several filtered blocks (for example "open" and "closed" jobs), or when a template outside a plugin needs a filtered query. For a single filtered list, the plugin's own [Filters](/en/latest/TonicTypes/FrontendPlugins/DisplayRecordsPlugin/Index#filters) are simpler.

| Argument | Type | Default | Meaning |
| --- | --- | --- | --- |
| `records` | QueryResult | — | Records to filter |
| `datatype` | mixed | — | Datatype whose repository is queried (when `records` is empty) |
| `filters` | array | `[]` | Filter definition: `condition` (`AND` / `OR`) + `rules` |
| `variables` | array | `[]` | Extra variables for Fluid in filter values |
| `respectStoragePage` | bool | `true` | Restrict the query to storage pages; set `0` to search all pages |
| `storagePageIds` | array | `[]` | Storage page UIDs to query (used when not empty) |
| `ignoreEnableFields` | bool | `false` | Ignore enable fields (hidden / start / stop) when querying |

```html
<dv:filter.records records="{records}" filters="{condition:'AND',rules:{0:{field:'title',operator:'contains',value:'sales'}}}" respectStoragePage="1" storagePageIds="{0:77}" />
```

Operators include: `equal`, `not_equal`, `in`, `contains`, `begins_with`, `ends_with`, `is_empty`, `is_null`, and related variants.

## group.recordsByProperty

Groups records by a property.

Typical uses are an A–Z index, records grouped by category, or events grouped by month. The result is an array of `value => records`, which you loop over with two nested `f:for` tags.

| Argument | Type | Default | Meaning |
| --- | --- | --- | --- |
| `records` | Iterator | *required* | Records to group |
| `property` | string | *required* | Field name to group by |
| `returnOnlyGroups` | bool | `false` | Return only the group keys (values) instead of `key => records` |
| `multiple` | bool | `false` | Property holds multiple comma-separated values |

```html
{dv:group.recordsByProperty(records:records,property:'propertyName',returnOnlyGroups:0)}
```

## Also available

`dv:backend.*`, `dv:format.*`, string/array helpers, `dv:typo3.isVersion`.

The `dv:format.*` group includes `dv:format.flexFormToArray`, which turns the XML of a FlexForm field into an array (see [Tonictypes Pro → FlexForm Field](/en/latest/TonicTypes/Professional/Index#flexform-field-repeater)). `dv:typo3.isVersion` lets one template support several TYPO3 versions.

Predefined templates: [Templating](/en/latest/TonicTypes/GettingStarted/Templating/Index).
