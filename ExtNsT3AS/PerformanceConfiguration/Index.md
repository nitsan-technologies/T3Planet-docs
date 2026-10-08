---
title: "Performance Configuration Based on Database Size"
description: "The extension’s performance depends on the amount of vector data stored in the database. As the number of vectors increases, PHP memory and execution limits must be adjusted to prevent timeouts and memory issues."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AS"
  - "Performance Configuration Based on Database Size"
sidebarTitle: "Performance Configuration Based on Database Size"
---

## Overview

The more content AI Search has learned, the more memory and time your server needs to answer. If searches or training stop with a timeout or memory error, ask your hosting provider or developer to raise the PHP limits below.

Pick the level that matches the number of learned items (vectors). You see the number on the **Dashboard** in **AI Universe → AI Chatbot/Search**.

<Note>
These values are set on the server (in PHP settings), not in the TYPO3 backend.
</Note>

## Low Level (≤ 25,000 vectors)

For small websites and first setups.

```ini
memory_limit = 512M
max_execution_time = 120
max_input_time = 120
default_socket_timeout = 120
```

## Medium Level (25,000 – 150,000 vectors)

For medium-sized websites.

```ini
memory_limit = 1024M
max_execution_time = 300
max_input_time = 300
default_socket_timeout = 300
```

## High Level (150,000 – 250,000+ vectors)

Needed for large websites, so searches and training don't time out.

```ini
memory_limit = 2048M
max_execution_time = 900
max_input_time = 900
default_socket_timeout = 900
```

{/* Original text before the 8 Oct 2026 simplification (kept for reference):

The extension’s performance depends on the amount of vector data stored in the
database. As the number of vectors increases, PHP memory and execution limits
must be adjusted to prevent timeouts and memory issues.

**Recommended for:** Small datasets and initial setups.

**Recommended for:** Moderate vector volumes.

**Required for:** Large datasets to avoid execution timeouts and memory errors.
*/}
