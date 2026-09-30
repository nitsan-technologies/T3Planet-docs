---
title: "How to prepare Google Docs with headers?"
description: "From version 14, Google Docs (EXT:ns_googledocs) uses Heading 1 and Heading 2 in your Doc to create TYPO3 content elements. Markers are no longer needed."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "ns_GoogleDocs"
  - "How to prepare Google Docs with headers?"
  - "Google Docs headings"
  - "PrepareGoogleDocWithMarkers"
sidebarTitle: "How to prepare Google Doc..."
---

## How the import reads your Doc

Version 14 reads the headings of your Doc. You do not need to add any special text.

| Part of your Doc | What happens during the import |
| --- | --- |
| **Heading 1** | Starts a new content element. The heading text becomes the element title. |
| **Heading 2** | Also starts a new content element. The heading text becomes the element title. |
| **Content below a heading** | Belongs to this element, up to the next Heading 1 or Heading 2. This includes paragraphs, Heading 3 to 6, lists, tables and images. |
| **Content before the first heading** | Becomes its own element without a title. |

<Tip>

Use the built-in **Heading 1** and **Heading 2** styles of Google Docs (**Format › Paragraph styles**). Text that is only bold or large does not start a new element.

</Tip>

## Example

This Doc has a **Heading 1** and a **Heading 2**. The import creates two content elements, one per heading, with the paragraph below each heading as its text.

![Google Doc with a Heading 1 and a Heading 2, each followed by paragraph text](./images/google_doc_heading_1_heading_2.webp)

## Choose the element type in the import dialog

The heading only decides where a new element starts. It does not decide the element type. You choose the type for each section in the import dialog:

| Element type | TYPO3 content element | What is imported |
| --- | --- | --- |
| **Header** | Header | The section title only |
| **Text Element** | Text | Title and text. Images stay inside the text |
| **Text & Image** | Text & Images | Title, text and images (media field) |
| **Image Only** | Images | Title and images (media field) |

In the dialog you can also change the element title, or untick a section to skip it. The preselected type comes from the [extension configuration](/ExtNsGoogleDocs/ImportGoogleDocToPage/Index#extension-configuration) (default: **Text & Image**). For all steps, see [The import dialog](/ExtNsGoogleDocs/ImportGoogleDocToPage/Index#the-import-dialog).

## Formatting and images

The import keeps bold, italic and underline, text alignment, text and highlight colours, links, bulleted and numbered lists, and tables. Empty paragraphs are removed.

Images from the Doc are copied to `fileadmin/ns_googledocs/` and attached to the matching content element. For details, see [Images](/ExtNsGoogleDocs/ImportGoogleDocToPage/Index#images).

## What's new in version 14

- **Headers instead of markers.** Each Heading 1 or Heading 2 starts a new content element. See [How the import reads your Doc](#how-the-import-reads-your-doc).
- **More ways to import.** Start an import from the **Page** module, the **List** module or the page tree context menu. See [Three ways to start an import](/ExtNsGoogleDocs/ImportGoogleDocToPage/Index#three-ways-to-start-an-import).
- **Default settings.** Set default record and image settings once in [Global Settings](/ExtNsGoogleDocs/NSGoogleDocsModule/Index#global-settings).
- **"Docs owned by" filter.** Choose which Docs appear in the import list: **Owned by anyone**, **Owned by me** or **Not owned by me**.
- **New TYPO3 and PHP versions.** Supports TYPO3 12.4, 13.4 and 14, with PHP 8.1 or newer.
- **Official Google API client.** The extension now uses the official Google API client library.

## Upgrading from an older version

Docs that you prepared for an older version may still contain marker lines. Prepare them for version 14 like this:

1. Remove the marker lines (for example `###TEXT###`) from the Doc. Version 14 does not need them.
2. Give each section a **Heading 1** or **Heading 2**.
3. Import the Doc and choose the element type for each section in the import dialog.

To update the extension itself, see [Updating to version 14 from 2.x](/ExtNsGoogleDocs/UpdateVersion/Index#updating-to-version-14-from-2-x-marker-based-versions).
