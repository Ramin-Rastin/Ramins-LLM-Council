# WillBox — Investment Memo
*(working name)*

## Executive summary

WillBox is a mobile app that lets a person — most urgently someone with a terminal diagnosis, and just as usefully someone who is simply getting older and wants to get ahead of it — record video, voice, and photo explanations of who should receive each of their meaningful possessions, and *why*. It is explicitly not a will, a trust, or any other legal instrument. It is the layer that legal documents have never covered: the reasoning. A will tells heirs what they're getting; it almost never tells them why, and that silence is what turns grief into a lawsuit.

We've mapped the existing landscape closely (see below) and found no product that combines owner-narrated, per-item reasoning with a self-serve app built specifically to prevent inheritance conflict, aimed at the two moments people actually need it: a terminal diagnosis, and proactive aging. That gap is the opportunity.

## The problem

Estate disputes overwhelmingly center on specific personal property and perceived fairness, not on liquid assets — this is well enough established that at least one company (Racine, below) has built its entire product around arbitrating exactly this. Wills and personal property memoranda assign items legally, but they almost never explain reasoning, and unexplained decisions are what siblings and relatives fill in with their own, usually worse, story. The two moments when someone is most motivated to fix this are also the moments they're least equipped to: a terminal diagnosis (time and energy are gone) and advanced age (no easy tool exists to do it gradually, over years, without a lawyer's office visit). Estate attorneys already recommend recording an explanatory video for exactly this reason — it's accepted, established advice. Nobody has turned it into a product.

## The competitive landscape (researched, not assumed)

| | Mechanism | Who explains | Delivery | Legal framing |
|---|---|---|---|---|
| **Racine** | Heirs anonymously mark preferences; an algorithm fairly divides items | Nobody — it's arbitration, not explanation | Self-serve app, $49 one-time + premium | Not legal, purely logistical |
| **Artifcts / GenerationStory** | Owner attaches photo/video/story to an object | The owner | Self-serve app, ~$89/yr | General legacy/insurance use case, not conflict-specific |
| **StoryCorps Legacy / Thru My Eyes** | Facilitated interview or professional videographer visit | The owner (terminally ill) | Nonprofit, human-facilitated, scheduled | Relational/emotional messages, not itemized property |
| **WillBox** | Owner records reasoning per item, addressed to a specific recipient | The owner | Self-serve app, available immediately | Not legal, but honestly framed as potential evidence of intent |

No entrant combines owner-side reasoning, an itemized-property focus, self-serve availability, and explicit conflict-prevention positioning. That is the white space, and it sits precisely between three validated, real, funded categories — a fundable position, not a speculative one.

One legal nuance worth building the product around rather than around: this is not a will, but courts have in some contested-probate cases accepted similar recordings as evidence of a decedent's actual intent. WillBox should say plainly "this doesn't replace your will" while being honest that it can still matter if things go wrong — that's a selling point, handled carefully, not a liability to hide.

## The solution

**Core loop, per item:** photo(s) → video, voice, or text explaining what it is, why it matters, and why this specific person is getting it → assign recipient(s) → optional emotional/thematic tag.

**Two modes, matched to the two real moments:**
- **"One Month" mode** — for a fresh terminal diagnosis. Fast, guided, and prioritized: the app helps identify the items most likely to cause conflict first (high sentimental or monetary value, multiple plausible claimants) so the highest-risk explanations get recorded first if time runs out. Usable one-handed from a couch or hospital bed.
- **"Someday" mode** — for anyone planning ahead. Low-pressure, one item at a time, gentle periodic prompts, meant to be filled in over months or years.

**The Reveal (release mechanism):** the single weakest point in every competitor we found is the trigger — a lone "legacy contact" a company simply trusts. WillBox instead uses a **multi-trustee quorum**: the user names two or more trustees; release requires a quorum (e.g., 2 of 3) to independently confirm, with a grace/contest window before anything unlocks, and an audit trail of who confirmed what and when. Release can be staged per item or per recipient rather than all-or-nothing.

**Never orphaned:** the other structural failure in this category is company mortality — a startup shutting down and taking someone's only recording of their mother's voice with it. WillBox continuously and automatically syncs an encrypted archive to storage the *user* owns (their own Google Drive/iCloud/Dropbox), on every edit, not as a manual "export" button people forget to press.

**Voice-first capture:** the primary input is talking, not typing — record a rough voice note, get a transcribed, lightly cleaned-up caption alongside the original audio (the original recording is always the primary artifact; the AI-assisted text is a convenience layer, never a replacement, and is always shown as editable and clearly derived).

## Target users

