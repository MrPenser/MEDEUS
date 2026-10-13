# MEDEUS — HANDOFF STATE
**Date:** 2026-10-12 · **Version:** 2 · **Scope:** project initiation and user-accepted **requirements**, not approved runtime.

## Current exact truth
- `REPO=MrPenser/MEDEUS` (independent of ASTRADELIA core).
- `VISUAL_MASTER_LOCKED=true`. Original `MEDEUS_MASTER_VISUAL_V1_LOCKED.png`, SHA-256 `52244e15720d0dd40faa04914a44f8051a6466c166973b2609ea5d58f0e1de88`. **Binary asset not yet stored in repo**.
- `UX_CANON_LOCKED=true`: ONE SCENE / DESKTOP_FIRST_IMPLEMENTATION / MOBILE_DEFERRED / CENTRAL ORB / VOICE AND FRAMELESS TEXT / NO MENUS, BOXES, VISIBLE BUTTONS, OR USER ACCOUNTS / EXTERNAL HOSTED CHECKOUT.
- `PHOTON_ORIGIN=LAST_TOUCH_POINT`. `DIFFUSE_MIST_TO_SHARP_GLYPHS_TO_WORDS_TO_SENTENCES`. Language of spoken/typed query has priority over geo fallback.
- `CORE_STATE_COUNT=10`; behaviors detailed in `docs/canon/MEDEUS_CORE_STATE_MODEL_V1.md`. `USER_ACCEPTED_MOTION=FALSE`.
- `V4_VISUAL_REJECTED`, `V5_ROTATION_REJECTED`, `V6=CANDIDATE_NOT_USER_ACCEPTED`; never call ten states complete on the basis of ten labels.
- `VISUAL_TEXT_LOCALIZATION_CONFLICT=OPEN` for baked-in English/microphone cue in frozen PNG.
- `FORECAST_API_CONNECTED=false`, `HOSTED_CHECKOUT_CONNECTED=false`, `PUBLIC_HTTPS_DEPLOYED=false`.
- Pay per forecast (~USD 1) is research hypothesis, not verified price/cost/performance.
- `ASTRADELIA_FULL_CORE_READY` must **not** be inferred from MEDEUS demo. No core architecture or safety authority change authorized.

## Product medium clarification (latest user instruction)
- `PRODUCT_TYPE=WEBSITE`; `NATIVE_APP=OUT_OF_SCOPE`; `DESKTOP` means development/testing in a desktop web browser, not a desktop executable; `MOBILE` means responsive site in a phone browser, not a mobile app.
- The delivery target is a normal HTTPS website with one seamless scene.

## Current execution priority (latest user instruction)
- `ACTIVE_DEVELOPMENT_PLATFORM=DESKTOP` / `DESKTOP_MECHANICS_FIRST=true` / `MOBILE_WORK=DEFERRED_UNTIL_DESKTOP_SIGNOFF`.
- Override applies to **development/testing order**, not exact visual master, end-product responsive goal, 10 states, multilingual speech/text or external checkout.
- Work through all behavior and animation on desktop browser; collect explicit user acceptance. Do not treat desktop tests as mobile PASS.

## Read first after restart
1. `README.md`
2. `ROADMAP.md`
3. `docs/canon/MEDEUS_CANONICAL_SPEC_V1.md`
4. `docs/canon/MEDEUS_VISUAL_MASTER_LOCK_V1.md`
5. `docs/canon/MEDEUS_CORE_STATE_MODEL_V1.md`
6. `docs/decisions/MEDEUS_CANON_RECONCILIATION_2026-10-12.md`
7. `docs/architecture/MEDEUS_PRODUCT_BOUNDARY_V1.md`
8. `docs/history/MEDEUS_DECISION_JOURNAL_2026-10-12.md`
9. `docs/source-atlas/SOURCE_ATLAS.md`
10. Current relevant ASTRADELIA `MrPenser/genius-ai/docs/roadmap/ROADMAP.md`, plus global inheritance policy/registry from their present authoritative stores. Do not claim they are synced if they haven't been read/updated.

## Next action (do not silently skip)
- Publish and hash-readback approved PNG (binary custody); resolve text/localization conflict by user approval.
- Rebuild movement as 10 **qualitatively different**, clearly perceptible, low-memory device-friendly states; compare actual desktop browser interactions and recordings.
- Record true touch-coordinate smoke emission + word formation; test RU/EN/TR and browser speech; get user signoff.
- Only after UI signoff pursue forecast evidence and checkout.

## Closure / inheritance
`DESKTOP_IMPLEMENTATION_ACTIVE=true`; `DESKTOP_STATE_ACCEPTANCE=PENDING`; `MOBILE_PORT=DEFERRED`.

`TECHNICAL_PROTOTYPE=NOT_ACCEPTED`; `DOCUMENTATION_STAGE=IN_PROGRESS`; `VISUAL_ASSET_CUSTODY=PENDING`; `LIBRARY_SYNC=PENDING`; `GLOBAL_HANDOFF_REGISTRY_SYNC=PENDING`; `ATLAS_MIRROR_SYNC=PENDING`; `STAGE_STATUS=NOT_COMPLETE`.

Apply inherited sequence: `CLOSED_VERIFIED → HANDOFF → ROADMAP/JOURNAL → SOURCE_ATLAS → READBACK → COMPLETE`. For a new project, docs can be drafted ahead of technical closure but **no** technical `CLOSED_VERIFIED` is implied by this document.

## GitHub documentation readback — 2026-10-12
- Readback receipt: [MEDEUS_GITHUB_READBACK_2026-10-12.md](docs/verification/MEDEUS_GITHUB_READBACK_2026-10-12.md).
- `GITHUB_DOCUMENT_READBACK=PASS` for 10 published baseline documents; receipt now stored in GitHub.
- The global closure gate remains OPEN: `VISUAL_BINARY_CUSTODY=PENDING`, `USER_MOTION_SIGNOFF=PENDING`, `LIBRARY_AND_GLOBAL_REGISTRY_SYNC=PENDING`, `STAGE_STATUS=NOT_COMPLETE`.

## Inheritance alignment — global Rule of Inheritance v2.5 (2026-10-09)
**Mission / North Star:** build the exact user-approved one-screen, multilingual, no-signup MEDEUS experience, ultimately connecting only to evidence-verified scoped forecasts; do not alter ASTRADELIA core.
**Authority order (explicit):** current canonical declarations in this HANDOFF → independent verified evidence/readback → active canon/rules/specs → reproducible implementation/tests → historical demos → chat/model recollection. The explicit user-approved original visual and requirements are immutable constraints across these layers.
**Evidence origins:** user acceptance/rejection = `HUMAN`; connector GitHub file readback = `EXECUTION_READBACK` for documentation content only; design hypotheses and autogenerated code = `MODEL_DERIVED`; locally simulated responses and demo effects = `SYNTHETIC`; assistant-only grading = `SELF_EVALUATION`. These origins do not automatically establish product quality or real-world forecast truth.
**Prior-art / recall gate:** material prior art searched across this MEDEUS conversation, its v1–v6 existing specs and the established ASTRADELIA roadmap; the new repository **EXTENDS** the already-decided MEDEUS design, it does not invent an unrelated feature or new ASTRADELIA node. Discovery root: `docs/source-atlas/SOURCE_ATLAS.md` + `docs/history/MEDEUS_DECISION_JOURNAL_2026-10-12.md`. Future proposals must search existing designs and legacy wording (`ORAKUL`, `ORACL`, `MEDEUS`, `photonic text`, `core state`) before naming a new line.
**Execution constraints:** no account, checkout or model execution permission follows from a visual demo; any signed payments/authz must be bounded to public user requests; a verified upstream API contract is mandatory for external forecasts. `PREDICTION != AUTHORITY`; no fabricated readback.
**Failure/unknown state:** v4/v5 acceptance FAIL by user observation; v6 remains `NOT_USER_ACCEPTED` (not FAIL or PASS); exact image GitHub binary custody `NOT_RUN`; geo + voice/language and payments `NOT_CONNECTED`. Do not recast `NOT_RUN` as `PASS`.
**Handoff flags:** `HANDOFF_READY=true` (safe transfer in declared HOLD state, not technical completion); `CONTINUATION_READY=false` for executable/project-runtime continuation until binary and source custody are restored (documentation and non-authoritative design work may continue); `SELF_CONTAINED=false` (master binary/demo runtime not in repo); `FULLY_INHERITABLE=false`. This is not a `COMPLETE` stage.
**Next safe action:** import exact master binary with SHA-256 custody; resolve baked-in English conflict with user; demonstrate 10 genuinely distinct states and photon origin on DESKTOP first for user acceptance. Do not claim production forecasts or payment readiness.

