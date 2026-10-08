---
title: "For developers"
description: "Developer reference for AI Chatbot: chatbot ID, events, page types and upgrade wizard."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AC"
  - "Developers"
  - "Events"
sidebarTitle: "For developers"
---

Developers can change what AI Chatbot sends to the AI with TYPO3 events. Most websites don't need anything on this page.

- **Listen to events to change the data** – for example the chat history before it goes to the AI (`BeforeChatbotSendEvent`), the answer to small talk like "hi" (`BeforeCasualIntentEvent`), or the content before it is trained (`BeforeDatasourceEmbeddingEvent`). Register a normal [TYPO3 event listener](https://docs.typo3.org/m/typo3/reference-coreapi/main/en-us/ApiOverview/Events/EventDispatcher/Index.html).
- **Keep the chatbot ID in the site configuration** – when you save, AI Chatbot writes `chatbotId` into your site's `config.yaml`. Don't delete it when you edit the file by hand.
- **Don't reuse these page types** for your own pages: `1740479454`, `1748328939`, `1740978594`, `1741166457`, `1741166458`, `1764663345`.
- **Run the upgrade wizard after an update** – **Admin Tools → Upgrade → Upgrade Wizard** (TYPO3 v14: **System → Upgrade**).

{/* Detailed developer notes (moved here on 2026-10-08 to keep the page short; not shown on the website):

<Accordion title="Developer reference: chatbot ID, events, page types, upgrade wizard">

**Chatbot ID in the site configuration** – when you save, AI Chatbot writes the ID of the chatbot (`chatbotId`, per language) into the `config.yaml` file of your site. Do not remove it if you edit this file by hand.

**Events** – register a PSR-14 listener as described in the TYPO3 documentation.

| Event | When it runs | What you can change |
|---|---|---|
| `NITSAN\NsT3Ac\Event\BeforeChatbotSendEvent` | Before a chat request is sent to the AI | The chat history |
| `NITSAN\NsT3Ac\Event\BeforeCasualIntentEvent` | Before a small-talk question ("hi", "thanks") is answered | The visitor question and the chatbot interests |
| `NITSAN\NsT3Ac\Event\BeforeChatbotTrainingEvent` | Before content is sent to a custom LLM for training | The training data |
| `NITSAN\NsT3Cs\Event\BeforeDatasourceEmbeddingEvent` | Before a piece of content is turned into embeddings | The text |
| `NITSAN\NsT3Cs\Event\BeforeCustomLlmIngestPayloadEvent` | Before content is sent to a custom LLM | The data sent |

**Page types used by AI Chatbot** – do not use these numbers for your own page types:

`1740479454`, `1748328939`, `1740978594`, `1741166457`, `1741166458`, `1764663345`

**Upgrade wizard** – run in **Admin Tools → Upgrade → Upgrade Wizard** (on TYPO3 v14: **System → Upgrade → Upgrade Wizard**) after an update:

- EXT:ns_t3ac: Add chatbot message response time column

</Accordion>
*/}
