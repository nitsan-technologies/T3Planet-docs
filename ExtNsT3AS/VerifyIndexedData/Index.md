---
title: "Verifying Indexed Data Content in TYPO3 AI Search"
description: "To ensure that the data from your selected search engines Solr, keSearch, IndexedSearch is properly fetched, stored, and trained in TYPO3, follow these steps:"
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AS"
  - "Verifying Indexed Data Content in TYPO3 AI Search"
sidebarTitle: "VerifyIndexedData"
---

Want to check that AI Search really learned your content from Solr, ke_search or Indexed Search? Here is how.

## Check in the backend

1. Go to **AI Universe → AI Chatbot/Search → Training Center**.
2. Filter by your data source.
3. Look at the status:
   - **Completed** – learned, AI Search can use it.
   - **Pending** – waiting for the next training run.
   - **Failed** – something went wrong. Select it and click **Re-queue** to try again.

See [Training Center](/en/latest/ExtNsT3AS/Configuration/TrainingCenter/Index).

<Note>
If you use a custom AI model (custom LLM) that stores the data outside TYPO3, you won't see the items here.
</Note>

<Accordion title="For developers: check in the database">
You can also check the training status directly in the database. Every collected item is one row with a status: **Pending**, **Completed** or **Failed**.

```sql
SELECT uid, type, path, status, error_message
FROM tx_nst3cs_domain_model_datasource_queue
WHERE status IN ('Pending', 'Failed');
```
</Accordion>

{/* To ensure that the data from your selected search engines (Solr, keSearch, IndexedSearch) is properly fetched, stored, and trained in TYPO3, follow these steps:

1. **Verify Column Values** In the table tx_nst3as_domain_model_indexed_data, check the following columns for each search engine type:
  - **`type`**: solr, keSearch, or indexedSearch
  - **`status`**: trained
  - **`path`**: The corresponding data URL
2. **Check Trained Data** Replace **`solr`** with the type of search engine you want to check (e.g., **`solr`**, **`kesearch`**, or **`indexedsearch`**): SELECT *
FROM `tx_nst3as_domain_model_indexed_data`
WHERE `type` = 'solr'
  AND `status` = 'trained';
3. **Check Untrained Data** Replace **`solr`** with your search engine type as needed: SELECT *
FROM `tx_nst3as_domain_model_indexed_data`
WHERE `type` = 'solr'
  AND `status` = 'Untrained'
  AND `path` != '';

<Note>
This is not use when you use the CustomLLM because we didn’t save the any data inside the TYPO3 Database.
</Note>

```sql
SELECT *
FROM `tx_nst3as_domain_model_indexed_data`
WHERE `type` = 'solr'
  AND `status` = 'trained';
```

```sql
SELECT *
FROM `tx_nst3as_domain_model_indexed_data`
WHERE `type` = 'solr'
  AND `status` = 'Untrained'
  AND `path` != '';
``` */}

{/* Detailed developer notes (moved here on 2026-10-08 to keep the page short; not shown on the website):

<Accordion title="For developers: check in the database">

The collected content is stored in `tx_nst3cs_domain_model_datasource_queue` (columns `type`, `status`, `path`). The AI data (embeddings) is in `tx_nst3cs_domain_model_datasource_embedd`. Source types: `solr`, `ke_search`, `index_search`, `sitemap`, `pdf`, `typo3_pages`, `web_pages`, `qa`, `text`.

Trained items (replace `solr` with `ke_search` or `index_search` if needed):

```sql
SELECT uid, type, path, status
FROM tx_nst3cs_domain_model_datasource_queue
WHERE type = 'solr'
  AND status = 'Completed';
```

Items not trained yet or failed:

```sql
SELECT uid, type, path, status, error_message
FROM tx_nst3cs_domain_model_datasource_queue
WHERE type = 'solr'
  AND status IN ('Pending', 'Failed');
```

</Accordion>
*/}
