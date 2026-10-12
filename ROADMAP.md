# MEDEUS — ROADMAP
**Baseline date:** 2026-10-12 · **Status:** `DESKTOP_UI_PROVISIONALLY_ACCEPTED / MOBILE_TYPING_USER_PASS / CONVERSATION_BACKEND_NOT_IMPLEMENTED / NOT_PRODUCTION`
**Identity:** one-page conversational WEBSITE, not a native app; desktop visual first, mobile responsive site now active with tested keyboard. ASTRADELIA-under-the-hood is a FUTURE server integration, not yet a live capability. The approved master graphic is frozen. MEDEUS is **not** a new ASTRADELIA core component.

Read in order: [PRODUCT CANON](docs/canon/MEDEUS_CANONICAL_SPEC_V1.md) → [EXACT VISUAL LOCK](docs/canon/MEDEUS_VISUAL_MASTER_LOCK_V1.md) → [10 CORE STATES](docs/canon/MEDEUS_CORE_STATE_MODEL_V1.md) → [RECONCILIATION](docs/decisions/MEDEUS_CANON_RECONCILIATION_2026-10-12.md) → [ASTRADELIA boundary](docs/architecture/MEDEUS_PRODUCT_BOUNDARY_V1.md) → [HANDOFF](HANDOFF_STATE.md).

## No false passes
- `VISUAL_MASTER_LOCKED` is **not** `ASSET_IN_GITHUB` or `ANIMATION_ACCEPTED`.
- `TEN_STATES_DESCRIBED` is **not** `TEN_STATES_VERIFIED`. v4/v5 rejected as static/single-spin; v6 still candidate.
- `PREVIEW_RENDERED` is **not** `LIVE_DEPLOYMENT` or `MOBILE_INTERACTION_PASS`.
- `SIMULATED_RESPONSE` is **not** `ASTRADELIA_VERIFIED_FORECAST`; `NO_ACCOUNTS` is not `NO_PAYMENT_SECURITY`.
- `DOCUMENT_WRITTEN` is not `STAGE_COMPLETE` until GitHub readback, custody, testing and relevant inheritance sync complete.

## Current priority — USER OVERRIDE 2026-10-12

**ACTIVE_PLATFORM=DESKTOP.** Latest explicit user instruction supersedes the earlier mobile-first *development sequence*: implement and visually approve all mechanics on a desktop browser first; MOBILE=DEFERRED until desktop signoff (not cancelled). Exact visual master, voice/no visible fields, ten distinct states, photon smoke from contact, languages, no accounts and external checkout stay unchanged.

**Desktop order:** exact master composition → qualitatively distinct 10 states (not a spinner) → contact-position photonic smoke and character-to-sentence construction → voice and frameless text → language handling → forecast contract/payment exploration. After desktop approval, port to mobile and verify it separately.

## Ordered delivery stages

