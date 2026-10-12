# MEDEUS — PRODUCT CANON v1
**Date:** 2026-10-12 · **Authority:** user-approved design requirements · **Status:** CANON_REQUIREMENTS_LOCKED / IMPLEMENTATION_UNVERIFIED.

## Product identity
MEDEUS is an independent public-facing single-screen interface (desktop-first active implementation, mobile compatibility later) to probabilistic intelligence. It may later consume verified ASTRADELIA services, but is **not a ninth core block, a replacement for NOW, or a production-capable AGI**.

## Hard user constraints
1. **Only the approved visual**: the original `MEDEUS_MASTER_VISUAL_V1_LOCKED.png` has SHA-256 `52244e15720d0dd40faa04914a44f8051a6466c166973b2609ea5d58f0e1de88`. No substitute image, redraw, recolor, different sphere, or design reinterpretation.
2. **Desktop-first implementation, cross-device final design**: the latest user instruction prioritizes desktop for all behavioral implementation/approval. Exact master composition, central orb and no distortion on desktop. Mobile full-bleed, central orb and aspect-preserving crop remain a deferred, independent gate after desktop signoff. No new ornamental panels.
3. **One scene, zero conventional UI**: no accounts, registration, sign-in, menus, navigation, visible input frames or buttons. The core itself is the contact surface. Text overlays remain frameless and integrated into the scene. Ordinary on-screen OS keyboard and microphone-permission prompts are exceptions outside product UI control.
4. **Voice or free-floating text**: tapping the core initiates a speech interaction where supported and after permission. Text input without a visible box must be available, including keyboard/accessibility fallback. Interactions cannot claim that listening began without microphone access.
5. **Language follows the user's actual question**: for an intelligible incoming spoken/typed question, the answer uses that language. Before any question, prefer explicit saved session preference (not account) then browser locale, then optional coarse geolocation hint with consent/privacy review, then English fallback. Country != language; a detected language cannot be inferred reliably from geography alone. Recognition accuracy and support must be declared, not faked.
6. **From touch, never arbitrary center**: emission origin is the recorded interaction coordinate on the orb (fallback for keyboard/voice triggers without touch must be explicitly defined and surfaced in tests). Diffuse lilac mist emerges there, gains focus during transit, forms individual glyphs, then words, then whole sentences. Not instant typed text.
7. **Ten qualitatively distinct states**: see [core-state model](MEDEUS_CORE_STATE_MODEL_V1.md). One rotating graphic at variable speed is a nonconforming implementation.
8. **No MEDEUS account requirement for payments**: any paid analysis, if later approved, redirects to a hosted third-party checkout (e.g. Stripe Checkout where supported), with explicit price and consent. No local card collection. External checkout may legally require customer/payment details; this does not authorize MEDEUS sign-up.
9. **Truthful forecasts only**: use evidence-based probabilities, uncertainty, calibration and scoped horizons when available. Do not present demo phrases or fabricated confidence as verified prediction. A \$1-per-forecast concept is **commercial hypothesis, not proven price or margin**.
10. **No auto-audio without a user gesture**; provide screen-reader and reduced-motion paths, with a silent animation fallback when input/microphone is not available.

## Non-negotiable boundaries
- Source graphic stays binary-identical; all animation layers are runtime-only and separately versioned.
- A static picture / spinning-center-only behavior != accepted live-core implementation.
- A clickable HTML download preview != tested production deployment.
- Animated prototype != functional multilingual ASR != forecast integration != payment completion.
- No required authentication != no backend security: anonymous payment entitlements must be server-side verifiable and rate-limited.
- No visual interface chrome != concealment of material commercial disclosures or privacy rights; present legally necessary information unobtrusively via accessible context interactions, with product design review.

## Approval & change control
**2026-10-12 sequencing override:** `DESKTOP_FIRST / MOBILE_DEFERRED_UNTIL_DESKTOP_APPROVAL`; this supersedes the old mobile-first build order but does not change the locked visual, interaction or final responsive requirements.

Visual master and user-stated UX requirements are **LOCKED**. Version v6's motion/art direction and all motion gates remain **CANDIDATE_NOT_USER_ACCEPTED**. Changes to locked requirements require explicit user approval; no cosmetic reinvention.