- **Primary:** people with a terminal or serious diagnosis, often helped by a family member
- **Secondary:** adults 65+ doing proactive legacy planning
- **Expansion:** multi-generational households collaboratively documenting family history and property together

## Technical requirements

**Client:** mobile-first (iOS + Android; a single cross-platform codebase — React Native or Flutter — is the pragmatic choice for a small team). Camera, microphone, and photo-library access; offline-first capture with background sync, since hospital and hospice connectivity is often poor. Accessibility is not an add-on here: large touch targets, voice as a first-class input path (not a fallback), legible type at low contrast sensitivity, full one-handed operation.

**Backend:**
- Client-side encrypted media storage for photo/video/audio — encrypted before it leaves the device, so WillBox itself cannot access raw content without the user's key
- Structured metadata store for items, recipients, stories, and tags
- A trustee/quorum release engine as an explicit state machine (Active → periodic check-in → missed check-in or trustee report → quorum confirmation window → released), fully audit-logged
- Notification service for check-ins, trustee confirmation requests, and reminders
- A transcription + light AI-cleanup pipeline for the voice-to-caption assist, always presented as a suggestion layered over the untouched original recording
- A continuous export/backup service pushing the user's encrypted archive to a cloud destination they control, running on a schedule, not on demand

**Security & compliance:**
- Client-side (or end-to-end) encryption is not optional given the sensitivity of the content — this is, functionally, deathbed material and family-wealth-adjacent disclosure
- SOC 2 Type II as a target within 12–18 months — required to be credible to any professional (attorney, hospice) referral partner
- An immutable, tamper-evident audit trail for the release event itself, since a disputing heir may later challenge whether a release was legitimate
- GDPR/CCPA-compliant handling, with a genuinely hard open question flagged honestly: a "right to delete" is awkward once the account-holder is deceased, so post-mortem data handling needs to be a choice the user makes explicitly at capture time, not a policy invented after the fact

**The hard problem — triggering, without WillBox certifying death itself:** WillBox should never claim to verify a death (liability and licensing risk it has no business taking on). The trustee-quorum model puts that judgment where it already legitimately sits — with named people who have standing, ideally including a non-family option such as an attorney or executor. A configurable check-in cadence is a secondary, opt-in safety net, not the primary trigger, specifically to avoid falsely triggering a release on a healthy user. A grace/contest window before an irreversible release exists to catch a false trigger before damage is done.

## Monetization

1. **Subscription (primary)** — a free tier (e.g., 10 items) to prove the value, paid tier for unlimited items, unlimited trustees, and the automatic cloud-export feature.
2. **One-time "legacy package"** — the terminal-diagnosis segment may not want to commit to an ongoing subscription decision at an overwhelming time; a one-time-purchase tier (Racine validates this pricing shape at $49) removes that friction.
3. **B2B / professional referral** — estate attorneys, financial advisors, and hospice/palliative care organizations already have this exact conversation with exactly this population. A referral or white-label program turns an otherwise-difficult outbound consumer acquisition problem into an inbound one, sourced through professionals already in the relationship.
4. **Family plan** — one subscription covering a household across generations, which also raises switching cost and retention because the whole family's material lives there, not just one person's.

## Go-to-market

**Wedge 1:** pilot with two or three hospice/palliative-care organizations and estate attorneys in a single metro area — the highest-intent, highest-empathy use case, sourced through partners who already have standing with these families, rather than trying to reach terminally ill people directly through paid acquisition.

**Wedge 2:** expand to proactive elder planning through financial advisors and elder-law attorneys, then to direct-to-consumer — notably, adult children buying it as a prompt or gift for aging parents, a distinct but very plausible buyer.

## Key risks

- **Emotional stakes.** This product is used at the worst moments in people's lives. A bad interaction here isn't an annoyance, it's a family in crisis — UX, tone, and support all carry more weight than in a typical consumer app.
- **Company-mortality trust gap.** Addressed structurally by continuous auto-export to user-owned storage, but it needs to be marketed as a core promise, not buried as a settings toggle.
- **Low usage frequency per individual.** Most people finish cataloging once and stop opening the app. Mitigated by the family plan (keeps the account alive across generations) and by "Someday" mode's deliberately incremental, ongoing design.
- **Legal ambiguity.** Requires real legal review to keep messaging consistent: not a will, but not legally irrelevant either — a fine line that has to be gotten right and kept consistent everywhere in the product.

## What it takes to build the pilot

A small team can reach a pilot-ready product: two mobile/backend engineers, one product designer, and a part-time legal advisor for the will/evidentiary-language review, over roughly 9–12 months to a launch with the first hospice/attorney partners. These are illustrative planning figures, not a funding ask — sized to validate retention and usage with real partner-sourced users before any larger raise.