| Stage | Target | Required evidence / acceptance | Initial status |
|---|---|---|---|
| **M0 — Canon + provenance** | Versioned roadmap, requirements, discrepancy log, handoff; freeze master reference hash | GitHub file readback; check all user constraints; SHA record | `IN_PROGRESS` |
| **M1 — Asset custody and exact design** | Import **exact approved** PNG as a managed binary; no regeneration | SHA-256 on source vs repository + delivery; pixel-perfect desktop composition; mobile crop after desktop signoff; resolve baked-English localization/embedded-mic conflict by approved plan | `BLOCKED_BY_ASSET_AND_VISUAL_TEXT_DECISION` |
| **M2 — Real core motion** | Implement all 10 distinct non-rotational states plus real transitions | 10 short desktop clips of actual state triggers; visibly distinct movements; mouse contacts in four orb quadrants; desktop fps/memory and user signoff; independent mobile tests later; explicit **user acceptance** | `REQUIRED_NOT_ACCEPTED` |
| **M3 — Photon materialization** | Local touch emits blurred smoke -> sharpens -> glyphs -> words -> complete sentence | Variable touch origin; blur monotonic toward target; no center fallback for touch; RU/EN/TR and non-Latin rendering; timing tests | `REQUIRED_UNVERIFIED` |
| **M4 — Input, accessibility, i18n** | Voice capture + frameless text; language of request; localization by locale/geo hint | Browser speech tests with permission denial; ru/en/tr+ script/direction QA; no visible form/buttons; reduced-motion and keyboard/screen-reader QA | `REQUIRED_UNVERIFIED` |
| **M5 — Verified forecast integration (shadow)** | Safe read-only interface with ASTRADELIA or scoped non-ASTRADELIA baseline | Validation contract and provenance, forecast cutoff, proper scoring / uncertainty, independ. verifier, forward frozen ledger; shadow before paid claims | `DEPENDENCY_GATED_NOT_CONNECTED` |
| **M6 — Anonymous external checkout** | Hosted provider redirect, pay-per-answer (~$1 hypothesis), no MEDEUS signup | Eligible merchant/jurisdiction check; webhook verification + idempotency + signed anon entitlement; refunds/tax/consent/abuse limits; unit economics | `NOT_CONNECTED` |
| **M7 — HTTPS desktop pilot, then mobile** | Live desktop one-screen implementation with voice/text and accessibility, followed by mobile adaptation | Real live link; independently validate desktop first, then mobile portrait/landscape and permissions/performance | `DESKTOP_FIRST / NOT_DEPLOYED` |
| **M8 — Evidence-backed public launch** | Stable truthful forecasts, monetization and documentation | Independent end-to-end readback, user signoff, legal/privacy checks, economic test, no unsupported accuracy claims | `NOT_AUTHORIZED` |

### First next execution
1. Resolve **M1 visual text localization / source asset custody** before declaring layout final.
2. Replace common spinner with genuinely different state-field mechanics; **demonstrate all 10** on DESKTOP and get user verdict before mobile work and collect user verdict.
3. Iterate M3 photon mist from tap coordinate with performance measurements.
4. Bring up DESKTOP HTTPS preview for *real* interaction before claiming user has an interactive demo.

## Research / economics
- Indicative **$1 forecast**, not a fixed commercial obligation. Run end-to-end unit cost and lawful payment availability experiments. Do not equate model API price with verified per-answer cost.
- Preserve model/evidence snapshot IDs, search ledger, frozen trial family/evaluation window/adaptation policy for claims. `BACKTEST_EDGE != VERIFIED_FORWARD_EDGE`.
- External Stripe/Visa-capable provider may require billing details; MEDEUS does not collect card details or require account.

## Controls & change authority
- Latest approved sequencing: `DESKTOP_FIRST / MOBILE_DEFERRED_UNTIL_DESKTOP_SIGNOFF`; mobile is not removed from the end-product scope.

- **Approved visual** and **explicit UX decisions** are locked; any change requires user signoff.
- **Animations v1-v6** are samples/evidence, not accepted master behavior. No automatic promotion.
- MEDEUS may reuse permitted public ASTRADELIA capabilities, but must not alter `MrPenser/genius-ai` gates, architecture or history.
- Inheritance/doc closure follows `CLOSED_VERIFIED → HANDOFF → ROADMAP/JOURNAL → SOURCE_ATLAS → READBACK → COMPLETE`. Not yet completed; all unverified stages remain OPEN.

