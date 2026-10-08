---
title: "Known Problems"
description: "Known problems and workarounds for AI Search (T3AS), including streaming gzip issues on older versions."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AS"
  - "Known Problems"
sidebarTitle: "Known Problems"
---

Known issues and how to fix them.

## Streaming search response does not work (T3AS 14.2.2 or older)

**Who is affected:** AI Search **14.2.2 or older** on **TYPO3 v12 / v13**.

**What you see:** the answer stays empty, comes very late, or the browser shows an error.

**Why:** TYPO3 compresses (gzips) whole pages before sending them. AI Search shows its answer word by word while it is written, and compression breaks this.

### Best fix

Update AI Search to a version newer than 14.2.2. Newer versions switch off compression only for the search answer, so the rest of your website stays compressed.

### Workaround (14.2.2 or older)

Your developer can switch off TYPO3 page compression:

1. Open `config/system/settings.php`.
2. Find this line:

```php
$GLOBALS['TYPO3_CONF_VARS']['FE']['compressionLevel'] = 5;
```

3. Remove the line, or change it to:

```php
$GLOBALS['TYPO3_CONF_VARS']['FE']['compressionLevel'] = 0;
```

4. Clear all caches.
5. Test a search again.

<Note>
This switches off TYPO3 compression for **all** pages. Your web server (Apache or nginx) can still compress pages.
</Note>

## Report a Problem

Something not working? Contact us through the support portal: [https://t3planet.de/support](https://t3planet.de/support)

{/* Original text before the 8 Oct 2026 simplification (kept for reference):

**Affected versions:** T3AS **14.2.2 or older** (and the matching T3CS base package), on **TYPO3 v12 / v13**.

On these versions, the search answer may stay empty, appear only after a long delay, or fail in the browser with a content-decoding error. In the Network panel, the streaming request often shows:

```text
Content-Encoding: gzip
```

instead of an uncompressed event stream.

### Cause

TYPO3 frontend compression is still enabled in `settings.php`:

When this value is `1`–`9`, TYPO3 gzip-compresses the full frontend response and adds `Content-Encoding: gzip`. Search streaming needs incremental Server-Sent Events. Gzip waits for the complete body before sending it, so the live response cannot be delivered.

This is TYPO3 core frontend compression, not a search configuration error.

1. Open `config/system/settings.php`.
2. Find:

3. **Remove** that line, or set:

4. Flush all TYPO3 caches.
5. Run a search again. The streaming response should work, and `Content-Encoding: gzip` should no longer be applied to that request.

<Note>
Setting `compressionLevel` to `0` disables TYPO3 application-level gzip for **all** frontend pages. HTML compression can still be handled by the web server (Apache `mod_deflate`, nginx `gzip`).
</Note>

<Tip>
**Newer T3AS releases** disable gzip only for search streaming requests. After you update past 14.2.2, you can keep `compressionLevel = 5` for normal pages.
</Tip>

Facing trouble while using the T3AS extension?

We're here to help! Please report your issues through our support portal:
[https://t3planet.de/support](https://t3planet.de/support)
*/}