## Lovable browser website workbench — 2026-10-12
- A Lovable project was created: `76dd8168-469d-4edb-88f6-f313be1c1de8`.
- Editor: https://lovable.dev/projects/76dd8168-469d-4edb-88f6-f313be1c1de8
- Preview: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app
- `WEBSITE_PROJECT_CREATED=true`; `LOVABLE_BUILD_FINISHED=NOT_YET_VERIFIED`; `APPROVED_MASTER_IMAGE_ATTACHED=false`; `USER_VISUAL_APPROVAL=OPEN`; `DEPLOYED_PUBLIC=false`.
- Agent instructed to avoid any substitute visual and leave a neutral asset-awaiting state pending exact `MEDEUS_MASTER_VISUAL_V1_LOCKED.png` import. Source SHA-256 remains `52244e15720d0dd40faa04914a44f8051a6466c166973b2609ea5d58f0e1de88`.
- Desktop-first *website*, not a native app. No production forecast/payment or functional state validation claimed.

## Confirmed Lovable asset upload — 2026-10-12
- Lovable lists `src/assets/MEDEUS_MASTER_VISUAL_V1_LOCKED.png.asset.json` with asset ID `ec7ee008-df26-448b-941e-b8b40b78b02e`, size `2849633` bytes, source label matching the approved file.
- Local SHA256 of exact master file verified `52244e15720d0dd40faa04914a44f8051a6466c166973b2609ea5d58f0e1de88`, local size `2849633`. Remote metadata size matches. **Remote binary checksum not independently checked**; site runtime checksum check is present in `src/lib/medeus/asset.ts`, but a successful client browser verification has not yet been observed.
- Lovable project `76dd8168-469d-4edb-88f6-f313be1c1de8` status `ready`, agent `finished`, latest code commit `da47c69d1a04cccc138553331593db11583f3e83`, no project error reported. `WEBSITE_PREVIEW_EXISTS=true`; `BROWSER_RENDER_AND_MOTION_SIGNOFF=PENDING`.
- Prior `APPROVED_MASTER_IMAGE_ATTACHED=false` is superseded by `MASTER_ASSET_UPLOAD_METADATA_PRESENT=true`; GitHub binary custody and ten-state visual acceptance are still independently `PENDING`.

## Screenshot-driven desktop website correction — 2026-10-12
- User screenshot (human observation) confirmed approved visual is loaded at Lovable preview, but letterbox black gutters and forbidden visible technical footer/state counter were present. It did **not** verify animated core behavior.
- Source inspection of prior Lovable code established DORMANT had no core motion and other modes primarily drew overlaid halos/rings; user acceptance remains `NOT_VERIFIED`.
- Proposed replacement committed in Lovable at `a06fd137bded5eb167ef2701f63e8e3ee0d9b7ab` ("Added six core modules"), containing `orb-field.ts` (WebGL internal-texture state-specific movement), `glyph-fog.ts` (touch-origin fog-to-glyph), `speech.ts`, updated `MedeusStage.tsx`, cleaned `src/routes/index.tsx`, and side-gutter CSS extension from the same source image.
- `LOVABLE_BUILD_AGENT=FINISHED` and project status `ready`, but agent admitted **NO build/typecheck/live-browser screenshot/effects QA**. Treat feature claims as `MODEL_DERIVED_IMPLEMENTATION_CANDIDATE`, not verified effect. `USER_ACCEPTED_TEN_STATES=FALSE`.
- Follow-up Lovable QA request was rejected by provider: `WORKSPACE_OUT_OF_CREDITS` (requires owner top-up to run more Lovable AI turns). No further app changes may be claimed from rejected request. Independently accessible git history/readback of files confirmed source changes, **not** runtime success.
- New desktop preview link unchanged: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app . **Next safe action:** user opens preview, hard refreshes, reports visible layout and internal animation or browser console errors; once credits available, run real desktop build + state-motion screenshot acceptance before declaring PASS.
- `DOCS_SYNC_THIS_HANDOFF=READBACK_PENDING`; `DESKTOP_INTERACTION_VERIFIED=FALSE`; `LOVABLE_FOLLOWUP_QA=BLOCKED_BY_CREDITS`; `STAGE_STATUS=NOT_COMPLETE`.

## Desktop website source now connected — 2026-10-12 (LATEST)
- `CODE_REPO=MrPenser/medeus-master-asset` (private GitHub linked directly to Lovable). Separate `MrPenser/MEDEUS` remains canonical documentation repo. **Do not edit docs repo when intending to patch website code.**
- User authorized GitHub connection. Four website source patches committed, latest `5ff9141515fc2a775d1b9f1bcbdf237dd4d7f59d`: full-screen edge feather/background fill, slower smoke-to-glyph 3.5+8.7 s, independent per-letter fade, stronger 10-state shader modes.
- Lovable independently read back latest exact commit on preview, `status=ready`. `WEBSITE_GITHUB_SYNC=PASS`, `SOURCE_EDITS_PRESENT=PASS`; **USER_VISUAL_ACCEPTANCE=NOT_YET_EVALUATED** for new build; earlier human FAIL applies to predecessor.
- Exact custody and source commit receipt: [GitHub site sync check](docs/verification/MEDEUS_SITE_GITHUB_SYNC_2026-10-12.md). Original PNG remains frozen, no source redraw.
- Next safe action: ask user to hard-refresh [Lovable desktop preview](https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app), evaluate full width, slow photon text, and different core behaviors. If not conforming, iterate in **code repo** via GitHub, not through credit-limited Lovable assistant.
- `DESKTOP_VISUAL_GATE=RECHECK_REQUIRED`, `TEN_STATE_HUMAN_SIGNOFF=PENDING`, `MOBILE_PORT=DEFERRED`, `PRODUCTION=NOT_AUTHORIZED`.

## Latest site checkpoint — GitHub connected & v7 desktop corrections synchronized (2026-10-12)
- Real Lovable source is in private `MrPenser/medeus-master-asset`; docs/roadmap remain here. **GitHub push → Lovable preview confirmed**.
- Updated site commits: `123b63e` CSS same-source peripheral fill; `5edd9ac` pixel-ratio-correct foreground feather; `96f3ce1` emitter 3500ms + materialization 8700ms with staged per-glyph condensation; `5ff9141` stronger ten distinct internal optical fields; `47fb4f0` opt-in motion tour (`?tour=1`, 4.6 seconds/state, hidden from normal UI).
- Verified via Lovable `get_project`: `latest_commit_sha=47fb4f04cecc47b728246cffd0e3daed26cf9f17`, `status=ready`, `agentFinished=true`. **Source-to-preview sync PASS**, separate from **human visual acceptance PENDING**.
- Review main desktop scene: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app
- Review all ten without normal UI chrome: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/?tour=1 (diagnostic-only state labels).
- `SOURCE_PATCH_SYNCHRONIZED=PASS`; `USER_FULL_WIDTH_VERDICT=PENDING`; `USER_GLYPH_MOTION_VERDICT=PENDING`; `USER_TEN_MOTION_VERDICT=PENDING`. Prior screenshot complaints remain the acceptance baseline until user rechecks this version. PNG master file unchanged; site still only visual demo, no forecast/payment integration.