## 2026-10-12 — Desktop live visual review reopened (HUMAN FAIL)
- Reported by user on current Lovable build: wide desktop retains empty side areas, glyphs fall/appear too abruptly, and perceptually distinct state reactions are fewer than 5 of required 10.
- Root cause recorded: image `object-contain` + insufficiently blended gutter; `glyph-fog.ts` reveals *all text* in a global ~0.9s opacity jump; 10 shader branches do not demonstrate 10 distinct visible behaviors.
- **Current visual acceptance:** `DESKTOP_FULLSCREEN=FAIL`, `PHOTON_TEXT_MOTION=FAIL`, `TEN_STATE_MOTION=FAIL`. No automatic promotion; original master stays frozen.
- Required precise corrections: [Desktop visual gate v2](docs/verification/MEDEUS_DESKTOP_VISUAL_ACCEPTANCE_GATE_V2_2026-10-12.md) and [Issue #1](https://github.com/MrPenser/MEDEUS/issues/1).
- `LOVABLE_WORKSPACE_OUT_OF_CREDITS`: this ROADMAP update is documentation only, **not** a live site patch. To continue implementation: restore Lovable build access, or connect site source to GitHub/direct editor.

## 2026-10-12 — USER OVERRIDE: states provisionally kept; full-bleed cosmic field MUST be sharp
- **Latest user decision:** ten state motions are acceptable *for now*; freeze their current code/visual behavior. This supersedes the previous visual-rejection task for the motion component only, **not** technical production readiness.
- **New issue:** no blurred/fuzzy frame at either side; artwork must read as ONE CONTINUOUS sharp cosmic field across the entire browser viewport, no black gutters or duplicated/scaled background.
- **Implementation:** only the verified locked master PNG is sampled. New `src/lib/medeus/cosmic-field.ts` implements a continuous, monotone horizontal extension of the outer space at C1 join boundaries. Logo, orb, core geometry, microphone and mid-scene stay isotropically scaled and correctly positioned. Original binary never changed.
- **Website source (private):** `MrPenser/medeus-master-asset` commits `e0a5939` (sharp cosmic field), `4b5e3fd` (site render), `70cbd2a` (deleted deprecated blur). Lovable project readback confirmed `latest_commit_sha=70cbd2a2c0d6636217797fed92a8ca4c45a808fc`, `ready`, and verified newly imported canvas source; `SOURCE_TO_PREVIEW_SYNC=PASS`.
- **Evidence limit:** `USER_FULL_VIEWPORT_SHARP_FIELD_SIGNOFF=PENDING` until user checks the current preview visually. Do not call the site finished on the strength of code readback. Old blur-based appearance is superseded.

## 2026-10-12 — Latest approved desktop display changes (source synced, visual signoff pending)
- User authorizes removal of bottom-left and bottom-right English microcopy, microphone placement BELOW materialized text, and faster photonic appearance.
- Normative six-point contract: [MEDEUS_DESKTOP_LAYOUT_REVISION_2026-10-12](docs/decisions/MEDEUS_DESKTOP_LAYOUT_REVISION_2026-10-12.md).
- Exact source master SHA-256 unchanged: `52244e15720d0dd40faa04914a44f8051a6466c166973b2609ea5d58f0e1de88`. A runtime-only original-pixel derivative suppresses baked texts/old microphone and moves its original artwork under dynamic answer, without changing source file. This explicitly resolves the previously OPEN visual-text preservation conflict for these user-approved regions only. Global multilingual translation of other baked-in English text remains NOT COMPLETE.
- Microphone image center original-coordinate `(723,973)`; response/input baseline `y=823`; click on relocated mic also initiates input.
- Emission `1400ms` (was `3500ms`); materialization `3900ms` (was `8700ms`) with per-letter reveal.
- `TEN_STATE_MOTION=PROVISIONALLY_ACCEPTED_AND_FROZEN`; `SHARP_FULL_WIDTH_COSMIC_FIELD=UNCHANGED`; `DESKTOP_ONLY_CURRENT`.
- Verified Lovable source-sync checkpoint `235fed4190b9558f43eeab302a7de492e421517e`; `SOURCE_IMPLEMENTED=true`; `USER_VISUAL_SIGNOFF=PENDING`; `FULL_STAGE_COMPLETION=FALSE`.

## 2026-10-12 — Orb/microphone origin separation and maximal safe enlargement
- User requires ALL emitted text/light to originate in the **orb**, even when mic was clicked. Contact with sphere uses exact orb touch; mic is an input trigger only, with fallback origin inside sphere. `MIC_COORDINATES_NEVER_AS_PHOTON_SOURCE`.
- User wants **orbit lines visually suppressed** and **living orb maximized safely** (not overlaid on title/answer/mic). Current bounded candidate is 1.23x radius, CSS/WebGL geometry only, state behaviors unchanged.
- Implemented in Lovable-connected working GitHub repo, synced commit `6c92b87ca0dd69e8a1697e3e5e339871921b9f20`. Original hash unchanged. Source-orbit cleanup uses derived runtime canvas, not altered PNG.
- Authority and QA: [MEDEUS_ORB_SOURCE_AND_SCALE_2026-10-12](docs/decisions/MEDEUS_ORB_SOURCE_AND_SCALE_2026-10-12.md).
- `SOURCE_SYNC=PASS`; `ORB_ORIGIN_LOGIC=PATCHED`; `ORBIT_REMOVAL_HUMAN_VISUAL_PASS=PENDING`; `ORB_SCALE_HUMAN_VISUAL_PASS=PENDING`. Do not modify the provisionally approved 10 state shaders.

## 2026-10-12 — Mobile website work explicitly activated by user
- Later explicit user request `Адаптируй для мобильного` supersedes previous `MOBILE_DEFERRED` execution order. **ONE WEBSITE, responsive mobile adaptation**, not a native app. Desktop stays preserved as regression baseline.
- Working source now branches by phone viewport and uses `mobile-field.ts` / `MedeusStage.tsx` for full-bleed portrait/landscape, centered orb, frameless native keyboard, microphone speech or keyboard fallback; emissions still originate from the orb.
- Detailed contract/evidence: [MEDEUS_MOBILE_RESPONSIVE_PORT_2026-10-12](docs/decisions/MEDEUS_MOBILE_RESPONSIVE_PORT_2026-10-12.md).
- `MOBILE_CODE_COMMITTED=true`; `LOVABLE_CODE_SYNC=PASS`; `MOBILE_HUMAN_VISUAL_SIGNOFF=PENDING`; `ANDROID_BROWSER_QA=PENDING`; `IOS_BROWSER_QA=PENDING`. Do not confuse preview READY with device pass.

## 2026-10-12 — mobile keyboard acceptance result
- **USER_PASS:** Android/mobile text-input gesture and keyboard persistence after `d4ecc140d3332f304b751883d4b1fe92b9a24341`; user confirms «Все ок. Работает».
- Locked outcome: remove previously unwanted hint, keep native orb input and unchanged 10-state mechanics. Avoid unnecessary redesign or re-opening this solved issue without new evidence.
- `MOBILE_KEYBOARD_GATE=CLOSED_VERIFIED_BY_USER` (bounded); `FULL_MOBILE_RELEASE_GATE=OPEN`, other features not inferred as PASS.

## 2026-10-12 — Conversational service authority and tuned photon blur (LATEST)
- **Product architecture:** ChatGPT-like *conversation mechanics*: multi-turn context, follow-ups, long readable responses, source links and downloadable files — expressed within the locked one-scene MEDEUS visual. Intelligent backend requires a verified governed ASTRADELIA gateway. This explicitly expands one-shot prediction-only UX without claiming actual ChatGPT feature/model equivalence.
- Required new roadmap gates: **C0** persistent multi-turn conversation/session service; **C1** authorized model/tool routing and GEMMAX/GUARDAR evidence bounds; **C2** long readable streaming answers; **C3** verified sources/files; **C4** mobile voice/text parity; **C5** verified forecast-specific capabilities; **C6** hosted checkout; **C7** launch QA.
- Normative spec: [MEDEUS_CONVERSATIONAL_PRODUCT_CANON_V1](docs/architecture/MEDEUS_CONVERSATIONAL_PRODUCT_CANON_V1.md) and [MEDEUS_LONG_RESPONSE_AND_ARTIFACTS_V1](docs/canon/MEDEUS_LONG_RESPONSE_AND_ARTIFACTS_V1.md).
- Photonic particles now **less blurry**, with smaller glow and sharper transit while maintaining progression; private site GitHub source `src/lib/medeus/glyph-fog.ts` at `c35d0e2a2a874d483e6a28ed8cb6760beb2253e6`, Lovable readback `ready`. Ten-state orb GLSL and timing unchanged.
- `PHOTON_BLUR_CODE_SYNC=PASS`, `PHOTON_BLUR_HUMAN_SIGNOFF=PENDING`, `CONVERSATIONAL_BACKEND=NOT_IMPLEMENTED`, `ASTRADELIA_GATEWAY=NOT_CONNECTED`, `PRODUCTION=NOT_AUTHORIZED`.

## 2026-10-12 — User-source greeting sound prepared (separate audio gate)
- User supplied a 10.16s AMR-NB tonal recording and requested quality processing of timing, timbre and tuning for MEDEUS website welcome.
- **Prepared, but not yet site-installed:** short ~4.5s (default) + extended ~7.4s greeting, processed original + gentle glass-pad re-synthesis around B-flat/D/F, mastering ~−17 LUFS, 48kHz/24-bit stereo, MP3 and WebM/Opus formats. The conversation delivers downloadable audio pack. No site binary upload claimed.
- Authority / checksum / integration gate: [MEDEUS_GREETING_SOUND_DESIGN_V1](docs/canon/MEDEUS_GREETING_SOUND_DESIGN_V1.md).
- Mobile browser autoplay before user interaction is unreliable or prohibited: implement one-time sound on first intentional orb/mic interaction (after user's approval), not autoplay claims. `AUDIO_RENDERED=PASS`; `SITE_AUDIO_UPLOAD=PENDING`; `CLIENT_PLAYBACK=PENDING`; `USER_SOUND_SIGNOFF=PENDING`.

## 2026-10-12 — Greeting Audio V1 REJECTED; ASCENT V2 synthesized
- Human review of earlier processed AMR: **quality unacceptable**, melodic pitches must move **strictly upward**, sound lacks depth. V1 **REJECTED/SUPERSEDED**. Do not promote or re-export V1.
- Synthesized entirely new ascending sonic logo, no original AMR audio reused: seven progressively higher notes **B♭2–D3–F3–A3–C4–D4–F4**, sub-B♭ foundation, chime + resonant pad + diffuse stereo. 7.4s, 48kHz stereo WAV (~1.42MB).
- Stored actual WAV in Lovable-connected website repository `MrPenser/medeus-master-asset/public/audio/medeus_ascent_deep_v2.wav` Git blob `94d6bd1ee4d57b969d41ae7a93f19c3ae258e299`. Preview-only listen/download gated behind `?soundDemo=1`; **normal site playback OFF** pending user signoff.
- Canon and links: [MEDEUS_GREETING_SOUND_DESIGN_V2_ASCENT](docs/canon/MEDEUS_GREETING_SOUND_DESIGN_V2_ASCENT.md). GitHub-to-Lovable source sync commit `90e5de9e000060c6e5f61f298f1c68157facaf38` verified. `NEW_AUDIO_RENDERED=PASS`; `BROWSER_PLAYBACK_NOT_INDEPENDENTLY_TESTED`; `AUDIO_HUMAN_APPROVAL=PENDING`; `PRODUCTION_SOUND=DISABLED`.

## 2026-10-12 — USER PROVISIONAL SOUND REVIEW
- The user reviewed the newly synthesized MEDEUS ASCENT V2 sound and said: «для начала сойдет но это не окончательный».
- Exact adjudication: `V2_AS_WORKING_REFERENCE=PROVISIONAL_ACCEPTED`; `FINAL_AUDIO_SIGNOFF=false`; `FINAL_SOUND_DESIGN=PENDING`.
- The V2 ascending-only melodic direction and desire for genuine low-frequency depth remain design requirements, but timbre, harmonic sophistication, spatial depth and final sound identity are open to refinement. Do not mistake «сойдет» for full approval.
- Do not activate the provisional cue as a default/automatic welcome sound solely on this review. If a demo is used, label it as provisional and retain manual or first-gesture playback restrictions.

## 2026-10-12 — Mandatory first phrase for every visitor
- **Latest user confirmation:** the first verbal phrase of MEDEUS for any visitor is the natural localized equivalent of **«Добро пожаловать!»**. First spoken sentence precedes ordinary response speech; one time per new session, not every turn. For RU/EN/TR illustrations: «Добро пожаловать!» / “Welcome!” / “Hoş geldiniz!”. The visitor's language, not a fixed Russian string or IP location, governs the real output.
- One **androgynous single core voice** must speak it, as specified in [CORE VOICE IDENTITY](docs/canon/MEDEUS_CORE_VOICE_IDENTITY_V1.md). Play only after allowed user gesture or audio consent; on-screen localization and transparent language fallback remain required.
- Separate test gates: localized text strings and language selection; real high-quality supported-language TTS using the same voice identity; audio-first-phrase ordering; session dedupe; Android/iOS browser autoplay/security; no interruption of user's question. `WELCOME_LANGUAGE_CANON=LOCKED`; `ALL_LANGUAGES_TTS=NOT_IMPLEMENTED`; `CORE_VOICE_PRESET=PENDING`; `NORMAL_SITE_GREETING_AUDIO=OFF`. 
