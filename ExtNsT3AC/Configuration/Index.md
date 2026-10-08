---
title: "Configuration"
description: "T3AC uses T3AF for provider setup, model selection, shared prompts, and core AI services. Complete the T3AF setup first, then return to T3AC for chatbot-specific configuration."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AC"
  - "Configuration"
sidebarTitle: "Configuration"
---

This page shows you how to set up AI Chatbot after installation: check the AI settings, design the chatbot and put it on your website.

With AI Chatbot you control how the chatbot answers, what it learns and where it is shown – on your website or on other websites.

**The basic idea in 4 steps**

1. Connect an AI service in **AI Foundation** (done during installation).
2. Add your content in **Data Source** and let the chatbot learn it (see [Data Source](/en/latest/ExtNsT3AC/FeatureGuide/DataSource/Index)).
3. Set up the chatbot on the **Chatbot** tab (see [Chatbot Features](/en/latest/ExtNsT3AC/FeatureGuide/Chatbot/Index#quick-setup)).
4. Check the chatbot on your website.

**Follow the pages in this order.** Pages 1–5 are the basic setup. The others are optional or for later. Dashboard, Data Source, Training Center, Chatbot, Usage Analytics and AI Logs are described on the [Features](/en/latest/ExtNsT3AC/FeatureGuide/Index) pages.

<CardGroup cols={2}>
  <Card title="1. AI Features & provider" icon="sparkles" href="/en/latest/ExtNsT3AC/Configuration/AIFeatures/Index">
    Shared settings in AI Foundation and the AI service the chatbot uses.
  </Card>
  <Card title="2. Dashboard" icon="layout-dashboard" href="/en/latest/ExtNsT3AC/FeatureGuide/Dashboard/Index">
    Check at a glance if everything is set up and working.
  </Card>
  <Card title="3. Data Source" icon="database" href="/en/latest/ExtNsT3AC/FeatureGuide/DataSource/Index">
    Add pages, PDFs, Q&A and text. Use source groups per page.
  </Card>
  <Card title="4. Training Center & Scheduler" icon="graduation-cap" href="/en/latest/ExtNsT3AC/FeatureGuide/TrainingCenter/Index">
    Watch the training. The Scheduler runs it automatically.
  </Card>
  <Card title="5. Chatbot: Configuration, Customize, General" icon="message-circle" href="/en/latest/ExtNsT3AC/FeatureGuide/Chatbot/Index">
    Switch the chatbot on, design it, choose the pages and the widget position.
  </Card>
  <Card title="6. Quick replies" icon="reply" href="/en/latest/ExtNsT3AC/FeatureGuide/Chatbot/Index#quick-replies">
    Up to 5 buttons with prepared answers under the welcome message.
  </Card>
  <Card title="7. Hide the chatbot on a page" icon="eye-off" href="/en/latest/ExtNsT3AC/Configuration/DisableChatbotOnPage/Index">
    A switch in the page properties.
  </Card>
  <Card title="8. External Embed" icon="code" href="/en/latest/ExtNsT3AC/Configuration/ExternalEmbed/Index">
    Show the chatbot on another website (+ .htaccess / CORS).
  </Card>
  <Card title="9. Usage Analytics" icon="chart-column" href="/en/latest/ExtNsT3AC/FeatureGuide/UsageAnalytics/Index">
    Visitor conversations and their feedback.
  </Card>
  <Card title="10. AI Usage & AI Logs" icon="scroll-text" href="/en/latest/ExtNsT3AC/FeatureGuide/AILogs/Index">
    How much AI was used, and error messages.
  </Card>
  <Card title="11. Permissions" icon="shield" href="/en/latest/ExtNsT3AC/Configuration/Permissions/Index">
    Who may see or change the chatbot and the chats.
  </Card>
  <Card title="12. Providers & MCP Tools" icon="plug" href="/en/latest/ExtNsT3AC/Configuration/MCPTools/Index">
    The AI provider, and MCP for AI assistants.
  </Card>
  <Card title="13. Upgrading? Where your old settings moved" icon="map" href="/en/latest/ExtNsT3AC/Configuration/WhereToFindIt/Index">
    Only if you upgrade from an older version: where the old site settings are now.
  </Card>
  <Card title="14. For developers" icon="terminal" href="/en/latest/ExtNsT3AC/Configuration/ForDevelopers/Index">
    Chatbot ID, events, page types, upgrade wizard.
  </Card>
</CardGroup>

{/* Original text before the 8 Oct 2026 simplification (kept for reference):

T3AC uses T3AF for provider setup, model selection, shared prompts, and core AI services.
Complete the T3AF setup first, then return to T3AC for chatbot-specific configuration.

Helpful T3AF references:

- [T3AF Configuration](/en/latest/ExtNsT3AF/Configuration/Index)
- [AI Providers](/en/latest/ExtNsT3AF/Configuration/AIProviders/Index)
- [AI Features](/en/latest/ExtNsT3AF/Configuration/AIFeatures/Index)
- [AI Prompts](/en/latest/ExtNsT3AF/Configuration/AIPrompts/Index)

T3AC focuses on chatbot-related AI workflows built on top of the shared T3AF setup.
Use these features when you want to control how the chatbot answers questions, how data is trained, and how the chatbot is shown on your site or external websites.

Key T3AC capabilities include:

- Chatbot configuration and behavior control
- Training and data-source-based answer generation
- Dashboard, logs, and analytics for chatbot activity
- External embed support for approved domains

For shared model routing and central AI behavior, see [T3AF AI Features](/en/latest/ExtNsT3AF/Configuration/AIFeatures/Index).

- [AI Providers](/en/latest/ExtNsT3AF/Configuration/AIProviders/Index)
- [MCP Server](/en/latest/ExtNsT3AF/Integrations/MCPServer/Index)
- [MCP Tools](/en/latest/ExtNsT3AF/Integrations/MCPTools/Index)
*/}
