---
# old title: "T3AS Search Plugin"
title: "AI Search plugin"
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AS"
  - "T3AS Search Plugin"
# old sidebarTitle: "T3AS Search Plugin"
sidebarTitle: "AI Search plugin"
---

## Overview

The **AI Search** plugin puts an AI search box on one page of your website. Use it when you want a search page, or when one page needs different settings (for example other colours) than the rest of the website.

Settings for the whole website are on the [Search tab](/en/latest/ExtNsT3AS/Configuration/Search/Index). The plugin settings only apply to the page where you add it.

{/* <div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmf40ewn21x4v39ozrnrdxqmm" loading="lazy" title="AI FileMeta Overview Demo" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div> */}

{/* The **T3AS Search** plugin places an AI search box on your TYPO3 frontend. Visitors type a question in plain language and get an answer based on content you have trained in T3AS.

You can set colours, layout, suggested questions, chatbot follow-ups, voiceover, and feedback for each page. Site-wide defaults are in **T3AS → Search** (see [5. Search tab](/en/latest/ExtNsT3AS/Configuration/Search/Index)). */}

## Interactive Demo

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmrak5f4u0vicqmhxqgs1cufg?utm_source=link" loading="lazy" title="T3AS Search Plugin Demo" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

{/* SUPADEMO NEEDED: Add the AI Search plugin (General, Search Box, Search Results, Enable dark mode) */}

## Add the Plugin to a Page

1. Open the page in the page module (**Web → Page**, on TYPO3 v14 **Content → Layout**).
2. Click **+ Content**.
3. Open the **Plugins** tab.
4. Choose **AI Search**. (It is currently listed as **AI Search Search**.)
5. Open the **Plugin** tab of the new content element.
6. Set up the tabs **General**, **Search Box** and **Search Results** (see below).
7. Click **Save**.
8. Open the page on your website and try a search.

{/* **Step 2:** Click **Create new content** and choose a container — for example **Accordion** for Q&A-style layouts.

**Step 3:** Inside the container, add the **T3AS Search** plugin.

**Step 4:** Configure the **Plugin**, **Search Box**, and **Search Results** tabs.

**Step 5:** Click **Save and close** or **Save and refresh**, then check the frontend. */}

{/* ## Plugin Tab

Controls the look of the search box on this page.

- **Title** — Heading above the search box (e.g. `Search`)
- **Select Style** — **Default Style** uses your site theme; **Customized Style (plugin)** lets you pick colours
- **Box Layout** — Container layout (e.g. `Box`)
- **Search Icon** — Icon shown in the search field
- **Select Loader** — Loading animation: **Skeleton Loader** or **Typing Loader**
- **Primary Color** / **Secondary Color** / **Text Color** — Only available with **Customized Style**
- **Border Radius** — Corner style (e.g. **Semi Rounded**)
- **Reference Links** — Show source links below the AI answer

## Search Box Tab

Controls the search input and suggested questions.

- **Search Form Type** — How the input is laid out (e.g. `With Button`)
- **Button Type** — **Search Icon** or **With Label**
- **Search Input Placeholder** — Hint text inside the field
- **Recent Search** — Show the visitor’s previous searches
- **Recent Search Title** — Label above recent searches
- **Predefined Questions** — Show clickable question suggestions
- **Question Position** — Where suggestions appear relative to the search box
- **Number of Questions Limit** — How many suggestions to show
- **Questions Storage Folder(s)** — TYPO3 folder that holds question records

## Search Results Tab

Controls how AI answers are displayed on this page.

- **Enable Chatbot Mode** — Visitors can ask follow-up questions after the first answer
- **Enable Search Feedback** — Thumbs up/down on answers; saved in **Usage Analytics**
- **Enable Voiceover** — Play button to hear the answer read aloud
- **Result Style** — **Summarize** (short) or **Long Answer** (detailed)
- **Reference Links** — Source links for this plugin instance */}

## General

How the search box looks.

- **Title** – a heading above the search box.
- **Select Style** – **Default** uses your website design. **Customized Style** uses the colours you pick here.
- **Box Layout** – **Box** or **Full** (full width).
- **Search Icon**, **Select Loader** (loading animation), **Border Radius** (corners).
- **Primary Color**, **Secondary Color**, **Text Color** – only used with **Customized Style**.
- **Button Class** / **Input Class** – optional style names from your website design. Ask your developer; only used with **Default**.

## Search Box

The input field and example questions.

- **Search Form Type** – **Default** or **With Button**.
- **Button Type** – **Search Icon** or **With Label**. With a label, enter the **Search Button Text**.
- **Search Input Placeholder** – the grey hint text in the field.
- **Recent Search** – show the visitor's last searches. **Recent Search Title** is the heading above them.
- **Predefined Questions** – show clickable example questions.
- **Question Position**, **No. of questions limit**, **Questions storage folder(s)** – where they show, how many, and the folder that holds them.

## Search Results

How answers look.

- **Enable Reference Links** – links to the pages or files the answer comes from.
- **Enable chatbot mode** – visitors can ask follow-up questions.
- **Enable search feedback (thumbs)** – visitors rate answers; you see the ratings in **Usage Analytics**.
- **Enable voiceover** – a play button reads the answer aloud.
- **Enable dark mode** – adds a light/dark switch to the answer area.
- **Result Style** – **Summarize**, **Short Answer** or **Long Answer**.

<Note>
These settings only apply to this content element. For the whole website, use **AI Universe → AI Chatbot/Search → Search**.
</Note>

{/* <Note>
Plugin settings apply to this content element only. For site-wide defaults, use **T3AS → Search**.
</Note> */}

## Tips

- Keep **Default** style unless the page needs its own colours.
- Turn on **Enable chatbot mode** on help or FAQ pages.
- Show 3–5 example questions, not more.
- After saving, test a real question on the website.

{/* - Enable **Chatbot Mode** on help, docs, or FAQ pages */}

## Related

- [Search tab](/en/latest/ExtNsT3AS/Configuration/Search/Index) – site-wide defaults for every page
- [Search widget](/en/latest/ExtNsT3AS/Configuration/Search/Index#search-widget) – the floating search button
- [AI answers in ke_search, indexed_search or Solr](/en/latest/ExtNsT3AS/InjectingAISearchResults/Index)
- [AI Chatbot](/en/latest/ExtNsT3AC/Introduction/Index) – a chat window that uses the same trained content

{/* Original text before the 8 Oct 2026 simplification (kept for reference):

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmrak5f4u0vicqmhxqgs1cufg?utm_source=link" loading="lazy" title="T3AS Search Plugin Demo" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>
## Add the Plugin to a Page
*/}
