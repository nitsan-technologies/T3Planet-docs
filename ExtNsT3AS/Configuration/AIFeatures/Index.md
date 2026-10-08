---
title: "AI Features & AI Prompts"
description: "AI Foundation settings for AI Search: the AI Chatbot/Search cards in AI Features and the AI Prompts that set the tone of answers."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AS"
  - "AI Features"
  - "AI Prompts"
sidebarTitle: "AI Features & Prompts"
---

A few general settings (for example limits and training options) are in AI Foundation. You usually only need them if you want to change the defaults.

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmraj97pg0ryeqmhxt1yypwta?utm_source=link" loading="lazy" title="AI Features Demo" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

1. Go to **AI Universe → AI Foundation → AI Features**.
2. Find the cards with the label **AI Chatbot/Search**:
   - **Provider Overrides** – use a different AI provider just for search and chat.
   - **Rate Limiting** – stop one visitor from sending too many questions.
   - **Training** – how your content is prepared for the AI.
   - **Solr configurations** – only if you use Solr (see [Solr settings](/en/latest/ExtNsT3AS/Configuration/SearchExtensions/Index#solr-settings)).
3. Click **Configure** on a card.
4. Change the settings.
5. Click **Save**.

![AI Features filtered to the AI Chatbot/Search cards: Provider Overrides, Rate Limiting, Training and Solr configurations](../images/ai-features-chatbot-search.webp)

<Note>
These cards are shared by AI Search and AI Chatbot. A change here affects both.
</Note>

{/* SUPADEMO NEEDED: AI Features cards for AI Chatbot/Search */}

More about these cards: [AI Features](/en/latest/ExtNsT3AF/Configuration/AIFeatures/Index).

{/* 1. Go to the **TYPO3 backend**.
2. Open **AI Foundation** → **AI Features**.
3. Open the **T3AS** (`ns_t3as`) feature card and configure the shared settings.
4. Click **Save**.
5. Return to **T3AS** to continue with source, training, and search-specific settings. */}

<a id="ai-prompts"></a>

## AI Prompts

A **prompt** is the instruction the AI gets before it writes an answer. With AI Prompts you can change the tone and style of all answers in one place.

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmrbog9to0dl9qmo5dmb8bj0m?utm_source=link" loading="lazy" title="T3AS AI Prompts Demo" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

- Keep the instructions short, for example "Answer in simple words, in 3 sentences".
- Test changes with real questions from your visitors.
- Prompts are managed in [AI Foundation → AI Prompts](/en/latest/ExtNsT3AF/Configuration/AIPrompts/Index).

{/* - Review [AI Foundation AI Prompts ](/en/latest/ExtNsT3AF/AIPrompts/Index) when you want shared prompt behavior across multiple AI Universe extensions. */}

{/* ## 9. AI Prompts */}

{/* - [AI Prompts ](/en/latest/ExtNsT3AF/AIPrompts/Index) */}
