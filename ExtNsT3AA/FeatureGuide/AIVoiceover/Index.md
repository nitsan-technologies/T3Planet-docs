---
title: "AI Voiceover"
description: "Generate an AI voiceover for a TYPO3 page in AI Accessibility, store it in the page properties, and play it on the website with the AI Accessibility-Voiceover content element."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AA"
sidebarTitle: "AI Voiceover"
---

With **AI Voiceover**, you generate an AI audio narration of a TYPO3 page.
The audio file is saved in the page properties and played on the website with
the **AI Accessibility-Voiceover** content element.

This is separate from [AI Audio](/en/latest/ExtNsT3AA/FeatureGuide/AIAudio/Index),
which creates standalone audio files from a script.

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmrapcuhh17atqmhxhxh0i79l?utm_source=link" loading="lazy" title="T3AA Voiceover Demo" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

## Generate a page voiceover

1. Open **AI Accessibility** → **Content** → **Create a page voiceover** and
   choose the page.
   You can also open the page properties and click **Voiceover with T3AA** in
   the top button bar.
2. In the **Create a page voiceover** dialog, set:
   * **Select AI Provider** — for example T3Planet Credits or your own
     provider from AI Foundation
   * **Choose model variant** — for example **TTS-1** or **TTS-1 HD**
   * **Different Voices** — the voice, for example **Alloy**, **Echo**,
     **Fable**, **Onyx**, **Nova**
   * **Choose the speed of the generated audio** — default **1.00**
   * **Select output format file** — **mp3**, **flac** or **wav**
3. Click **Generate Audio**.
4. The file is saved to the page: **Page Properties** → **AI Accessibility**
   tab → **Voiceovers** field. One voiceover file per page is stored there.
5. Add the **AI Accessibility-Voiceover** content element to the page to play
   the audio on the website (see below).

The model and voice options depend on the selected provider. OpenAI voices are
available with T3Planet Credits and with your own OpenAI key. ElevenLabs works
with your own ElevenLabs API key only.

<Note>
The voiceover is not shown on the website automatically. Add the
**AI Accessibility-Voiceover** content element to the page.
</Note>

## OpenAI Voiceover

Use this option when you want to generate page voiceovers with OpenAI voices
instead of ElevenLabs. The steps are the same; select the OpenAI-based provider
in **Select AI Provider**.

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmrapfm8c17ngqmhxpuzr9t66?utm_source=link" loading="lazy" title="T3AA OpenAI Voiceover Demo" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

## AI Voiceover for Blog

The **Voiceovers** field is available on every page type, so blog post pages
work the same way as standard pages:

1. Open **AI Accessibility** → **Content** → **Create a page voiceover** and
   choose the blog post page (or click **Voiceover with T3AA** in its page
   properties).
2. Select the provider, model, voice, speed and format.
3. Click **Generate Audio**.
4. The file is saved in **Page Properties** → **AI Accessibility** tab →
   **Voiceovers**.
5. Add the **AI Accessibility-Voiceover** content element to the blog post and
   save.

## AI Accessibility-Voiceover content element

The **AI Accessibility-Voiceover** content element renders an audio player for
the voiceover of the current page.

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmrap6idu16mpqmhxipbc4qvl?utm_source=link" loading="lazy" title="T3AA Voiceover Content Element Demo" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

1. Add the **AI Accessibility-Voiceover** content element to the page.
2. In the plugin settings, adjust the player if needed: play button layout and
   offsets, colors, and player size.
3. Save and check the page on the website.
