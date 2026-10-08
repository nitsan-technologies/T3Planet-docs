---
title: "Solr, ke_search & indexed_search"
description: "Use AI Search with Solr, Hosted-Solr, ke_search or indexed_search, and show AI answers in their result pages."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AS"
  - "Solr"
  - "ke_search"
  - "indexed_search"
sidebarTitle: "Solr & other search extensions"
---

{/* ## Solr Settings

If the selected search engine is **Solr**, please provide the following details in case your Solr server is secured with HTTP authentication.

- **Solr Username**
  Username for Solr authentication.

- **Solr Password**
  Password for Solr authentication.

## Hosted-Solr Server Integration for Solr

The **Hosted-Solr Server** feature enables you to connect your TYPO3 instance directly to the Hosted-Solr service for improved search indexing and data retrieval.
The following guide outlines how to configure **T3AS** and **Hosted Solr** in your TYPO3 instance using the Site Configuration module.

- Step 1: Open Site Configuration

1. In the TYPO3 backend, navigate to **Site Management → Sites**
2. Edit site configuration

- Step 2:Scroll down to the **Solr** section in the same T3AS tab and Configure Solr Integration

   - **Hosted Solr Server**: Enable this checkbox.
   - **Hosted Solr Cores**: Enter one or more Solr cores separated by commas
     (e.g., `core_en,core_de`).

- Step 4: Define Solr Connection Settings

- Switch to the **Solr** tab within the Site Configuration.
- Enable the **Enable Solr for this site** option.
- Provide the connection details:

  - **Scheme:** `http` or `https`
  - **Host:** Enter your Hosted-Solr host address
    (e.g., `562d8a85dc0-icy-tree-111:eecbaaae879b@node-14.hosted-solr.com`)
  - **Port:** Usually `443` for secure connections
  - **URL Path:** Provide the Solr path without `/solr/`
    (e.g., `/562d8a85dc0-icy-tree-111/`)

- Step 5: Save Configuration

## Getting Started

1. **Create an Account:**
   Sign up on the Hosted-Solr platform using your email address.

2. **Create a Solr Core:**
   Once your account is active, create a new Solr core.

3. **Configure in TYPO3:**
   Add your Solr core connection details within the **TYPO3 Site Settings**.

This integration allows you to seamlessly manage your Solr configuration and maintain consistent communication between TYPO3 and the Hosted-Solr environment.

## Verifying the Connection

After configuration, ensure that Solr is properly connected:

- Navigate to the **Info module** inside the **Solr tab** within your TYPO3 backend.
- Verify that the Solr connection status and indexing information appear correctly.

## Additional Fields Support

The extension now supports fetching **additional fields** from Solr beyond the standard predefined set.

This means you can include **custom or project-specific fields** in your search configuration to enhance indexing and display flexibility.

**Configuration Steps**

1. Go to **AI Foundation** → **AI Features** and open the **T3AS** feature card (or the related T3AS Solr settings in your project setup).
2. Specify which fields should be retrieved from Solr.
3. Save your settings to enable greater control over search results and data output.

By leveraging this feature, you can tailor your Solr-based search experience to match the exact needs of your TYPO3 project.

<Note>
Several default fields are automatically included for content retrieval from Solr: `id`, `site`, `type`, `uid`, `content`, `pid`, `url`, `changed`, and `access`. Ensure that Solr is properly configured and that the `content` field is available in your Solr-indexed data.
</Note> */}

## Solr settings

Only needed if you use **Solr** (a separate search server) as a data source.

1. Go to **AI Universe → AI Foundation → AI Features**.
2. Click **Configure** on the card **Solr configurations**.
3. If your Solr server needs a login, enter the **Solr username** and **Solr password**.
4. If you use the Hosted-Solr service, turn on **Hosted Solr Server** and enter your **Hosted Solr Cores**, for example `core_en,core_de`.
5. Optional: add **Additional fields** that AI Search should read.
6. Click **Save**.

## Connect TYPO3 to Hosted-Solr

1. Create an account and a Solr core on the Hosted-Solr website.
2. Open your site configuration: **Site Management → Sites** (TYPO3 v12/v13) or **Sites → Setup** (TYPO3 v14).
3. Edit your site.
4. Open the **Solr** tab. (It only exists when the Solr extension is installed.)
5. Turn on **Enable Solr for this site**.
6. Enter the **Scheme**, **Host**, **Port** (usually `443`) and **URL Path** from Hosted-Solr.
7. Save.
8. Check the connection in the Solr **Info** module.

{/* 2. In TYPO3, go to **Site Management → Sites** and edit your site.
3. Open the **Solr** tab (from EXT:solr) and turn on **Enable Solr for this site**. */}

## Using ke_search and indexed_search

Already use ke_search or indexed_search? Make sure your website is fully indexed by that extension and training has run.

<a id="inject-ai-search-results"></a>

## Injecting AI Search result in TYPO3 Search Extensions

You can show an AI answer above the normal results of ke_search, indexed_search or Solr. Your developer needs to add a small snippet to the search template. Full guide: [AI answers in other search extensions](/en/latest/ExtNsT3AS/InjectingAISearchResults/Index).

## Enable AI Search plugin using TypoScript

Developers can also show the AI Search plugin with TypoScript. See [Enable AI Search plugin using TypoScript](/en/latest/ExtNsT3AS/InjectingAISearchResults/Index#enable-ai-search-plugin-using-typoscript).
