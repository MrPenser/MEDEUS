# MEDEUS — Conversational Product & ASTRADELIA Backend v1
**Date:** 2026-10-12 · **User framing:** "По сути подобие чата с тобой. Только под капотом астраделия."
**Status:** PRODUCT_VISION_CANON_LOCKED / CONVERSATION_BACKEND_NOT_IMPLEMENTED.

## Product meaning
MEDEUS is **a conversational one-page website**: a service with ChatGPT-like *interaction scope* (open questions, multi-turn clarifications, in-session context, long answers, references, artifacts), but with **the approved MEDEUS cosmic visual**, living core, frameless touch/voice interaction and ASTRADELIA-governed intelligence behind a *future authorized server gateway*. It is neither a standard chat bubble interface nor an exclusively one-shot fortune-telling / probability response service.

"Chat-like" describes conversational interaction, **not** a guarantee of equal model capabilities, AGI, unbounded knowledge, or access to ChatGPT proprietary model/runtime features. Those require their own integrations, tests and licensing.

## Chat contract
1. Every submitted user turn belongs to an anonymous `conversation_id` scoped to a browser session or privacy-appropriate persisted session. Preserve turn ordering and role distinctions, timestamps, language and actual provenance. No website sign-in is required; anonymous retention and restore must respect consent and server security.
2. A follow-up inherits resolved conversation context rather than treating every question as unrelated; explicit corrections supersede only relevant slots/claims. Avoid inventing memories or facts.
3. The first answer may arrive in short photonic form from the orb. Long answers use a **scrollable accessible reading mode** in the same scene, with progressive *paragraph* display and a persistent affordance for further input (voice/text). The ten core **motion states do not increase**: rendering/reading is an orthogonal UI substate.
4. Questions can be broad, analytical, creative or factual. **Specialized domains** (e.g. forecasting) require a scope-defined, verified capability, not a blanket assertion that ASTRADELIA already supports any domain.
5. Answers may include verifiable in-text references, external links and on-demand downloadable artifacts (PDF, DOCX, spreadsheet etc.) only after real sources/files exist. No fabricated citations or dead downloads.
6. Expose truthful state: composing, waiting for backend, partial output, error and retry/cancel. Do not display `LISTENING` without active recognition or `VERIFIED_FORECAST` without evidence.
7. No conventional chat message bubbles, account pages, menus or bulky submit forms. The living core and surrounding cosmic space remain the interaction canvas; keyboard/touch/voice accessibility has priority over purely hidden controls.
8. Very long sessions must support contextual compression or retrieval with evidence/provenance preservation and explicit retention limits, not silently discard active task constraints.

## System boundary and integration
`Browser MEDEUS scene ↔ authenticated/authorized MEDEUS server gateway ↔ permitted ASTRADELIA orchestration / verification services ↔ approved model and tools`.

- ASTRADELIA remains independent and retains `8 outer functional nodes + NOW/S_t` plus EVERION dynamic state-space, GEMMAX evidential memory, GUARDAR authority, and relevant routing/verification policies. MEDEUS is **not** a new ASTRADELIA architectural core node.
- A capable language model may be a **model behind ASTRADELIA's governed routing**, not a replacement for evidence or automatic production capability. The backend must not pretend "ASTRADELIA alone" performs capabilities not yet implemented.
- For real-world forecasts: source cutoff, evidence IDs/hashes, forecast-system snapshot, search ledger/trial family, uncertainty/calibration, and segmentation after material changes remain required. General factual answers require proportionate retrieval/verifiability.
- The website frontend must never directly hold external credentials, ASTRADELIA privileged tokens, payment secrets or execution authority. Public chat gateway needs rate limits and user/privacy/security safeguards.
- Payments may be requested for explicitly disclosed product features through **external hosted checkout**, no MEDEUS signup and no local card capture. Transparent usage policies and receipts still required.

## Existing behavior versus intended behavior
**Currently implemented/tested visually:** exact asset scene, some state motion, click/soft-keyboard text capture on user's phone, emitted **demo copy**.
**Not yet implemented:** a general language-conversation server, multi-turn persistence/retrieval, streamed long responses, real-source citations, source-grounded artifacts, ASTRADELIA service gateway, verified domain forecasting in site, paid checkout.
No demo chat response should be called an ASTRADELIA answer without actual protocol confirmation.

## Release milestones & verification
C0 — Multi-turn session API and explicit follow-up acceptance across 3+ turns.
C1 — Real model routing behind ASTRADELIA authority with traceable `system/model/version/evidence` rather than in-browser invented answers; shadow mode first.
C2 — Long answers (200/1000/3000 words), progressive reading, scroll preservation and follow-up.
C3 — Grounded links / research citations and on-demand actual file generation with downloads; copyright and privacy gates.
C4 — Voice/text parity and speech permissions on Android/iOS; keyboard and accessibility.
C5 — Domain-specific forecasts require independent forward evidence, not completion by generic chatting.
C6 — Payment/anonymous entitlements where commercially justified; law/provider and audit gates.
C7 — Real website pilot with full session retention, rate limiting, redaction, recovery, monitoring and user signoff.

**Explicit status:** `CONVERSATIONAL_PRODUCT_CANON=LOCKED`; `GENERAL_CHAT_BACKEND=NOT_CONNECTED`; `ASTRADELIA_LIVE_INTEGRATION=NOT_CONNECTED`; `USER_UI_MOBILE_KEYBOARD=PASS_FOR_TESTED_DEVICE`; `PRODUCTION=NOT_AUTHORIZED`.