## Latest visual directive — 2026-10-12: SHARP SEAMLESS COSMIC FIELD
- User verdict: `TEN_STATE_VISUAL_BEHAVIOR=PROVISIONALLY_ACCEPTED` ("состояния пока оставим такими — хорошо"); **do not further modify the 10-state animation behavior** without new instruction. This is a bounded visual signoff, not production/API acceptance.
- New hard requirement: `NO_BLURRED_PAGE_EDGES=true`, `ONE_CONTINUOUS_COSMIC_FIELD_FULL_VIEWPORT=true`, no black side columns, no visible framing.
- New desktop site implementation in private code repo: `src/lib/medeus/cosmic-field.ts` renders exclusively the SHA256-verified approved PNG as a continuous full-viewport panorama. Center `x=240..1208` original pixels retain original isotropic scale; only peripheral space is smoothly horizontally extended (a C1 edge mapping, NOT blur or duplicated cover). Master PNG itself remains unchanged.
- Code commits: `e0a5939f7023b611a06b9c661840db08c9432c31` (sharp panorama), `4b5e3fd4787a6f9f284273c87bc9a6c2cea5cd89` (website composition), `70cbd2a2c0d6636217797fed92a8ca4c45a808fc` (remove blurred styles).
- `SHARP_FULL_BLEED_CODE_WRITTEN=true`; `LATEST_GITHUB_COMMIT=70cbd2a2c0d6636217797fed92a8ca4c45a808fc`. Lovable preview sync and user rendering **must be separately checked** before `VISUAL_WIDTH_PASS`. `MOBILE=DEFERRED`.
- Preserve accepted core-state shaders (`orb-field.ts`) and existing photon timing/glyph code unchanged during this background repair.

## 2026-10-12 — Latest approved desktop display changes (source synced, visual signoff pending)
- User authorizes removal of bottom-left and bottom-right English microcopy, microphone placement BELOW materialized text, and faster photonic appearance.
- Normative six-point contract: [MEDEUS_DESKTOP_LAYOUT_REVISION_2026-10-12](docs/decisions/MEDEUS_DESKTOP_LAYOUT_REVISION_2026-10-12.md).
- Exact source master SHA-256 unchanged: `52244e15720d0dd40faa04914a44f8051a6466c166973b2609ea5d58f0e1de88`. A runtime-only original-pixel derivative suppresses baked texts/old microphone and moves its original artwork under dynamic answer, without changing source file. This explicitly resolves the previously OPEN visual-text preservation conflict for these user-approved regions only. Global multilingual translation of other baked-in English text remains NOT COMPLETE.
- Microphone image center original-coordinate `(723,973)`; response/input baseline `y=823`; click on relocated mic also initiates input.
- Emission `1400ms` (was `3500ms`); materialization `3900ms` (was `8700ms`) with per-letter reveal.
- `TEN_STATE_MOTION=PROVISIONALLY_ACCEPTED_AND_FROZEN`; `SHARP_FULL_WIDTH_COSMIC_FIELD=UNCHANGED`; `DESKTOP_ONLY_CURRENT`.
- Verified Lovable source-sync checkpoint `235fed4190b9558f43eeab302a7de492e421517e`; `SOURCE_IMPLEMENTED=true`; `USER_VISUAL_SIGNOFF=PENDING`; `FULL_STAGE_COMPLETION=FALSE`.

## Latest MEDEUS website patch — 2026-10-12
- `ACTIVE_SITE_SOURCE=MrPenser/medeus-master-asset` (private, Lovable GitHub sync). `ACTIVE_CANON=MrPenser/MEDEUS` (this repository).
- Latest user direction: mic triggers input, but photons ALWAYS emerge from sphere; remove baked orbit guide lines in presentation; safely enlarge living orb without colliding with logos/answer/other scene locations.
- `ORB_SCALE=1.23` applied to on-screen WebGL box and hit testing; shader definition `orb-field.ts` unchanged (blob `04fbf8a4432d55cdb964096b42949bb24a248643`). Master PNG remains SHA256 `52244e15720d0dd40faa04914a44f8051a6466c166973b2609ea5d58f0e1de88`.
- `MIC_TRIGGER != PHOTON_ORIGIN`; first mic contact sets orb-internal source; prior real orb contact reused; direct orb touch retains exact coordinates. In-memory orbital line suppression `orbit-cleanup.ts` uses verified source pixels only.
- `SITE_GITHUB_TO_LOVABLE_SYNC=PASS`: Lovable returned exact commit `6c92b87ca0dd69e8a1697e3e5e339871921b9f20`, ready=true; source readback confirmed edits.
- Canon detail: [MEDEUS_ORB_SOURCE_AND_SCALE_2026-10-12](docs/decisions/MEDEUS_ORB_SOURCE_AND_SCALE_2026-10-12.md).
- `LIVE_BROWSER_MOTION_AND_VISUAL_GATE=PENDING`; `ALL_ORBIT_TRACES_GONE=UNVERIFIED`; `HUMAN_VISUAL_APPROVAL=PENDING`; `PRODUCTION=NOT_AUTHORIZED`. Mobile remains DEFERRED.

## Orbit removal latest readback (2026-10-12)
- Refined orbit cleanup commit `a358bb34397eeb9505998abc663ff638a7e45161` **confirmed synchronized** in Lovable preview (`ready=true`); source mask only targets brighter thin external guide lines, avoiding previous smearing. May leave faint remnant guides: visual acceptance PENDING.
- Mic activation now stores source coordinate inside visual orb, never mic position. `orbScale=1.23`; all 10 original state shaders remain frozen (blob `04fbf8a4432d55cdb964096b42949bb24a248643`).
- Source and evidence in [ORB_SOURCE_AND_SCALE](docs/decisions/MEDEUS_ORB_SOURCE_AND_SCALE_2026-10-12.md). `LIVE_VISUAL_APPROVAL=PENDING`; `MOBILE_WORK=DEFERRED`.

## ACTIVE: Responsive mobile website port — 2026-10-12
- **Latest instruction supersedes old `MOBILE_DEFERRED`**: user specifically requests mobile adaptation. Not a native mobile app; same MEDEUS browser site, mobile-specific layout with original desktop unaffected.
- Private code repo `MrPenser/medeus-master-asset`; GitHub source commits: `3fa5457` mobile full-bleed source-derived cosmic painter, `de63c54` responsive stage and soft-keyboard/IME, `214a307` mobile safe viewport, `64c90f4` overscroll, `b0859a5` speech support check, `e4cb31a` mic fallback. Lovable last synced: `e4cb31a05e3f3238dce4f143035168a825f890cc` with `ready=true`.
- Mobile portrait 390x844: orb center ~(195,333), max diameter ~369px, reply baseline ~641, relocated mic center ~758. Full-bleed scene, no form boxes; tap sphere for native text, mic for voice where browser supports it. All photon origin coordinates remain orb-only.
- Approved-for-now ten-state shader **untouched** blob `04fbf8a4432d55cdb964096b42949bb24a248643`; source master PNG still hash `52244e15720d0dd40faa04914a44f8051a6466c166973b2609ea5d58f0e1de88`.
- Full contract: [MEDEUS_MOBILE_RESPONSIVE_PORT_2026-10-12](docs/decisions/MEDEUS_MOBILE_RESPONSIVE_PORT_2026-10-12.md).
- `MOBILE_SOURCE_AND_SYNC=PASS`; `MOBILE_PHYSICAL_DEVICE_QA=NOT_RUN`; `MOBILE_USER_APPROVAL=PENDING`; `DESKTOP_REGRESSION_QA=PENDING`; `PRODUCTION_FORECAST=NOT_CONNECTED`.

