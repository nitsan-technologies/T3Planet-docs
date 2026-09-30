---
title: "Accessibility Widgets"
description: "**Accessibility Widgets** configures the frontend accessibility widget in T3AA (`EXT:ns_t3aa`)."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AA"
sidebarTitle: "Accessibility Widgets"
---

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmu2a8y5d0mllqmrxp8jxg1ue?utm_source=link" loading="lazy" title="T3AA Accessibility Widgets Feature Demo" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

## What it is

**Accessibility Widgets** configures the frontend accessibility widget in
T3AA (`EXT:ns_t3aa`).

The widget is a floating button on the website. Visitors open it and turn
accessibility tools on or off for their own browser session (font size,
contrast, reading aids, and similar options).

In the TYPO3 backend you decide:

* Whether the widget is shown
* How the button and panel look (icon, size, color, position, layout)
* Which tools and accessibility profiles are available
* Your branding and the accessibility statement shown in the widget

Settings are saved per site in `config.yaml`. It does not change page content
in the database.

![Enable Assistant Widget in AI Foundation General Settings](../images/enable-assistant-widget.webp)

## How to use it

**Activate the feature**

1. Open **AI Foundation** → **AI Features**.
2. Open **General Settings**.
3. Enable **Enable Assistant Widget** and save.

**Configure the widget**

4. Open the T3AA dashboard and click **Accessibility Widgets**.
5. Set widget options (icon, position, style, layout, profiles, settings,
   branding, accessibility statement).
6. Enable or disable the accessibility tools you want visitors to see.
7. Click **Save Settings**.
8. Flush caches and check the frontend.

On the website, visitors click the floating button, open the panel, and use the
enabled tools or profiles. Changes apply only in their browser.

<Note>
The widget needs **Enable Assistant Widget** (under **AI Foundation** →
**AI Features** → **General Settings**) and a valid license/domain for the
site. If it does not appear, check those first, then flush caches.
</Note>

## Widget configuration

Accessibility Widgets has these configuration tabs: **Widget Icon And Size**,
**Widget Position**, **Widget Style**, **Widget Layout**, **Profile Selection**,
**Widget Settings**, **Widget Branding** and **Accessibility Statement**.

## Widget Icon and Size

Choose the launcher size (**Small**, **Medium**, **Large**) and one of six icon
styles (**Widget Style 1–6**).

Default in the extension: **Large** + **Style 1**.

## Widget Position

Set desktop and mobile placement separately.

* **Standard position** — left/right and top/middle/bottom (default: right
  bottom on desktop and mobile).
* **Widget Hide on Desktop / Mobile** — hide the launcher on that device type.
* **Exact positioning** — enable exact position, then set X/Y in pixels
  (desktop about **5–500** px; mobile about **5–300** px as labeled in the UI).

Exact position fields work only when exact positioning is enabled.

## Widget Style

* Primary color: **Solid** or **Gradient**
* Color pickers for solid/gradient and header text color
* Appearance: Default, Dark, or System

Default solid color in code: `#0101d9`. Default header text: `#ffffff`.

## Widget Layout

* **Simple Layout** — default, clear single panel
* **Flexible Layout** — responsive arrangement
* **Minimal Layout** — fewer controls (Motor Impaired and Blind profiles are
  hidden with this layout)
* **3 Column Layout** — tools arranged in three columns

## Profile Selection

Turn accessibility profiles on or off, then choose which profiles appear:

Motor Impaired, Blind, Color Blind, Dyslexia, Low Vision, Cognitive and
Learning, Seizure and Epileptic, ADHD, Elder.

A profile turns on a fixed group of tools at once. Only one profile can be
active at a time.

## Widget Settings

* **Select Widget Language** — default or `en`, `es`, `fr`, `de`,
  `it`, `pt`
* **Move/Drag Widget** — visitors can drag the button (not on mobile)
* **Widget Large** — larger text/icons/buttons inside the widget
* **Widget Tooltip** — hover help text on widget options
* **Widget Mode** — light / dark / system for the widget UI

## Widget Branding

Show your own brand in the widget instead of T3Planet.

Turn on **White-label Settings**, then fill in:

| Field | What it does | Default |
| --- | --- | --- |
| **Brand Title(Name)** | Company name shown as the title in the widget panel header (max. 70 characters) | `T3Planet` |
| **Brand Website** | Link target of the logo in the widget footer | `https://t3planet.de/` |
| **Brand Logo URL** | Full URL of the logo image shown in the widget footer | T3Planet logo |

