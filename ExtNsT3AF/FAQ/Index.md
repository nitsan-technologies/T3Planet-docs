---
title: "FAQ"
description: "FAQ for EXT:ns_t3af (T3AF)."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AF"
  - "ns_t3af"
sidebarTitle: "FAQ"
---

Short answers to common questions about AI Foundation (T3AF, `ns_t3af`). For general questions about T3Planet products and support, see the [general FAQ](/en/latest/FAQ/Index).

## General

### What is T3AF?

The shared AI foundation for T3Planet TYPO3 extensions: AI providers, MCP, AI Credits, logs and governance. It also runs on its own. See [What Does It Do?](/en/latest/ExtNsT3AF/WhatDoesItDo/Index).

### Is T3AF free? Is there a premium version?

T3AF is free and open source, with no license key and no registration. There is one version. Run `composer require nitsan/ns-t3af` or install it from the TYPO3 Extension Repository. See [Installation](/en/latest/ExtNsT3AF/Installation/Index).

### Does it work on the frontend?

It has no frontend plugin of its own. It powers backend AI features and MCP agents. Visitors see AI through child extensions such as the AI Assistant (T3AI) or the AI Chatbot (T3AC).

### Which TYPO3 and PHP versions are supported?

TYPO3 12.4, 13.4 and 14.x with PHP 8.2 or higher. See [System Requirements](/en/latest/ExtNsT3AF/SystemRequirements/Index).

## Providers

### Do I need AI Credits?

No. Your own API keys are the default. [AI Credits](/en/latest/ExtNsT3AF/T3Planet-Credit-System/Index) is an optional add-on for teams that do not want to manage their own AI vendor accounts.

### Own API keys or AI Credits: what is the difference?

With your own keys, you pay the AI vendor directly (OpenAI, Anthropic and others), and requests go from your server to that vendor with no T3Planet server in between. With AI Credits, you pay T3Planet from one balance on your account, usable on any install, and requests are routed through T3Planet to the AI providers.

### Which provider should I use?

OpenAI GPT-4o and Claude Sonnet are popular for quality. Gemini Flash is fast and cost-effective for bulk tasks. See [AI Providers](/en/latest/ExtNsT3AF/AIProviders/Index).

### Can I use Ollama locally?

Yes, with a custom endpoint or the Ollama provider type. This is useful for development without cloud API costs.

### Test connection fails, but the key is correct

Check the spelling of the model ID, outbound HTTPS from your server, and the vendor's service status. See [Known Problems](/en/latest/ExtNsT3AF/KnownProblems/Index).

## AI Credits

### The AI Credits toggle is on, but AI fails

Click **Activate** after you enable AI Credits. The toggle alone is not enough. See [AI Credits](/en/latest/ExtNsT3AF/T3Planet-Credit-System/Index).

### I get a zero balance error

Top up your AI Credits. You can check the balance on the [Dashboard](/en/latest/ExtNsT3AF/Dashboard/Index).

## MCP

### What is MCP?

The Model Context Protocol, a standard that lets AI tools such as Cursor or Claude Desktop connect to TYPO3. T3AF ships 100+ MCP tools. See [MCP Server](/en/latest/ExtNsT3AF/MCPServer/Index).

### How do I keep MCP access under control?

Use HTTPS and OAuth, limit which backend users may authorize agents, and test write actions in a draft workspace first.

### Cursor will not connect

Check that MCP is enabled, the site uses HTTPS, and the OAuth metadata URLs return HTTP 200. See the health check in [MCP Server](/en/latest/ExtNsT3AF/MCPServer/Index).

## Privacy

### Is data sent to US providers?

With OpenAI and Claude, yes, unless you choose EU options such as Azure EU or Mistral. Check your data processing agreement with the vendor.

### Are prompts logged?

That depends on the privacy level in [AI Permissions](/en/latest/ExtNsT3AF/Configuration/AIPermissions/Index). Choose **Minimal** or **Standard** to log less.

## Installation

### Composer reports a conflict with another MCP package

Remove the conflicting MCP server package before you install `nitsan/ns-t3af`. See [Known Problems](/en/latest/ExtNsT3AF/KnownProblems/Index).

## Still stuck?

Open [Support](/en/latest/ExtNsT3AF/Support/Index) with your TYPO3, PHP and `ns_t3af` versions, the error text, and whether you use your own keys or AI Credits.
