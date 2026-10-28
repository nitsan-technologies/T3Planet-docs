---
title: "Troubleshooting"
description: "Documentation for Troubleshooting (ExtNsT3AF)."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "ExtNsT3AF"
sidebarTitle: "Troubleshooting"
---

## Quick smoke test

Before digging into individual symptoms:

1. Credits is **Selected** and **Activated**?
2. Balance loads on Dashboard / Providers?
3. One AI action → AI Usage shows `t3planet_credits`?
4. Switching to Your Own API Keys restores the provider list?

## Activation failed

1. Check the server can reach the T3Planet API (outbound HTTPS)
4. Flush caches → retry Activate
3. Still failing? Open [Support](/en/latest/ExtNsT3AF/Support/Index) with the exact error text

No licence key or domain registration is involved in activation.

## Balance missing

1. Confirm Activate completed (Active, not only Selected)
2. Reload Providers / Dashboard
3. Check for a rate-limit message
4. If balance is `0`, [buy credits](/en/latest/ExtNsT3AF/T3Planet-Credit-System/BuyCredits/Index) or switch to Own API Keys if you need AI without a credits balance

## Claim code not accepted

1. Paste the code again. Spaces and line breaks are removed for you.
2. Request a new code with **Email me a code** in the same dialog, using the email address of your T3Planet credits account.
3. If the dialog shows an error from T3Planet, copy the text and open [Support](/en/latest/ExtNsT3AF/Support/Index). Do not send the claim code itself.

Full guide: [Use a claim code](/en/latest/ExtNsT3AF/T3Planet-Credit-System/ClaimCode/Index).

## Claim link is missing

**Use a claim code** sits at the bottom of the **T3Planet Credits** card on **AI Foundation → AI Providers** (text: *Bought credits on t3planet.de?*). It is shown before and after Credits is active. If you do not see it:

1. Select a page in the page tree. Without a selected page the module only asks you to select a site.
2. Reload the module and look at the card on the right of **AI Provider Mode**.
3. Check that your backend user may manage AI Providers.

See [Use a claim code](/en/latest/ExtNsT3AF/T3Planet-Credit-System/ClaimCode/Index).

## This server IP already belongs to a paying account

T3Planet allows one free trial per public server IP. If the IP is already linked to a paid account, **Activate** is refused. Use that account's claim code instead.

## Token does not match this server

*This T3Planet Credits token is registered to a different server IP.* The server IP changed (new host, proxy or move). Click **Activate** again from this server, or connect with a [claim code](/en/latest/ExtNsT3AF/T3Planet-Credit-System/ClaimCode/Index).

## Checkout does not open or a purchase is not visible

- Use **Open in new tab** in the checkout window if the embedded page is blank.
- Bank transfers show *Payment pending*. Credits arrive when the payment clears.
- After a payment, wait a minute and reload **AI Providers**. Purchases show in **Recent AI Usage** after the next sync.
- **Checkout unavailable** on a bundle: reload, or buy on [t3planet.de/ki-credits](https://t3planet.de/ki-credits) and use a claim code.

See [Buy credits](/en/latest/ExtNsT3AF/T3Planet-Credit-System/BuyCredits/Index).

## No `t3planet_credits` in AI Usage

1. Is Credits still active?
2. Did the action call AI Foundation AI?
3. Check the date filter

## Provider list missing

Expected while Credits is on. Switch to Your Own API Keys to edit
providers again.

## Module shows empty or an error

- Select the site root in the page tree, then reopen the module
- Flush caches and reload
- Confirm your backend user can access AI Foundation modules

## Rate limited

T3Planet returned a temporary cooldown. Wait for the shown period, then retry.

## Insufficient credits

Balance is too low for the next request. Buy more credits, or switch to
Your Own API Keys.
