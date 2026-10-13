---
title: "Extend Records Translation"
description: "Configure TCA l10n_mode prefixLangTitle so ns_t3ai can translate specific record fields."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AI"
  - "Translation"
sidebarTitle: "Extend Records Translation"
---

T3AI translates only the record fields whose `l10n_mode` is `prefixLangTitle`. It detects them with a DataHandler hook.

To make T3AI translate fields of your own table, set `l10n_mode` in a TCA override, one line per field:

`<extension_key>/Configuration/TCA/Overrides/<table_name>.php`

```php
$GLOBALS['TCA']['<table_name>']['columns']['<field_name>']['l10n_mode'] = 'prefixLangTitle';
$GLOBALS['TCA']['<table_name>']['columns']['<other_field_name>']['l10n_mode'] = 'prefixLangTitle';
```

**Related:** [AI Translation card](/en/latest/ExtNsT3AI/Configuration/AIFeatures/Index#ai-translation) · [Records Translation](/en/latest/ExtNsT3AI/Translation/RecordsTranslation/Index)
