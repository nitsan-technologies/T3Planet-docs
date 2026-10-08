---
title: "External Embed"
description: "Show the chatbot on another website: copy the embed code, allow the domains and add the Apache (.htaccess) configuration."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AC"
  - "External Embed"
  - "CORS"
sidebarTitle: "External Embed"
---

{/* ## Step 5: External Chatbot Configuration

To configure chatbot embedding for external domains:

1. Go to the **T3AC** module.
2. Navigate to **Chatbot > External Embed**.

Available options:

- **Custom CSS**
Use your own styles to customize the chatbot appearance.
- **Allowed Domains for Embedding**
Specify the domains where the chatbot can be embedded, e.g. `example.com`, `trusted-domain.com`.
- **Allow Any Domain**
Enable this option to permit embedding on any domain without restrictions. */}

Want the chatbot on a website that doesn't run on this TYPO3, for example your shop? Use **External Embed**.

1. Save the chatbot on the **Configuration** tab first. Until then, External Embed shows: "Save the chatbot (Configuration tab) to generate the embed code with your site URL and chatbot identifier."
2. Go to **Chatbot → External Embed**.
3. Under **Add AI Chatbot to Any Website in Seconds**, click **Copy**.
4. Give the code to the person who manages the other website. They paste it just before the closing `</body>` tag.
5. Under **External Embedding Settings**, choose which websites may use the chatbot:
   - **Allow Any Domain** – every website.
   - **Allowed Domains** – only the websites you list, separated by commas, for example `shop.example.com, www.partner.com`.
   - **External CSS Path** – optional: your own design file, for example `/fileadmin/user_upload/chatbot.css`.
6. Click **Save Configuration**.
7. Ask your developer to allow the other website on your server (see below).

![Chatbot External Embed tab with the embed code, External Embedding Settings and Apache Configuration](../images/chatbot-external-embed.webp)

<Warning>
Only use **Allow Any Domain** if every website may use your chatbot. Each chat uses your AI service and may cost money.
</Warning>

<Accordion title="For developers: allow the other website on the server (Apache)">

Browsers block content from another domain unless the server allows it (CORS – cross-origin resource sharing).

1. Copy the code under **Apache Configuration** on the External Embed tab.
2. Paste it into the `.htaccess` file of the TYPO3 website where the chatbot runs.
3. Save the file and test the chatbot on the other website.

</Accordion>

{/* SUPADEMO NEEDED: Chatbot External Embed + .htaccess */}

**Related:** [External Embed in the Chatbot features](/en/latest/ExtNsT3AC/FeatureGuide/Chatbot/Index#external-embed) · [AI Search External Embed](/en/latest/ExtNsT3AS/Configuration/ExternalEmbed/Index) (works the same way)
