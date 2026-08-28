# Claimable — The Entitlement Autopilot
*(working name, pending trademark clearance)*

## The blind spot

Modern consumers accumulate a sprawling, invisible portfolio of pre-paid entitlements: credit card purchase protection, price-drop refunds, trip-delay insurance, cell-phone damage coverage, extended warranties, retailer price-adjustment policies, insurance riders (identity theft, legal assistance), employer perks (wellness stipends, FSA/HSA), membership perks (Prime credits, airline credits, Costco price adjustments). Nobody has ever aggregated "what am I entitled to right now, and did anything just happen that qualifies me?"

The category doesn't fully exist yet. Bill-negotiation apps (Rocket Money, Trim) attack recurring subscriptions. Warranty trackers (Sortly) require manual entry and stop at "reminder" — they never file anything. The old price-protection bots (Paribus, Earny) covered one narrow slice each and both shut down. No consumer product spans **discovery + passive trigger detection + automatic claim filing** across the full spread of cards, insurance, retail policies, and employer benefits. That gap is the blind spot.

The frustration isn't one big daily annoyance — it's dozens of small, recurring "ugh, I should look into that" moments a year: Did my flight delay qualify for reimbursement? Is this still under warranty? Did the price drop after I bought it? Do I even have coverage for this? Each one is a 20-minute PDF-hunting, hold-music chore for $20–$200 — not worth an afternoon, so almost nobody does it, and issuers/insurers benefit from that (unredeemed benefits are a designed-in margin for them).

## The concept

Claimable turns "you're entitled to something" into a single push notification with one button: **File it**.

- **Connect once.** Link cards (Plaid-style, read-only) and, optionally, a purchase-confirmation-only email scope (OAuth, read receipts/flight/order confirmations only). No manual data entry, ever.
- **Entitlement graph.** Claimable maintains a continuously-updated, machine-readable map of what every major card, insurer, retailer, and membership actually promises in its fine print, and matches it against the user's real purchases and policies.
- **Passive trigger detection.** It watches for the moments that activate a benefit: a flight delay, a price drop on something bought 12 days ago, a cracked screen (user just snaps a photo), an item still inside its warranty window.
- **One-tap filing.** When a match fires, the user gets a prompt like: *"Your flight to Denver was delayed 3h — your card covers up to $500 in trip-delay reimbursement. File now?"* One tap auto-fills the claim with stored receipts/confirmations and submits it; Claimable tracks status and chases follow-ups until it's paid or denied.
- **One number.** The app collapses to a single running total on the home screen: *"$1,240 recovered this year · $310 in unclaimed benefits waiting."* That number is the entire retention mechanism — nobody deletes an app that's visibly making them money.

## Why it's frictionless

No forms, no PDFs, no hold music, no manual entry. The user's only actions are: link an account once, and tap "File" when prompted. Everything else — matching, drafting, submitting, following up — happens off-screen. The UX bet is that the app should feel less like a tool and more like a background process that occasionally hands you money.

## Why now

Two enabling shifts make this buildable today in a way it wasn't five years ago: open-banking APIs (Plaid and peers) made secure, read-only financial linking routine, and LLMs made it tractable to parse thousands of pages of card/insurer/retailer terms-and-conditions into structured, queryable rules — the exact kind of fine-print extraction that benefits from cross-checking one model's reading of a policy against another's before it's trusted to auto-file a claim on someone's behalf.

## Monetization strategy

Four streams, deliberately structured so the app makes money *with* the user, not off friction:

1. **Contingency transaction fee (primary).** A 15–25% cut of money actually recovered through a filed claim — trip-delay payouts, price-adjustment refunds, warranty payouts. No recovery, no fee. This aligns Claimable's incentives with the user's and anchors the revenue model on a "we found you money" basis.
2. **Subscription tier (~$7–9/mo or ~$60/yr).** The free tier files claims on a delay (e.g., 48 hours) and caps concurrent claims; paying subscribers get instant filing, unlimited concurrent claims, a household/family plan across shared cards, and a human-in-the-loop specialist for disputed claims. The lever is speed and coverage, not withholding a feature people need, so the free tier stays genuinely useful and word-of-mouth-able.
3. **B2B partnerships with issuers, insurers, and retailers.** Card issuers and insurers already lose money when perks go unredeemed (it hurts retention and NPS); Claimable sells itself to them as an outsourced "benefit activation engine" — a licensing/API deal to white-label the entitlement graph inside their own apps, priced per activated user or per successful redemption. Retailers and warranty administrators pay a lead-gen/affiliate fee when Claimable surfaces "you have accidental damage coverage on this — file now?" and routes the claim to them.
4. **Aggregate benefit-utilization insights (secondary, privacy-gated).** Anonymized, opt-in trend reports sold to issuers/insurers on which benefit types actually get redeemed and where users abandon claims. Only ever aggregate/statistical, never individual-level, with explicit opt-in and no default data sale — this stream only ships once the core product has earned enough trust to ask for it.

**Illustrative (not sourced) unit-economics sanity check**, just to stress-test the model: if an average active user recovers ~$150/year in claims, a 20% contingency fee yields ~$30/user/year before any subscription revenue — meaning the subscription tier isn't optional padding, it's what makes the economics work for the large share of users who file zero claims in a given year but still value the dormant-benefit nudges and the peace of mind.

## Go-to-market wedge

Launch narrow, not broad: start with premium travel credit cards only (Chase Sapphire/Amex Platinum-tier). That segment has the highest per-claim dollar value, the best-documented benefit terms, and an existing, vocal "travel hacking" community primed to evangelize a tool that pays for itself in one trip-delay claim. Expand next into price-protection/returns (higher frequency, lower value, builds daily-habit usage), then into insurance riders and employer benefits (higher value, slower sales cycle, B2B-assisted distribution).

## Risks and guardrails

- **Trust risk in auto-filing.** Only auto-submit above a high confidence threshold; anything ambiguous goes to a one-tap "review before sending" queue instead of firing blind.
- **Issuer pushback.** Frame the pitch around retention/spend lift, not claims-cost increase, and land first with issuers who already market "richness of perks" as their differentiator — they need redemption to be real for that pitch to hold.
- **Regulatory exposure.** Position Claimable as *assisting the user in self-filing* rather than acting as a licensed claims adjuster or broker, to stay outside insurance-licensing requirements; get this structure reviewed by counsel before the insurance-vertical expansion.
- **Data trust.** Read-only, revocable linking; never sell individual-level data; SOC 2 from day one — the entire business depends on being trusted with financial account access, so this is table stakes, not a nice-to-have.