## Mobile typing gesture discoverability fix — 2026-10-12
- User reports that it is not evident how text entry is invoked on mobile. The actual gesture remains: **tap the orb for native keyboard**, **tap microphone for voice recognition** (keyboard fallback if unsupported), **Enter/Send submits**. This does not change the orb-only photon origin, ten states, or locked visual PNG.
- Website code (private `MrPenser/medeus-master-asset`): `src/components/medeus/MedeusStage.tsx` commit `6d8cd92654894b50fc70bb70190c6c8de00b6759`: small localized, frameless `КОСНИСЬ СФЕРЫ — НАПИШИ ВОПРОС` idle instruction on phone only, vanishes after valid interaction; native text visually stays above the visible mobile keyboard via VisualViewport.
- `src/styles.css` commit `fe54f1b6c90ad70dbc5aedccc8c0c9821d51e4e3`: subtle breathing hint, reduced-motion fallback. No visible form/button/menu; no changes to core-state GLSL shader.
- GitHub source readback confirms both commits; Lovable latest commit reports `fe54f1b6c90ad70dbc5aedccc8c0c9821d51e4e3` and `ready`, but `Lovable.read_file(src/styles.css)` initially still returned pre-style content. **Do not claim runtime hint animation fully synchronized until independent style readback.**
- `HUMAN_ON_DEVICE_KEYBOARD_OPEN=NOT_VERIFIED`; `MOBILE_UI_DISCOVERABILITY=FIX_IMPLEMENTED_PENDING_VISUAL_CHECK`; `PRODUCTION=NOT_AUTHORIZED`.

## Mobile keyboard focus + user-requested hint removal — 2026-10-12
- **Human report:** tapping the mobile sphere opens Android keyboard but focus immediately drops / keyboard fails to stay open. The previous on-screen text-entry hint is explicitly **unwanted** and must be removed in every language (not hidden behind preference state).
- **Root cause candidates from code inspection:** earlier mobile textarea used `pointerEvents:none`, 280×28 near the answer zone, and depended on `focus()` inside the parent's `onPointerDown`. A later native pointer completion / viewport resize could blur it.
- **Source fix in connected private website repo `MrPenser/medeus-master-asset`:** `db1e6b69be6dbf0a71edf7e1748379e4adee88e6` places transparent, circular native textarea directly over the sphere with actual touch events, relies on browser-native focus when user taps textarea, avoids rerendering/resizing the focused textarea when mobile keyboard changes viewport height; deletes the hint JSX, all hint state and copy. `bdcac9b52d01fdb7ae360b55b24e764b283c99e5` deletes hint CSS; `d4ecc140d3332f304b751883d4b1fe92b9a24341` makes focus hit-area cover orb circumference.
- **Continuing contract:** native IME/Russian/paste; Enter/Send submits; microphone invokes voice when supported; photon origin remains inside sphere; all 10 approved-for-now GLSL states unchanged (blob SHA `04fbf8a4432d55cdb964096b42949bb24a248643`).
- `CODE_PATCH_COMMITTED=true`; `HINT_REMOVED_IN_SOURCE=true`; `KEYBOARD_HOLD_USER_VERDICT=PENDING`; `ANDROID_PHYSICAL_BROWSER_TEST=NOT_RUN`. Do not claim the hardware failure resolved until the user tests the refreshed site.

## Mobile keyboard human acceptance — 2026-10-12
- User reports after the native textarea focus patch: **«Все ок. Работает»** in direct response to mobile keyboard focus/persistence verification.
- Bounded human verdict: `MOBILE_KEYBOARD_FOCUS_AND_TYPING=USER_PASS`; `MOBILE_HINT_REMOVAL=IMPLEMENTED`; `ACCEPTANCE_SOURCE=HUMAN`.
- Accepted working source checkpoint: `MrPenser/medeus-master-asset` at Lovable-synced commit `d4ecc140d3332f304b751883d4b1fe92b9a24341`. The native textarea holds focus during typing and the unwanted hint was removed.
- This **does not** close phone voice-recognition QA, landscape QA, exact appearance QA, full forecast API, payments or production readiness. `STAGE_STATUS=NOT_COMPLETE` remains.

## CURRENT HIGHEST-PRIORITY TRUTH — 2026-10-12 (supersedes earlier one-shot-product framing)
- User clarifies: **MEDEUS IS A FULL CONVERSATIONAL WEBSITE**, broadly ChatGPT-like in multi-turn interaction, but with ASTRADELIA "under the hood" via a future permissioned verified gateway. Avoid saying MEDEUS is just a $1 one-off prediction portal. Existing forecast/payment concepts become specific future capabilities, not product's only operation.
- Conversational canon [MEDEUS_CONVERSATIONAL_PRODUCT_CANON_V1](docs/architecture/MEDEUS_CONVERSATIONAL_PRODUCT_CANON_V1.md); long response / links / downloads [MEDEUS_LONG_RESPONSE_AND_ARTIFACTS_V1](docs/canon/MEDEUS_LONG_RESPONSE_AND_ARTIFACTS_V1.md).
- Current Lovable website is still demo-only, no general conversation engine, no ASTRADELIA API, no verified source/file output, no live payment. It **does** have user-confirmed mobile keyboard input and provisionally accepted ten state animations. Zero conventional app UI / no accounts remains.
- Latest separate user correction: **reduce photon blur only**; code `MrPenser/medeus-master-asset/src/lib/medeus/glyph-fog.ts` edit `c35d0e2a2a874d483e6a28ed8cb6760beb2253e6` changed only softer sprite/spread parameters, no ten-state GLSL, materialization duration or original raster change. Lovable provider readback `latest_commit_sha=c35d0e2a2a874d483e6a28ed8cb6760beb2253e6`, ready=true.
- `PRODUCT_CANON=CONVERSATIONAL_SITE_WITH_ASTRADELIA_FUTURE_BACKEND`; `UI_PHOTON_BLUR_PATCH=SYNCED`; `PHOTON_HUMAN_APPROVAL=PENDING`; `GENERAL_CHAT_AND_ASTRADELIA_INTEGRATION=NOT_IMPLEMENTED`; `STAGE_STATUS=NOT_COMPLETE`.

