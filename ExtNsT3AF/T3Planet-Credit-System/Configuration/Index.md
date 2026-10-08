---
title: "Configuration"
description: "Documentation for Configuration (ExtNsT3AF)."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "ExtNsT3AF"
sidebarTitle: "Configuration"
---

Switch on T3Planet Credits, set limits per editor group and buy more credits.

**Path:** **AI Universe → AI Foundation → AI Providers**

## Before you start

- AI Foundation is installed and active.
- Your free AI Foundation license key is active (in the **T3Planet Shop**).
- Your server can connect to the T3Planet service (ask your hosting provider if unsure).

## Activate Credits

1. Go to **AI Universe → AI Foundation → AI Providers**.
2. Choose **T3Planet Credits**.
3. Confirm if asked.
4. Click **Activate** if it is shown.
5. Wait for the success message. The page reloads.

![AI Providers with T3Planet Credits selected and Activate button](images/t3planet-credits-activate.webp)

Select T3Planet Credits, then click Activate.

![AI Providers with T3Planet Credits active and credit balance panel](images/t3planet-credits-providers.webp)

After activation — T3Planet Credits active, balance panel, and
Buy more credits.

<Note>
**Activate** failed? Check that your license key is valid and that your server can reach the T3Planet service, then try again. See [Troubleshooting → Activation failed](/en/latest/ExtNsT3AF/T3Planet-Credit-System/Troubleshooting/Index#activation-failed).
</Note>

## After activation

- AI requests go through T3Planet and use your credit balance.
- They are listed in **AI Usage** as `t3planet_credits`.
- The Credits panels appear. Your own provider list is hidden.
- You see the balance on the **Dashboard** and in the Credits panel.
- Switch back to **Your Own API Keys** at any time – your saved providers come back.

## Group limits

Limit how much each editor group may use.

1. Go to **AI Universe → AI Foundation → AI Permissions**.
2. Select the backend user group.
3. In the **Limits** step, set:
   - **Monthly credit limit** – the most credits the group may use per month.
   - **Daily request limit** – the most AI requests the group may send per day.
4. Apply.

Administrators have no limits.

## Buy more credits

1. Click **Buy more credits** on the Credits panel or the **Dashboard**.
2. Complete the purchase on the T3Planet checkout page.

Your invoices are in your T3Planet account.

<Warning>
If T3Planet returns a rate-limit message, wait for the shown cooldown before
retrying.
</Warning>

{/* Original text before the 8 Oct 2026 simplification (kept for reference):

Turn on T3Planet Credits from AI Foundation and manage limits and top-ups.

**Path:** AI Foundation > AI Providers

- AI Foundation (`EXT:ns_t3af`) installed and active
- Valid OSS license key available (`EXT:ns_license`)
- Server can reach the T3Planet API

1. Open AI Foundation > AI Providers.
2. Choose T3Planet Credits.
3. Confirm if asked.
4. Click Activate if shown.
5. Wait for success → page reloads.

<Note>
If Activate fails, check that your OSS license key is valid, the server can
reach the T3Planet API, and try again. See
[Troubleshooting](/en/latest/ExtNsT3AF/T3Planet-Credit-System/Troubleshooting/Index#t3planet-credits-troubleshooting) for common fixes.
</Note>

When Credits is active:

- Billable AI calls go through T3Planet and use your credit balance
- Usage is logged in AI Usage as `t3planet_credits`
- Credits panels appear and the own provider list is hidden
- Balance is available on the Dashboard and Credits panel
- Switching back to Your Own API Keys restores your saved providers

Set per-group usage caps in AI Foundation > AI Permissions.

1. Open AI Permissions.
2. Select the backend usergroup.
3. Configure credit-related limits for that group.

What can be capped:

- **Monthly credit limit** — Maximum credits the group may use per month
- **Daily request limit** — Maximum AI requests the group may send per day

Administrator users are exempt from these caps.

When your balance is low, open Buy more credits on the Credits
panel or Dashboard. You complete purchase on the T3Planet checkout page;
invoices stay in your T3Planet account.
*/}
