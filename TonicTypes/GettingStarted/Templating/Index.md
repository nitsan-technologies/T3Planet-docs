---
title: "Templating"
description: "Fluid templates for Tonictypes — dv namespace, variables, predefined templates."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "Tonictypes"
  - "tonictypes"
  - "tonictypes_pro"
sidebarTitle: "Templating"
---

Tonictypes uses normal TYPO3 Fluid.

## Namespace

Use **`dv:`** (`K3n\Tonictypes\ViewHelpers`). Registered automatically with Core.

```html
<html
    lang="en"
    data-namespace-typo3-fluid="true"
    xmlns:f="http://typo3.org/ns/TYPO3/CMS/Fluid/ViewHelpers"
    xmlns:dv="http://typo3.org/ns/K3n/Tonictypes/ViewHelpers">
</html>
```

## Variables

| Context | Default variable |
| --- | --- |
| List | `{records}` |
| Detail | `{record}` |
| One field | `{record.fieldname}` |

Debug with `<f:debug>{_all}</f:debug>` or `<f:debug>{record.fieldname}</f:debug>`.

## Predefine templates in TypoScript

```typoscript
plugin.tx_tonictypes.templates {
    myTemplateIdentifier {
      group = General
      icon = EXT:tonictypes/Resources/Public/Icons/Datatype/animal-dog.png
      name = My Test Template
      file = EXT:yourtemplateext/Resources/Private/Templates/Tonictypes/TemplateOne.html
    }
}
```

![Template selector](Images/template_selection.webp)

*Debug · custom path · inline Fluid · TypoScript templates*

```html
<dv:template.render template="myTemplateIdentifier" arguments="{record:record}" />
```

More ViewHelpers: [ViewHelpers](/en/latest/TonicTypes/ViewHelpers/Index).

## Next

[Frontend Plugins](/en/latest/TonicTypes/FrontendPlugins/Index)