The fields can only be edited while **White-label Settings** is on. When it is
off, the widget shows the default panel title, the T3Planet logo and a
**Feedback** link in the footer. The preview on the right shows the result.

## Accessibility Statement

Create an accessibility statement for your website and link it from the
widget. **Website name**, **Contact email** and **Last audit date** are
required.

**Statement link in the widget**

| Field | What it does |
| --- | --- |
| **Add Accessibility Statement to Widget** | Shows the statement link in the widget footer (enabled by default) |
| **Link** | URL of the page on your website that contains the statement |
| **Link Text** | Text of the link in the widget footer, for example “Accessibility Statement” |

The link appears in the footer of the widget panel and opens in a new tab. It
is shown only when **Add Accessibility Statement to Widget** is on **and**
both **Link** and **Link Text** are filled.

**Statement content**

| Field | Required | What it does |
| --- | --- | --- |
| **Website name** | Yes | Website URL shown in the main title of the statement. Pre-filled with the site base URL. |
| **Contact email** | Yes | E-mail address for accessibility feedback. Pre-filled with your backend user e-mail. |
| **Contact phone** | No | Phone number for feedback |
| **Address** | No | Postal address for feedback |
| **Number of business days to respond** | No | Response time shown in the statement (1–30 days) |
| **Last audit date** | Yes | Date of your last accessibility audit, shown in the statement header and audit section |

The generated statement covers compliance status (WCAG), screen reader and
keyboard support, accessibility profiles, display adjustments, the last audit
date and your feedback contact. Check the preview on the right.

**Publish the statement on your website**

1. Fill in the statement fields and save.
2. In the preview, switch between **Text** and **HTML**, then use
   **Copy statement** or **Download** (HTML or Text).
3. Add the statement to a page on your website, for example
   `/accessibility-statement`.
4. Enter that page URL in **Link** and a **Link Text**, then save.
5. Flush caches and check the link in the widget footer.

<Note>
The statement is not published automatically. Visitors see it only on the page
where you add it, and through the widget link once **Link** and **Link Text**
are set.
</Note>

## Accessibility tools

Each tool is a card in Accessibility Widgets. If enabled and saved, it appears
in the frontend widget. If disabled, visitors do not see it.

## Reading and text

* **Screen Reader** — reads page content aloud (speed/pitch can be limited in
  config)
* **Readable Font** — switches to clearer fonts
* **Font Size** — increases or decreases text size
* **Letter Space** — changes space between letters
* **Word Space** — changes space between words
* **Line Height** — changes space between lines
* **Text Align** — left / center / right
* **Text Magnify** — magnifies text
* **Highlight Header** — highlights headings
* **Highlight Links** — highlights links
* **Reading Mask** — focuses on one reading band
* **Reading Guide** — follow-along reading line
* **Read Mode** — simpler reading layout

## Vision and color

* **Contrast** — overall contrast
* **Color Contrast** — text vs background contrast
* **Saturation** — color intensity
* **Invert Filter** — inverts colors
* **Grayscale** — removes color
* **Color Deficiency** — color correction modes
* **Dark/Light** — light or dark page mode
* **Blue Filter** — warmer screen tone
* **Blue Filter by Sun Position** — blue filter by sun position
* **Blue Filter by Time** — blue filter by time of day
* **Cursor** — larger or colored cursor
* **Blur** — softens parts of the view
* **Zoom** — zoom in/out
* **Hide Images** — hides images

## Motion, sound, and structure

* **Pause Animations** — stops motion effects
* **Mute** — mutes audio
* **Voice Navigation** — voice commands (browser support required)
* **Page Structure** — shows page structure for orientation

## How profiles behave

When a visitor selects a profile, the widget enables this tool set:

| Profile | Tools turned on |
| --- | --- |
| Motor Impaired | Pause animations, Text magnify |
| Blind | Screen Reader |
| Color Blind | Contrast, high saturation, readable/dyslexia font, pause animations |
| Dyslexia | Dyslexia-oriented font |
| Low Vision | Bigger text, pause animations, readable font, bigger cursor, text magnify, high saturation |
| Cognitive and Learning | Contrast, bigger text, pause animations, reading guide, text magnify |
| Seizure and Epileptic | Pause animations, low saturation |
| ADHD | Pause animations, reading mask, low saturation |
| Elder | Bigger text, bigger cursor |

Selecting another profile replaces the previous one. Visitors can also use
individual tools without a profile.