## 2026-10-12 — User-source greeting sound prepared (separate audio gate)
- User supplied a 10.16s AMR-NB tonal recording and requested quality processing of timing, timbre and tuning for MEDEUS website welcome.
- **Prepared, but not yet site-installed:** short ~4.5s (default) + extended ~7.4s greeting, processed original + gentle glass-pad re-synthesis around B-flat/D/F, mastering ~−17 LUFS, 48kHz/24-bit stereo, MP3 and WebM/Opus formats. The conversation delivers downloadable audio pack. No site binary upload claimed.
- Authority / checksum / integration gate: [MEDEUS_GREETING_SOUND_DESIGN_V1](docs/canon/MEDEUS_GREETING_SOUND_DESIGN_V1.md).
- Mobile browser autoplay before user interaction is unreliable or prohibited: implement one-time sound on first intentional orb/mic interaction (after user's approval), not autoplay claims. `AUDIO_RENDERED=PASS`; `SITE_AUDIO_UPLOAD=PENDING`; `CLIENT_PLAYBACK=PENDING`; `USER_SOUND_SIGNOFF=PENDING`.

## Latest sound work — 2026-10-12 / MUST NOT USE REJECTED V1
- Earlier `MEDEUS_GREETING_SOUND_DESIGN_V1` from AMR was explicitly **REJECTED** by user: thin/low-quality, wrong directional melody and no depth. No claim that v1 was approved. User authorized fully original replacement without source AMR.
- New active candidate `MEDEUS ASCENT V2`: user-requested only ascending notes B♭2, D3, F3, A3, C4, D4, F4; steady low fundamental; chime/resonant pad/stereo room. Generated independent stereo WAV 48 kHz, 7.4s; actual working code repo path `public/audio/medeus_ascent_deep_v2.wav`, Git blob `94d6bd1ee4d57b969d41ae7a93f19c3ae258e299`; main website code commits `7d7f07c2` asset, `90e5de9e` audition-only UI. Lovable source readback `latest_commit_sha=90e5de9e000060c6e5f61f298f1c68157facaf38`, ready=true.
- Opt-in audible link: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/?soundDemo=1 ; WAV: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/audio/medeus_ascent_deep_v2.wav
- [MEDEUS_GREETING_SOUND_DESIGN_V2_ASCENT](docs/canon/MEDEUS_GREETING_SOUND_DESIGN_V2_ASCENT.md) is the CURRENT AUDIO SPEC. Keep ordinary scene visually unchanged and **do not autoplay candidate** before explicit signoff.
- `SOUND_V2_ASSET_AND_PREVIEW=COMMITTED`; `SOURCE_SYNC=PASS`; `USER_SONIC_APPROVAL=PENDING`; `DEFAULT_WEBSITE_AUDIO_ENABLED=FALSE`.

## 2026-10-12 — USER PROVISIONAL SOUND REVIEW
- The user reviewed the newly synthesized MEDEUS ASCENT V2 sound and said: «для начала сойдет но это не окончательный».
- Exact adjudication: `V2_AS_WORKING_REFERENCE=PROVISIONAL_ACCEPTED`; `FINAL_AUDIO_SIGNOFF=false`; `FINAL_SOUND_DESIGN=PENDING`.
- The V2 ascending-only melodic direction and desire for genuine low-frequency depth remain design requirements, but timbre, harmonic sophistication, spatial depth and final sound identity are open to refinement. Do not mistake «сойдет» for full approval.
- Do not activate the provisional cue as a default/automatic welcome sound solely on this review. If a demo is used, label it as provisional and retain manual or first-gesture playback restrictions.

## 2026-10-12 — Spoken welcome phrase locked
- User requires: the very first phrase addressed to every visitor by the MEDEUS core is the translation of «Добро пожаловать!» into the visitor's language. For illustration: Russian «Добро пожаловать!», English “Welcome!”, Turkish “Hoş geldiniz!”.
- Spoken delivery must use **one androgynous core voice** (distinct from the greeting's provisional instrumental sound).
- One welcome per new visitor session; after browser-approved user gesture; first spoken phrase precedes other synthesized answers. Resolve language from user preference or browser locale, not IP alone. Provide honest fallback if a requested language is not available.
- Canonical source: `docs/canon/MEDEUS_CORE_VOICE_IDENTITY_V1.md`; requirement `LOCKED`. Real multilingual TTS/audio integration `NOT_IMPLEMENTED`; vocal identity approval `PENDING`; final welcome music `PENDING`.

## River selected as provisional timbral foundation — 2026-10-12
- Latest explicit user decision: **“Для MEDEUS наиболее близок голос River. Используй его как основу для дальнейших проб. Финального утверждения и разрешения на подключение к сайту пока нет.”**
- **Selection is directional, NOT a final voice approval**. Preferred source identity `ElevenLabs River`, exact provider voice ID `SAz9YHcvj6GT2YYXdXww`. Do not treat provider's plain voice as automatically satisfying MEDEUS's unique single-voice, androgynous, deep and luminous design.
- Prepare matched audition for first spoken welcome in RU `Добро пожаловать!`, EN `Welcome!`, TR `Hoş geldiniz!`; evaluate phonetic naturalness, pronunciation, low-mid body, top-end shimmer, pace, consonant clarity and *consistent identifiable voice across locales*.
- Provider sample synthesis jobs: RU `job_d82cb641-50fd-44d8-bdc0-506647a9777f`, EN `job_8be22026-5f56-4d2a-9c0b-bf76c4bb6bc7`, TR `job_6a35e8c0-49c4-4c86-9c55-67ada412ab39`. At last check RU was still `inprogress`; EN and TR newly submitted. A job ID is NOT an audio file; record real MP3 URLs only once jobs complete.
- Refine *subtly*: controlled formants/spectral envelope to increase depth without low-end mud, soft upper resonance, stable pitch and breath/consonants; no dual-speaker overlays, no heavy chorus, no full-track pitch shift that makes language unintelligible. All variants loudness-matched and checked on mobile and headphones.
- No GitHub website repository code, deploy, startup voice or autoplay change authorized by this provisional choice. Listening first, explicit final approval second, integration only after further distinct permission.
- `VOICE_BASE=RIVER_PROVISIONAL`; `MULTILINGUAL_VOICE_SAMPLES=PENDING`; `VOICE_TIMBRE_FINAL_APPROVAL=false`; `WEBSITE_VOICE_CONNECT_AUTHORIZED=false`; `SITE_AUDIO_UNCHANGED=true`.


## 2026-10-12 — User-authorized TEMPORARY site audio (latest)
- User explicitly requested temporary site connection for provisional River C3 voice direction **and** ASCENT V2 sonic welcome, not final voice signoff.
- Site source `MrPenser/medeus-master-asset`: `src/lib/medeus/temporary-greeting.ts` implements a one-time user-gesture-triggered 7.4s ASCENT V2 cue and locale-aware **native browser speech fallback** for «Добро пожаловать!»; it defers playback until user mic recognition ends to avoid echo and uses soft 0.82 speed / 0.95 relative pitch (NOT an exact 9Hz native TTS shift). It suppresses repeated cue starts, ducks music while speaking and honors one-per-session on successful greeting start.
- `src/components/medeus/MedeusStage.tsx` wires this temporary greeting to the existing orb/mic/text surface, and exposes actual `RIVER_C_MINUS_9HZ_SOFT_SLOW.mp3` in the existing `?soundDemo=1` audition panel only, never as arbitrary speech or a substitute for the localized welcome.
- **Critical epistemic boundary:** River C3 is a prerecorded English timbre **sample**, not a reusable multilingual River voice. A generic local SpeechSynthesis voice != River. Real River delivery of personalized Russian/multilingual welcome and chat replies remains **NOT CONNECTED** until authorized/licensed provider TTS can work. English River “Welcome!” provider job finished but provides a signed expiring URL, not a stable public asset. Russian and Turkish jobs have not yielded deployable clips. No fabricated capability claim.
- Existing working WAV `public/audio/medeus_ascent_deep_v2.wav` is reused; logo, locked PNG, 10 orb states and mobile text entry logic untouched. Default instrumental welcome now temporarily enabled after a gesture, including normal site rather than demo query; voice remains OS synth fallback.
- Lovable reported website `ready` and `latest_commit_sha=6ac3ee62310cfe0c03d8579d7840bc110c727f0d` and source readback for both modified stage and module; latest no-repeat-music fix `7c65a2abb801735b70052e2e2f77c8f70cab4213` awaiting separate readback.
- `TEMP_MUSICAL_GREETING_SOURCE_CONNECTED=true`, `BROWSER_TTS_FALLBACK_CONNECTED=true`, `RIVER_SAMPLE_IN_SITE_DEMO=true`, `RIVER_PERSONALIZED_TTS=false`, `BROWSER_ACTUAL_SPEAKER_TEST=NOT_RUN`, `FINAL_AUDIO_SIGNOFF=false`, `TEMP_AUDIO_USER_PERMISSION=true`. Operational full acceptance pending.
- Implementation decision detail: [MEDEUS_TEMP_AUDIO_WELCOME_2026-10-12](docs/decisions/MEDEUS_TEMP_AUDIO_WELCOME_2026-10-12.md).

## 2026-10-12 — Output follows input channel / long forecast override
- Latest user requirement: actual **microphone** question -> **spoken** short answer; actual **typed** question -> **written** short answer. **Long detailed forecast** -> **written only**, independently of input. After a voice-origin long forecast the core should first say a concise localized warning explaining that the full forecast is written for careful reading; if visitor asks why, explain again by their chosen input channel.
- Source code: `MrPenser/medeus-master-asset/src/lib/medeus/response-channel.ts` commit `738bb7a324d58a6d8230bc5cca79fa7b86a1c984`; source wiring `src/components/medeus/MedeusStage.tsx` commit `6b11df9c261fad182ecbc97b958386f1259f8bd9`. Unit tests in `src/lib/medeus/response-channel.test.ts` commit `317893c4d2278e3b3e437e92eb967ab55dcc135c`.
- Short demo microphone response now speaks native browser TTS, while typed answer uses original glyph-fog canvas with no per-reply TTS. Browser TTS is **NOT River C3**; fixed river sample only for timbre preview. If voice blocked, show readable text fallback; master PNG/ten core states unchanged.
- Because real ASTRADELIA/conversation backend does NOT yet return long forecast objects, `LONG_FORECAST_DATA_PIPELINE=NOT_IMPLEMENTED` and full scrollable long report UI also pending. `CHANNEL_ROUTING_CODE=IMPLEMENTED`, `BROWSER_SPEECH_RUNTIME_QA=PENDING`, `LONG_FORECAST_VOICE_NOTICE_POLICY=SPECIFIED`.
- Canon: [MEDEUS_RESPONSE_MODALITY_AND_LONG_FORECAST_V1](docs/canon/MEDEUS_RESPONSE_MODALITY_AND_LONG_FORECAST_V1.md).

## User visual concept — druid face (not a change order)
- User asked whether MEDEUS should become a huge druid-like face with eyes CLOSED on entrance, AWAKENING/opening eyes as conversation begins. This is **a concept for discussion, not explicit approval to replace the original locked sphere master**. Potential visual direction is an ageless androgynous face emerging from the live core. No master/shader/animation edits authorized until exact visual approval.

## 2026-10-12 — LIVING OCEAN SURFACE: first runnable trial, reversible
- User rejected druid/humanoid face; asked for living ocean-like fluid **surface** with the exact ten established subconscious/optical processes **underwater**. Explicit "запускай" authorized source deployment as a **trial**, not final visual lock.
- Site repo `MrPenser/medeus-master-asset`: `src/lib/medeus/orb-field.ts` non-destructive liquid membrane after existing `sampleState` passes (UV refraction, tangent slope, specular/fresnel edge sheen, single causal touch ring, damped continuous waves). WebGL1, original master remains SHA256-verified/untouched, 10 existing states unchanged; fixed shader reserved identifier via commit `b6650a40b3898b52dd2d61aa7c7bad729aeffed2`.
- `src/components/medeus/MedeusStage.tsx` liquid mode defaults ON. URL `?surface=classic` immediately reverts to unaltered classic shader; zero additional visible buttons and no redesign of mobile keyboard/microphone/phonon.
- QA: GitHub Actions `38291850459` **PASS** GLSL ES100 compilation, 10-state static gate, canonical Bun build, **6 unit tests PASS** (2 files). Initial failing run caught shader-reserved-word (product) and npm arborist installer failure (harness): both addressed. Latest QA workflow source commit `0a1675a1df7ec866116e4d3bf5c7c3d4908ca881`.
- Lovable project `76dd8168-469d-4edb-88f6-f313be1c1de8` status `ready`, source sync observed at `b6650a40...`.
- Liquid preview: `https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/`; classical fallback: same URL + `?surface=classic`.
- `CODE_LIVE_SYNC=PASS`; `GLSL_COMPILE=PASS`; `SITE_BUILD=PASS`; `AUTOMATED_TESTS=6_PASS`; `USER_VISUAL_SIGNOFF=PENDING`; `MOBILE_GPU_REAL_DEVICE_CHECK=PENDING`.
- Canon details [MEDEUS_LIVING_OCEAN_SURFACE_V1](docs/canon/MEDEUS_LIVING_OCEAN_SURFACE_V1.md). Do not claim physical fluid simulation or finalized visual appearance; this is a shader-based liquid optical membrane.


## 2026-10-12 — Liquid surface V1.1 hover and volumetric flow
- User-tested V1 result: click impact GOOD; idle looked like poor 2-D swinging, passive cursor hover had no response. DO NOT consider V1 user-approved.
- In private site repo `MrPenser/medeus-master-asset`, shader commit `a8990df7fd54262856b5aa8f41eaff38e5825421` changes ONLY the outer water membrane to asymmetrically flowing gyres, spherical optical normals and soft moving highlights, with a reversible hover lens/viscous contour tug.
- Stage commit `048b68ec734885f41ff2a49b1071e1dac81aac02` adds spring-damped cursor following (145ms) and fluid release (230ms), with no click required and no phone touch-input hijack. The click ripple survives unchanged.
- Verified original 10-state `sampleState` function is byte-identical (2656 characters) to pre-V1.1 version; immutable master and original vertex shader remain unchanged.
- GitHub Actions run `38293138422`: GLSL shader PASS; site Bun Vite build PASS; tests PASS. Lovable status `ready`, latest source commit matched `048b68ec...`. No visual/browser subjective acceptance claimed yet.
- Try fluid `https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/`; rollback via `?surface=classic`. `LIQUID_V1_1_READY_FOR_USER_QA=true`; `LIQUID_FINAL_VISUAL_APPROVAL=false`.
- Canon [MEDEUS_LIVING_OCEAN_SURFACE_V1](docs/canon/MEDEUS_LIVING_OCEAN_SURFACE_V1.md).

## 2026-10-12 — Living Ocean V1.2 deployed: outward-only contact, stronger hover, organic interiors
- User directly authorized implementation following visual QA: click ripple had appeared to reverse inward, cursor hover looked weak, and one state displayed repeated triangles converging on center. **V1.1 not accepted**.
- ROOT CAUSE: original liquid renderer still called legacy ten-state `sampleState` with inward LISTENING ring, angular 9-spoke RECEIVING_TEXT and radial PROCESSING compression, so changing FSM state altered the apparent water effect.
- CODE FIX in `MrPenser/medeus-master-asset`: `src/lib/medeus/orb-field.ts` commit `de8723a9b2d168c73f5f22310ac73803ce0fcb9f` adds separate `sampleOrganicState` for all ten original states ONLY in liquid mode, removing repetitive angular/radial geometry. The classic `sampleState` is preserved byte-for-byte behind `?surface=classic`. Surface `oceanHeight` now uses advected noise and a single outward-only positive Gaussian crest with monotonically increasing radius and time decay (no inward-return phase).
- `src/components/medeus/MedeusStage.tsx` commit `14503fb6d577f9b4fc7dcc158ed006e7024afc58` ensures true click-coordinate inheritance independent from state-entry transitions, increases hover deformation/refractive lens and faster viscoelastic pointer following. Does not change native mobile keyboard/mic event handling or immutable master pixels.
- Regression CI workflow commit `8fbec81e4bf4fcde927374971d615b12e0431d2f`, run `38295646821`: **GLSL ES100 PASS; ten organic state guards PASS; nonreversing ring guard PASS; Bun/Vite build PASS; existing tests PASS.** Product browser visual and mobile GPU smoothness NOT signed off.
- User-facing trial https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/ ; hard rollback to unchanged original classical optics with `?surface=classic`. Full [canon](docs/canon/MEDEUS_LIVING_OCEAN_SURFACE_V1.md).
- V1.2 `SOURCE_QA=PASS`; `BROWSER_VISUAL_APPROVAL=PENDING`; `FINAL_VISUAL_LOCK=FALSE`. Keep 10 existing core states; do not introduce a new state or AI character.


## 2026-10-13 — LIQUID V1.3 organic resting breath
- User explicitly APPROVED MEDEUS living liquid V1.2 ("хорошо оставляем"), but asked why the sphere does not breathe in idle. Cause: pre-V1.3 liquid surface shading/flow moved, but apparent orb contour remained constant radius.
- Implemented a distinct **intrinsic idle volume breath** (NOT an eleventh FSM state) with changing rhythm and amplitude. Private source `MrPenser/medeus-master-asset`: `src/lib/medeus/breathing.ts` latest commit `1ddd4a002f90bf4ac9eca46fe5ac2e038b747a12`; `src/lib/medeus/orb-field.ts` commit `f841dd41ea2f3e5d41fa85884cdfd4b6b6838293`; `src/components/medeus/MedeusStage.tsx` commit `8c2d1d946c5c10e11517a011d0316e0da0ade675`.
- Contour + UV refraction + spherical surface normals expand/contract by max ~2.6%, not simple texture brightness. Different successive cycles by noise modulation; disabled damping (30% amplitude) with reduced motion. Original master pixels, ten FSM states, liquid organic internals, hover and monotonic click ring unchanged.
- Reversible **V1.2 liquid** `?breath=off`, **original classic sphere** `?surface=classic`. V1.3 default `https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/`.
- Crucial product-vs-test distinction: first QA caught nearly repeating consecutive waves in NEW breath unit tests despite shader/build passing; changed breath phase variation rather than loosening test.
- Final CI workflow `8dafcf887478cca53f48b4a24df89dac59c2854c`, GitHub Actions run `38348454805`: `SHADER_GLSL_ES100=PASS`, `BUN_VITE_BUILD=PASS`, `ALL_AUTOMATED_TESTS=PASS`, `BREATH_NONREPETITION=PASS`. Visual/device sign-off remains PENDING (do not call it approved).
- Complete inheritance/canon: [MEDEUS_LIVING_OCEAN_SURFACE_V1](docs/canon/MEDEUS_LIVING_OCEAN_SURFACE_V1.md).


## 2026-10-13 — MEDEUS Living Ocean V1.4: internal micro-star lifecycles
- User approved V1.3 breathing ocean, then explicitly authorized sparse **submerged micro-stars** with autonomous asynchronous birth, slow random drift, dimming/death, rebirth elsewhere. No static particle wallpaper, no equal trajectories, no repeating triangles, no additional FSM state.
- Production code commits in private MrPenser/medeus-master-asset: src/lib/medeus/micro-stars.ts e7daf916538fc09415493e46c0a422125a26944e (14 independent stars with individualized 11–31s lives); src/lib/medeus/orb-field.ts 13796cbf704d4b7497fa58f17142c312afa32f5d (refracted under-liquid 256px lightmap, throttled 80ms, one texture sample, before outer sheen); src/components/medeus/MedeusStage.tsx 482289de7a91d076bf68587a0d32e8ca75b1ff3e (on by default, reversible ?stars=off); src/lib/medeus/micro-stars.test.ts 69ee4ebd5ba0b03ea835a6a4fb260c3ea85c31d3.
- Regression CI workflow commit ee2d658a9f9d4c490467d6e171ef207abf5dd244, Actions run **38349765671**: **shader GLSL ES100 PASS**, **site Bun/Vite build PASS**, **15/15 unit tests PASS** (includes five star tests). Previous code-only run 38349716794 also PASS 15/15.
- Lovable preview READY and synced: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/. Baseline V1.3 accepted and directly preserved with ?stars=off; ?surface=classic restores historical clean sphere; asset SHA and existing 10 states unchanged.
- Detailed canon: [MEDEUS_LIVING_OCEAN_SURFACE_V1](docs/canon/MEDEUS_LIVING_OCEAN_SURFACE_V1.md). **User acceptance V1.4 = PENDING; real mobile GPU visual QA = PENDING**, do not equate shader/build verification with visual acceptance.


## 2026-10-13 — Living Ocean V1.5 micro-star visibility recovery
- Real user review of V1.4: "пока ничего не видно" (micro-stars imperceptible). Explicitly rejected star visibility, despite prior production source + GLSL and unit tests passing. This is PRODUCT visual feedback, not a harness failure.
- ROOT CAUSE supported by code inspection: 256px lightmap stars used 0.55px cores, then accumulated painted alpha + shader alpha + idle gain 0.33; final luminous pixels could vanish against original busy orb.
- Direct source V1.5 remediation, private `MrPenser/medeus-master-asset`: `src/lib/medeus/micro-stars.ts` commit `39c565fe9851f71bcb98a8a4c04fb192fdf04c21` boosts individual halo/stellar light/core size with no count increase (14); idle gain 0.80; `src/lib/medeus/orb-field.ts` commit `6caf412ba9e6613decc741a3a65b994c318b2222` upgrades underwater emission compositing 2.6x, with same liquid refraction coordinates and pre-surface sheen layering.
- Added minimum visible core size / idle emissive gate to CI commit `4f5a1c2bfdb404c289fb678753eeea1c5c33990a`, and deterministic raster painter test in `src/lib/medeus/micro-stars.test.ts` commit `355de90d284cfa88feefe0413063e96f1f81e076`.
- CI run `38350464654`: `GLSL_ES100_PASS`, `BUN_VITE_BUILD_PASS`, `16/16_AUTOMATED_TESTS_PASS` (including 6 star tests). Lovable project `76dd8168-469d-4edb-88f6-f313be1c1de8` status ready, synced through `355de90d...`.
- Current preview: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/ ; accepted V1.3 baseline `?stars=off`; original classic `?surface=classic`.
- `USER_VISUAL_APPROVAL_V1_5=PENDING`: do not label stars as visually successful until the user observes them. Retain 10 FSM, one-way click, hover, V1.3 breathing, immutable master asset hash.
- Full details [MEDEUS_LIVING_OCEAN_SURFACE_V1](docs/canon/MEDEUS_LIVING_OCEAN_SURFACE_V1.md).


## 2026-10-13 — V1.6: reject star pox and protect approved default
- User rejected V1.5 with emphatic visual feedback "нет!!! это как оспа на теле океана". This is an explicit product VISUAL_FAIL; prior 16/16 unit-test success cannot override it.
- **Safety rollback first** in website repo MrPenser/medeus-master-asset: commit 5f8130572602cecc3fefc304a31931b0967f62e6 switched default micro-stars OFF and isolated future research to explicit ?stars=deep. Base URL now shows the accepted starless **living ocean V1.3** with breathing, hover attraction, and single outward-only touch ring unchanged.
- **Optional V1.6 deep experiment**, not for automatic display: micro-stars.ts commit 6b9ffac672635c784781c9294d61e225a17010a3 cuts 14->10, restricts apparent radial positions to deep inner volume, removes large bright skin-like cores/halos, dims cold/lilac light, retains random birth/life/death. orb-field.ts commit d4caa35f3f8202dba61c3bdafdc78314d5c7827a occludes near-shell and bright-cloud star light, composes at refracted underwater coordinates with much gentler emission. Stars deliberately remain invisible in default mode until user opts in.
- Star raster regression tests commit cf34cf7eb4b18b1a76174b03b0ab69e1c151479c, CI hard gates for no surface freckles and approved default commit 1def24ff3bd9b0487a6a4cfe1b6d45a13c092dc1. Final GitHub Actions run **38351217510** PASS GLSL ES100 + Bun/Vite production build + **16/16 unit tests**. This is automated source QA, **NOT visual acceptance of optional stars**. Stale earlier CI gates caused intermediate harness failures, corrected in final run.
- Approved BASE: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/ ; optional experimental STARS: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/?stars=deep ; legacy classic ?surface=classic.
- Detailed canon: [MEDEUS_LIVING_OCEAN_SURFACE_V1](docs/canon/MEDEUS_LIVING_OCEAN_SURFACE_V1.md). Do not enable surface spots by default again; USER_APPROVAL_STARS=NO; liquid base remains approved. All ten FSM states/master hashes frozen.


## 2026-10-13 — Living Ocean V1.7: Crystal-Clear Deep Flash Experiment
- User explicitly chose *редкие кристально чистые всполохи без тумана и мутностей* after direct visual rejection of surface star freckles/pox and invisible deep stars; then authorized autonomous implementation.
- **Approved root baseline unchanged:** https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/ ; breathing, cursor-magnetic water, one-way contact ripple and ten FSM states remain intact.
- New user-opt-in V1.7 https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/?light=crystal — ONE random interior short razor-sharp sliver per event (roughly every 5.5–11.5s apart), born then quickly extinguished; no smoke, haze, blobby halos, circular spots, glitter, star dust or repeating geometries.
- Website repo MrPenser/medeus-master-asset: source event controller src/lib/medeus/crystal-flashes.ts commit aa302d4c36ccbbe3dfeede5cce798e5f775de7a8; WebGL orb-field.ts commit f343872bbf081ed3c012404dc6b76cff9f3ed204 removes entirely the former star texture/raster/upload path and renders sharp GLSL clip within refracted pBelow + deep envelope; stage commit 5098877980aaa57d0ec765a7b36d9d5241059ac3 enables only ?light=crystal, old ?stars=deep removed.
- Test commit c27cef933bd2d4d99880d87866b175e340e4d127; CI workflow commit a1abc08480dc6f4a45c3bcc772586333fd79eebf; GitHub Actions run **38354547301** = WebGL1 GLSL compilation PASS, Bun/Vite production build PASS, **21/21 unit tests PASS**. Lovable readiness and source sync commit a1abc08480dc6f4a45c3bcc772586333fd79eebf checked.
- Full canon [MEDEUS_LIVING_OCEAN_SURFACE_V1](docs/canon/MEDEUS_LIVING_OCEAN_SURFACE_V1.md). **V1.7_VISUAL_USER_SIGNOFF=PENDING, not accepted**, while star particle approach REJECTED and V1.3 base ACCEPTED. Real-mobile GPU QA pending.


## 2026-10-13 — V1.8: NO ORBITS, NO CRYSTAL LINES
- **USER REJECTED** V1.7 crystal strokes and demanded removal of ALL orbital rings. No new stars, "cosmic fractures", particle spots or orbital guides may be silently promoted. Approved sphere = V1.3 living/breathing/hover/outward-click with ten original FSM states.
- Persistent visible rings are baked into the SHA256-frozen master panorama. The previous cleanup suppressed only high-contrast parts and sampled from other guide lines.
- Site repo source commits: `8676896b62f5170ccfe42249258ba121c75cf9cf` geometrically inpaints SIX ellipses + horizontal beam + four nodes in derived background; `6bc3c8b16b74f939c98e8be8ed3ac15d61c9928f` fixes crossing donor directions; `b6b45855403d3a43b716c981a4eb8d3204444a5d` cleans guide bead on fading orb rim; `8741bf9c87868d2ee3b288c6bc7f4914776c949b` removes crystal renderer; `99939e9a8b3a24e122d72ce79580294671e8a8c7` blocks old `?light=crystal` activation.
- New synthetic geometry/preservation tests `48c1acd28f30e24d46afcac892ce0f9f868c1d80`; QA gates `eb1e58e477c836fb61e3070f4d8ca066b2aaed23`. **FINAL CI `38355671430`: WebGL1 GLSL compile PASS, Bun/Vite build PASS, 24/24 tests PASS (6 test suites)**. Live Lovable exact source commit matches `b6b458...`, status ready.
- Preview (cleaned all viewports): https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/ . Locked master pixels unchanged; rendering uses transient in-memory derivative. User visual signoff on real site **PENDING**, do not claim already personally visually confirmed.
- Full [canon](docs/canon/MEDEUS_LIVING_OCEAN_SURFACE_V1.md).


## 2026-10-13 — V2 USER-APPROVED IMAGE SWITCH (CURRENT MASTER)
- The user approved the specific generated `космическое_ядро_medeus.png` and explicitly authorized replacement of the OLD site master, not an overlay or redraw. The approved 1672×941 RGB PNG has SHA256 `0dd41f6c5f1381136920480e23a3c9389604834a331e6b8bcfd4e22480f5b2ba`.
- Exact original bytes added to `MrPenser/medeus-master-asset/src/assets/MEDEUS_MASTER_VISUAL_V2_APPROVED.png` (binary commit `22907e60735ab79d58655fac795c084f8b31eaa5`; Git object SHA1 `71d82ce9c6c396d948921a31bb4b105a36db1222`); linked as default Vite-imported runtime SHA256-verified master by Lovable source commit `ddf90cc6263c6bbcee9c3432891234c1d4ec5074`.
- `asset.ts` sets V2 1672x941 and measured sphere (836,403) r224; `presentation.ts` becomes **pixel identity**, no old V1 orbit/caption/microphone masks or sprite stamp. New mic (836,810), answerY657, orbScale1. V1 immutable PNG + metadata remain historical backup without mutation. `cosmic-field.ts` adjusts wing-safety for planets.
- Existing ten core states, breathing, pointer drag, one-way ripple, mic/text interaction preserved. New V2 source custody + geometry unit suite added and workflow updated.
- **Verified CI GitHub Actions run `38359117816`: GLSL ES100 PASS, Bun/Vite production build PASS, **29/29 tests PASS** (7 files). Lovable preview ready, latest synced source commit `ddf90cc...`. Lovable agent browser-tested 1280x800 and 1440x1000 click/type/Enter result; planets and mic visible on those desktops.
- **NOT fully complete visually on every viewport:** tall desktop cosmic-field extension may generate faint streaks; mobile currently center-zooms sphere and can crop side planets. Separate responsive review required; do not silently claim mobile full-image pass. No production back-end forecast capability.
- Canonical authority now [V2 APPROVED SOURCE](docs/canon/MEDEUS_VISUAL_MASTER_V2_APPROVED_2026-10-13.md); V1 visual lock is HISTORICAL only for the current website. Preview https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/ . 
