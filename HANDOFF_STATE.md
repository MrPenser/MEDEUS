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


## 2026-10-13 — MEDEUS V3: exact approved image, no microphone captions
**Request and consent:** User visually approved a newly generated MEDEUS cosmic-vortex image after asking to remove the inscriptions above the microphone, then explicitly ordered "внедряй". The newly generated file from the current conversation is the *direct source* of V3, not a recreated artwork or an approximate text overlay.

**Immutable image identity:**
- Source: user-approved generated `космический_вихрь_medeus.png` (2026-10-13).
- Final GitHub site asset: `MrPenser/medeus-master-asset/src/assets/MEDEUS_MASTER_VISUAL_V3_NO_CAPTIONS.png`.
- Real original byte SHA256 = `9aac52baeac03d61a35ea9809d3580128952de1ae14d77f43c97a5fb7585c50d`, 2,218,455 bytes, PNG RGB 1672x941.
- Git blob SHA = `40620e1238b7c6ab2098c8f3c9d6c12e0d4899c6`; adding binary asset via Git-tree commit `f610cff5322b4c6e2445243e493f733e751aaa27`.
- `src/lib/medeus/asset.ts` commit `130f474b9e27d976db440ada7b9afeba5fe40d95`: renders V3 by default, runtime SHA256 verification switched to exact V3 hash, V1 and V2 retained as backups (V2 SHA256 `0dd41f6c5f1381136920480e23a3c9389604834a331e6b8bcfd4e22480f5b2ba`).
- `src/lib/medeus/presentation.ts` commit `93109509eb377b6bde6be75df209f05304914cba`: identity presentation, no old captions or masks, orb center 836,403 and radius 224; baked microphone center 836,810; full aspect 1672x941 maintained for desktop/mobile and WebGL.
- `src/lib/medeus/master-v2.test.ts` commit `79e3676ad9c73f83561a5c744514a85903697b31`: verified V3 full binary SHA256 + IHDR dimensions, V2 backup unchanged, original 10-state FSM, all UI target bounds.
- `.github/workflows/medeus-liquid-orb-qa.yml` commit `1120511e783818fb2731874d6a4740ed74a0d144`: asserts exact V3 PNG bytes, V2 backup bytes, WebGL shader, ten FSM state guards and site build.

**Verification:** GitHub Actions run 38362174590 PASS shader + site + 29/29 tests; Lovable binary V3 source present, preview linked above. USER_BROWSER_VISUAL_SIGNOFF=PENDING.


## 2026-10-13 — V3 independent living microphone: hover AND click
- User directive: microphone planet must respond **on mouse hover and on physical press**, matching approved big liquid sphere style, with **independent** optical behavior; do not modify frozen V3 master.
- Completed in website repo MrPenser/medeus-master-asset: `src/lib/medeus/mic-field.ts` commits `80b96f589f2d96d486f9284251359ce8a75de7ff` and `fa05d243c253b20f4f1ae8f6999fc13defcf3c3d` implement original-V3-sampled liquid refraction and localized ice specular on pointer hover, one decaying outward-only contact crest on mic. No stars, circles, extra decorative orbits, or idle appearance change.
- `src/lib/medeus/mic-motion.ts` commit `4e26bf22e458e592ca2432b9d3f32e1f192debe2`: separate normalized mic-local hover position, same 95 ms follow/180 ms release as large sphere. `src/components/medeus/MedeusStage.tsx` commit `aceec6a5cb2a0bcd1cfdebeaae338cb4be8317e2`: mic WebGL canvas, independent pointer target / ripple timestamp, mobile+desktop scaled placement, mic down continues existing voice capture and never triggers fake big-sphere ripple. Original sphere remains unchanged.
- Tests `src/lib/medeus/mic-motion.test.ts` commit `adb18f7fd468301f1b2cf24aa2dd72e4f22be60c`; CI workflow commits `7b918e608e2bb04040bb1639d31db2fc941c0931`, `93e420a24c609fa92e77ad02071a2ef96acde5e2` (corrected a *harness* regex extraction bug, no product defect). Run **38364507391**: two shaders compile GLSL ES100 PASS, Bun/Vite production build PASS, **34/34 automated tests PASS** across 8 suites; existing V3 exact SHA256 and 10-state guards preserved. Lovable Ready + live-source read probes verified.
- CANON: [MEDEUS_V3_MICROPHONE_LIQUID_RESPONSE.md](docs/canon/MEDEUS_V3_MICROPHONE_LIQUID_RESPONSE.md). Official V3 frozen image SHA256: `9aac52baeac03d61a35ea9809d3580128952de1ae14d77f43c97a5fb7585c50d`. **MIC_INTERACTION_VISUAL_APPROVAL=PENDING** (no actual user-browser signoff yet). Preview: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/


## 2026-10-13 — V3.1 Live Inner-Ocean Core (CODE MOTION ONLY)
- Direct user visual bug: "сфера. дышит но внутри какбудто зияет огромная статичная дыра", with explicit prohibition on image generation/overlays: "**не рисуй мне здесь больше ... только вноси в код изменения движений**". This overrides any prior suggested artwork/effects. No master PNG changes.
- Root cause: V3 baked near-white static inner source and modest existing inner UV motion; breath moves membrane/edge, not enough genuine material across the central image aperture. Mathematical check on SHA-matching original V3 shows near-white center; old interior was effectively stationary.
- Actual site source: `src/lib/medeus/orb-field.ts` commit `087781f7417e2184e0bde0308704ab92f03f76b2` adds non-periodic 2-D advected internal UV current and locally feathered optical source-pixel turnover from neighboring VERIFIED V3 material; no synthetic painted glow/dots, no radial orbital or repeated geometry. Default enabled in `MedeusStage.tsx` commit `bdf56f095432b8a481322ae45a3d292c2b2ffe8c`, fully reversible **?core=off** to previous static V3 center with all other visuals preserved. Do NOT regenerate any image.
- `src/lib/medeus/core-flow.test.ts` commit `0c792f4512f2bb489efaf9fd45bb3ea8cebdd8ec`; CI update `d1afdd562ff1a0a98b7d701f7da340a02d5105a7`. GitHub Actions run **38366441437**, shader+site both PASS, WebGL1 GLSL compile PASS, Vite build PASS, **38/38 tests PASS** (9 suites). Lovable latest synced and Ready at `d1afdd562ff1a0a98b7d701f7da340a02d5105a7`.
- Explicitly preserve immutable V3 master SHA256 `9aac52baeac03d61a35ea9809d3580128952de1ae14d77f43c97a5fb7585c50d`, approved large sphere breath + hover + touch waves, approved independent microphone hover/press, 10 states, voice/text, planet placement and panorama. No image editing.
- Detail: [MEDEUS_V3_LIVING_INNER_CORE_FLOW.md](docs/canon/MEDEUS_V3_LIVING_INNER_CORE_FLOW.md). Root: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/ ; comparison: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/?core=off
- Status: SOURCE_QA=PASS; LOVABLE_SYNC=VERIFIED; **USER_VISUAL_ACCEPTANCE=PENDING** (cannot prove perceived living depth without viewing user browser).


## 2026-10-13 — Handoff V3.2: whole-sphere multi-axis flow not yet visually accepted
- Transfer authorized by user command "пепредача" (interpreted as "передача"). Canonical and self-contained scope handoff: [MEDEUS_V3_2_TRANSFER_2026-10-13.md](docs/canon/MEDEUS_V3_2_TRANSFER_2026-10-13.md).
- **Authoritative current website HEAD** `MrPenser/medeus-master-asset@` `8130f4aa59188f533fb8c4879fad3fcfe1bfb29b`, same Lovable mirrored HEAD at project `76dd8168-469d-4edb-88f6-f313be1c1de8` (Ready). Latest GitHub Actions run **38367445856** both GLSL shader and site build PASS, **38/38 tests PASS** (9 suites). No source changes required for handoff.
- Active V3.2 in `src/lib/medeus/orb-field.ts`: `uVolumeFlow` + global noise-advection `oceanVolumeCurrent` + two genuine V3 texture transport layers `oceanLayerA/B`, off-center source sampling bounds and source-color correction (NOT central radius mask). `MedeusStage.tsx` turns it on by default, reversible with `?volume=off` or `?core=off`.
- **USER LATEST DIRECTION OPEN / NOT PROMOTED:** eliminate any remaining "сфинктер космоса"/aperture, motion across WHOLE SPHERE, natural movement around **MULTIPLE DISTINCT INVISIBLE TILTED ROTATION AXES** (axes never drawn). Current V3.2 noise/shear advection is not a true multi-axis rotational/volumetric field. `MULTI_AXIS_MOTION=REQUIRED_NOT_IMPLEMENTED`, `VISUAL_APPROVAL=NOT_GRANTED`, `STAGE_COMPLETE=FALSE`. Prior V3.1 center-only repair was explicitly rejected. Do not claim source-test PASS equals user visual PASS.
- **No new images** (explicit user prohibition: "не рисуй мне здесь больше ... только вноси в код изменения движений"). V3 locked PNG `MEDEUS_MASTER_VISUAL_V3_NO_CAPTIONS.png` SHA256 `9aac52baeac03d61a35ea9809d3580128952de1ae14d77f43c97a5fb7585c50d`; V1/V2 archived; approved liquid breath/hover/outward click, mic independently hover/press with voice capture, desktop/mobile, 10 FSM, classic `?surface=classic` intact.
- **Next action (once resumed):** source-edit volumetric multi-axis global advection, avoid visible orbits, dark wells, radial masks, stars, haze and synthetic glow. Check shader/WebGL1 compile, Vite build, unit/CI gates, user-browser visual acceptance and rollback. Do not edit image or mic functions.
- `HANDOFF_READY=TRUE`, `CONTINUATION_READY=TRUE`, `USER_VISUAL_SIGNOFF=FALSE`, `STAGE_STATUS=NOT_COMPLETE`.


## 2026-10-13 — V3.3: gentle whole-sphere three-axis rotation (LATEST SOURCE)
- User requested reduced shader strength/no fast streams plus subtle irregular rotation of the **entire sphere** around its own invisible axes. Recalled V3.2 handoff; disposition `EXTEND` (not a new image or another state).
- Site source `MrPenser/medeus-master-asset`: GLSL `src/lib/medeus/orb-field.ts` commit `55ee406e90043b071f354772aba4eb2cd0147042`, 3 independent tilted 3-D Rodrigues sampling axes, slower subdued V3 donor flow; preserved mic, 10 FSM, approved V3 exact SHA256 and all rollbacks. Tests `52a8398ebd58a3ed6d7953d1d8e54212cf369868`; QA workflow `df25d815f3c931a64ad061ecec50bf1e517aabdd`.
- GitHub website HEAD at source CI: `df25d815f3c931a64ad061ecec50bf1e517aabdd`. Actions run `38370699038`: shader GLSL ES100 PASS, site build PASS, 38/38 unit tests PASS (9 suites). This is **source verification**, not user visual acceptance.
- Full scope/verification and continuation: [MEDEUS V3.3 gentle multi-axis rotation](docs/canon/MEDEUS_V3_3_GENTLE_MULTI_AXIS_ROTATION.md). Previous V3.2 transfer remains historical for the pre-rotation checkpoint.
- `MULTI_AXIS_SOURCE=IMPLEMENTED`, `SOURCE_QA=PASS`, `USER_VISUAL_SIGNOFF=PENDING`, `MOBILE_REAL_GPU_CHECK=PENDING`, `STAGE_COMPLETE=FALSE`. Next: browser 20–40s rest/hover/click visual check against excessive speed, edge artifacts and prior central iris. Preview: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/ .

## 2026-10-13 — V3.4 USER CORRECTION: planet spin visible by source geometry; central iris source repair
- User explicitly rejected V3.3: "мы вернулись к дыре. вращения сферы как планеты- нет! шецдер не виден". This is **USER_VISUAL_FAIL** for V3.3 regardless of earlier 38/38 tests. Decision: `EXTEND` V3.2, `SUPERSEDE` only V3.3 optical movement.
- Implemented V3.4 in website `MrPenser/medeus-master-asset`: `src/lib/medeus/orb-field.ts` commit `cd4fae1814be5b633b92e948349796fe6b66b44f` fixes V3.3 attenuation of projected 3D three-axis source-coordinate spin, keeps angular rates modest, noise/current extremely weak, adds 3 verified-source moving donor layers and color-driven white plateau correction rather than static circular core. **No image generation**.
- Source tests updated `05aa2a1829b90e91379016242fa488344ac06a6f`, includes numerical 20s displacement bounds at center and off-center sphere coordinates; CI harness `8e9a36c5f82ae8745b5f9c0a872f80ca46f8104b` updated.
- GitHub site HEAD `8e9a36c5f82ae8745b5f9c0a872f80ca46f8104b`. Actions run `38372328909`: `SOURCE_QA=PASS`, GLSL ES100 shader / Vite site / 38/38 tests PASS.
- V3 PNG SHA256 `9aac52baeac03d61a35ea9809d3580128952de1ae14d77f43c97a5fb7585c50d` immutable. Microphone, 10 FSM, shell, voice, click and breath unchanged. Rollbacks `?volume=off`, `?core=off`, `?surface=classic` preserved.
- Detailed record: [MEDEUS V3.4 visual fail repair](docs/canon/MEDEUS_V3_4_NO_IRIS_VISIBLE_PLANET_SPIN.md). Preview: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/ .
- **Hard gate**: `V3_4_USER_VISUAL_ACCEPTANCE=PENDING`, `MOBILE_GPU_QA=PENDING`, `STAGE_COMPLETE=FALSE`. GitHub source PASS does not substitute for actual perceived motion/no hole, and Lovable commit mirror is independently checked.


## 2026-10-13 — V3.5: approved rotation, native texture restored without wet shader
- Latest user decision: **"вращение норм"** => preserve V3.4 three-axis sphere motion. **"шейдер убери -он плох. верни глубину тестуру прежгней сферы только без дыры"** => remove extra wet presentation and restore original approved V3 image texture/depth while maintaining only source-driven color repair of bright/flat regions. Authorization "делай. сама". Classification `EXTEND`, no extra generated image.
- Working website repo `MrPenser/medeus-master-asset` HEAD `d1859f5284bad8eadc7c8b533d5bb0584bc2cbe9`: `orb-field.ts` commit `de9f1d880a1e9c0da444ad0fe49d15b01dce4963` restores predominantly pristine V3 pixels; keeps entire V3.4 3-axis rotation untouched; removes default water specular, resting noise and wide donor texture blending; retains only restrained hover/click optical feedback; repairs near-white overexposed flat material using bounded 3 donor neighborhoods from original V3, without any radial center mask. **Do not remove WebGL coordinate sampling — it is needed for accepted spin.**
- Tests `d1859f5284bad8eadc7c8b533d5bb0584bc2cbe9`, workflow `5e1bb558c0a966ba58643f516ac09cc5c805726f`. GitHub Actions **38373966682**: WebGL GLSL ES100 shader and microphone shader PASS; Vite build PASS, **39/39 tests PASS** (9 suites).
- Lovable project `76dd8168-469d-4edb-88f6-f313be1c1de8` `ready` at independently verified matching website commit `d1859f5284bad8eadc7c8b533d5bb0584bc2cbe9`. Preview https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/ . No website PNG, microphone, ten FSM states or voice/text infrastructure changed.
- Canonical detailed record: [MEDEUS V3.5 native texture and depth without wet shader](docs/canon/MEDEUS_V3_5_NATIVE_DEPTH_NO_WET_SHADING.md). Rollbacks `?volume=off`, `?core=off`, `?surface=classic` intact. Original V3 master SHA256 `9aac52baeac03d61a35ea9809d3580128952de1ae14d77f43c97a5fb7585c50d`.
- `SOURCE_QA=PASS`, `LOVABLE_SYNC=PASS`, `V3_4_SPIN_USER_APPROVED=TRUE`, `V3_5_TEXTURE_AND_NO_HOLE_VISUAL_SIGNOFF=PENDING`, `MOBILE_REAL_GPU_QA=PENDING`, `STAGE_COMPLETE=FALSE`. Do not claim visual success from source QA; require user inspection on desktop/mobile at rest, hover and click.


## 2026-10-13 — V3.6 no rotation, restored native depth, gentle breath
- User supplied screenshot showing prominent internal striping during V3.5 rotation, explicitly rejected the rotational effect and requested **no rotation**, preservation of realistic original depth, and **less intense breathing**. Explicit approval for source edits: "меняй сама разрешаю".
- `recall&` disposition `EXTEND` on the V3.5 native-source implementation; V3.4 spin is now **SUPERSEDED_BY_LATEST_USER_DIRECTION** even though it had formerly been accepted. Do not revive 3-D axes, rotated hemisphere UV or planar flow when continuing.
- Website `MrPenser/medeus-master-asset`: `orb-field.ts` commit `69e5c8b519032e9999d58d96a12e6e6b44f8b009` deletes all rotation and the resampling that created bands; default samples sharp native V3 texture with only restrained hover/click optics. Keeps color-gated overexposed and neutral near-black source repair without a circular center mask, no material/new art, and preserves microphone/10 FSM.
- Breathing made slower and roughly half the amplitude, `breathing.ts` commit `f8fcf606b7e5c19c895f25b53f97baf41912f36d`; source shader clamp ±1.2%. Regression tests `9d3a8330be36b6169f733d09ea487b48d97fe99d`; CI workflow `815b04554ee4206e62e718a31ddf54620eff1864`. Final website HEAD `9d3a8330be36b6169f733d09ea487b48d97fe99d`.
- GitHub Actions run `38375660791` PASSED GLSL ES100, Vite production build, **39/39 tests** in 9 suites; earlier mid-change CI failures were stale-assertion/test-selector failures, not verified shader defects.
- Visual authority master V3 unchanged SHA256 `9aac52baeac03d61a35ea9809d3580128952de1ae14d77f43c97a5fb7585c50d`; `?breath=off`, `?volume=off`, `?core=off`, `?surface=classic` fallbacks preserved.
- Detailed handoff: [V3.6 no spin, gentle breath](docs/canon/MEDEUS_V3_6_NO_ROTATION_SOFT_BREATH_NATIVE_DEPTH.md). Preview: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/
- `SOURCE_QA=PASS`, `USER_VISUAL_SIGNOFF=PENDING`, `NO_HOLE_BROWSER_VERIFICATION=PENDING`, `REAL_MOBILE_GPU_QA=PENDING`, `STAGE_COMPLETE=FALSE`. No claim that CI alone proves visual disappearance of holes/stripes.


## 2026-10-13 — V3.7 white-lilac pearl-water sphere
- User replaced V3.6 accepted-visual target with new explicit direction: **homogeneous luminous white-lilac pearlescent** sphere, softly moving **water** surface and **stronger real hover/click reaction** ("сама" explicitly authorized direct code implementation). Disposition `EXTEND` interactive orb, `SUPERSEDE` only old default cosmic-source sphere color. No new rendered image asset.
- Website repository `MrPenser/medeus-master-asset` `main`: code `src/lib/medeus/orb-field.ts` commit `f68d3835c55538a7aa77ae85f6c3ecf7c17d5caa` adds `pearlSphereColor` procedural source-independent color with continuous water normals/soft specular and brighter localized touch feedback; retains gentle ±1.2% breath, **NO planet rotation**, no central hole mask or dark well.
- Tests commit `5a494801b995b47dde389302a01620b9cf6d31ea`; CI gates commit `7b3741bc8a5649185820a5f0440812166cb91df0`. GitHub Actions `38377339488`: GLSL ES100 shaders PASS, Vite build PASS, **39/39 tests PASS** across 9 suites. Final source HEAD `7b3741bc8a5649185820a5f0440812166cb91df0`; separately matched with Lovable `ready` and mirrored at exact same SHA.
- Master PNG remains byte-for-byte original SHA256 `9aac52baeac03d61a35ea9809d3580128952de1ae14d77f43c97a5fb7585c50d`; 10 FSM, voice/text/keyboard, independent microphone hover/click, desktop/mobile positions and rollback `?volume=off`, `?core=off`, `?surface=classic` preserved.
- Detailed inheritance: [V3.7 pearl-water sphere](docs/canon/MEDEUS_V3_7_PEARL_WATER_SPHERE.md). Preview https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/ .
- `SOURCE_QA=PASS`, `LOVABLE_SYNC=PASS`, `USER_VISUAL_SIGNOFF=PENDING`, `MOBILE_REAL_GPU_QA=PENDING`, `STAGE_COMPLETE=FALSE`. User to verify actual idle/hover/click/pearl appearance in browser; do not claim visual acceptance from automated checks alone.


## 2026-10-13 — V3.8 corrected flat pearl into optical 3-D depth
- User explicitly rejected V3.7: "говно екак будто 2d". V3.7 visual signoff is **FAIL**, not PASS. `recall&` disposition `EXTEND` of white-lilac water look, `SUPERSEDE` its flat optical material only; **not** a new source image or microphone/body redesign.
- Source `MrPenser/medeus-master-asset`: `src/lib/medeus/orb-field.ts` code commit `5e37cef24188eb8b3b9212ef4b77677ece2da685`, reserved-GLSL identifier correction `47cba6d083bed72e0d09b3d5a5320385d6161901`. A hemisphere surface normal plus independent wave normal drives directional illumination/specular; two internal refracted layers use spherical thickness and parallax for simulated visual depth. Previous flat bright RGB clamp and 14% alpha feather replaced with genuine light/shadow contrast and a 2.6% glass limb feather. Original pearl-water color, stronger actual hover/click, ±1.2% breath and no sphere rotation retained.
- Site HEAD `47cba6d083bed72e0d09b3d5a5320385d6161901`, GitHub Actions run `38378407498`: orb/mic GLSL ES100 PASS, production build PASS, **40/40 tests PASS** (9 suites). CI updated `64f5a5c1e2e1ce4f55c76cdf267708d345d8b8aa`, tests `2d06c13d56680705d9cbe5f4fa5e48f27d5e40c5`.
- Lovable project `76dd8168-469d-4edb-88f6-f313be1c1de8` synchronized at same GitHub HEAD; preview https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/ .
- Immutable scene master remains V3 SHA256 `9aac52baeac03d61a35ea9809d3580128952de1ae14d77f43c97a5fb7585c50d`, 10 FSM, source fallbacks, microphone untouched. Full source authority: [V3.8 dimensional pearl](docs/canon/MEDEUS_V3_8_DIMENSIONAL_PEARL_DEPTH.md).
- Strict boundary: `SOURCE_QA=PASS`, `LOVABLE_SYNC=PASS`, `ACTUAL_3D_MESH=NOT_IMPLEMENTED`, `V3_8_VISUAL_ACCEPTANCE=PENDING`, `REAL_MOBILE_GPU_QA=PENDING`, `STAGE_COMPLETE=FALSE`. This is optically modeled 3D-looking volume using a WebGL fragment shader; do not misrepresent it as a true 3D geometry sphere or visually accepted.

## 2026-10-13 — V3.9 interior emission replaces surface specular
- Latest user direction: remove outer-surface glare and illuminate the sphere **from within**; explicit command "сама" authorizes GitHub source changes. `recall&` disposition: `EXTEND` V3.8 pearl/water optical volume, `SUPERSEDE` only its external specular. No additional image/mesh/microphone/rotation.
- Website `MrPenser/medeus-master-asset`, source commit `395b95581746f881ea8d2b9e3e2fee6846ad1a18`: default `pearlSphereColor` now has thickness-integrated `emitterDepth`, broad `coreGlow`, inner `depthGlow`, refracted pearl layers, white-lilac `emissive`, and transmitted limb. `reflect`/two `specA/specB` mirrored surface lobes removed from DEFAULT pearl (historical rollback unchanged). Hover and physical outward click brighten internal source.
- Source tests `3cc7f92477802dfb20b414d4c5e8302f03d4c71f`, workflow guards `1946c2ea5a39b737adf045784ed434cd769be862`; website main HEAD `1946c2ea5a39b737adf045784ed434cd769be862`. GitHub Actions run `38380002533`: both GLSL ES100 programs PASS, production build PASS, **40/40 tests PASS in 9 suites**. No modification to original V3 master PNG SHA256 `9aac52baeac03d61a35ea9809d3580128952de1ae14d77f43c97a5fb7585c50d`, mic, 10 FSM, soft breath or fallback toggles.
- Detail record: [MEDEUS V3.9 inner light](docs/canon/MEDEUS_V3_9_INTERNAL_PEARL_LIGHT_NO_SPECULAR.md). Preview https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/.
- `SOURCE_QA=PASS`, `CI=PASS`, `USER_VISUAL_SIGNOFF=PENDING`, `MOBILE_REAL_GPU_QA=PENDING`, `STAGE_COMPLETE=FALSE`. The existing renderer remains a 2D WebGL fragment-based optical approximation, NOT a true 3D mesh. Verify live Lovable sync and real browser visual result separately.

## 2026-10-13 — V3.9 MOBILE RESPONSIVE SAFE-AREA + TOUCH
- User explicitly requested "Адапт для мобильных". `recall&` classification `EXTEND` existing V3.9 website, not a new visual/microphone design. Existing mobile scaffold had a panorama-height-dependent scene transform and response near/under the orb. Mobile-only responsive geometry now fits exact same V3 source, live pearl globe, mic and answer into viewport width/height, portrait and landscape; leaves desktop contain layout entirely untouched.
- Website `MrPenser/medeus-master-asset`: created `src/lib/medeus/mobile-layout.ts` commit `3d90c7b281971332ea0d1fcd37660fd90187045b`, imported in `MedeusStage.tsx` `6c1755e917a1eddc4f0533f425a5fccfe733b44a`, tightened keyboard orb overlay to real visible sphere `a94315a12b0f288f893551300b944ad5aaf606ad`, updated `mobile-field.ts` DPR `21136f1b967533cfb94c3f2bf5d03532dbcbeff2`. Screen-safe original headline restored on portrait, answer sits between orb and mic, native keyboard responsive `visualViewport`, mobile touch-down/drag now yields real liquid hover while keeping mic separate, 1.25 DPR/30-36 FPS GPU budget without desktop changes.
- Ten geometrically tested viewport sizes/safe-area cases, keyboard/gestures: `mobile-layout.test.ts` commit `e6ff012ef4d0e52f3679e1560e9020d01f2af090`; workflow guards `c99b38dbc0bbab298c0bcc5dc5de443229a553b7`. Final website HEAD `c99b38dbc0bbab298c0bcc5dc5de443229a553b7`. GitHub Actions `38390516042` `SUCCESS`: big orb+mic GLSL ES100 PASS, Vite production build PASS, **53/53 tests PASS across 10 suites**.
- Existing V3.9 internally lit white-lilac material, gentle breath, hover/click physical impulse, original source PNG SHA256 `9aac52baeac03d61a35ea9809d3580128952de1ae14d77f43c97a5fb7585c50d`, mic/voice, 10 states and legacy rollbacks unchanged. The website is still a DEMO.
- Canonical transfer: [V3.9 mobile responsive](docs/canon/MEDEUS_V3_9_MOBILE_RESPONSIVE_2026-10-13.md), Lovable preview https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/ .
- `SOURCE_QA=PASS`, `UNIT_TESTS=53_53_PASS`, `LOVABLE_SYNC=PENDING_VERIFICATION`, `REAL_ANDROID_IOS_GPU_QA=PENDING`, `OWNER_MOBILE_VISUAL_SIGNOFF=PENDING`, `STAGE_COMPLETE=FALSE`. Do not call site mobile visually approved on the basis of source-only/test-only results.

## 2026-10-13 — V3.9.1 SMALLER MOBILE SPHERE + SINGLE TITLE
- Latest user mobile visual rejection: "Слишком большая сфера тект сверху накладывается на название". `recall&` classification: `EXTEND` mobile scene only, `SUPERSEDE` previous full-source mobile background cover; all desktop and V3.9 pearl/speech/mic/FSM contracts unchanged.
- Verified cause: mobile sphere scaled to ~94% portrait width; source master drawn twice (cover and aligned), duplicating **baked master orb and headline**, plus one extra HTML mobile headline. Fix uses an exactly **76% portrait width** / 66% landscape width limit with safe header clearance. Mobile cosmos fill now samples *lateral original V3 nebula only*, never a second baked orb/title, and aligned mobile source sampling omits the original top headline strip. Exactly one original-text mobile HTML title remains; no source PNG modification.
- Website commits `ab5e9e288f74d1b825ef2010ea5a8962b77089e3` (`mobile-layout.ts`), `11f5c8b49bcfe3944cdf363d4d672dddfd578b7c` (`mobile-field.ts`), tests `1c20ddb7ec4100c791830663ba1db8fe25c5c70d`, CI gate `ca7bdb1eb0d1810a96e6ea931d04c663200a64be`, CI harness one-line `drawImage` assumption correction `b041a253cdee783fab57be0da562879ba074f657`.
- Final GitHub website HEAD `b041a253cdee783fab57be0da562879ba074f657`, GitHub Actions `38403198586`: shader GLSL ES100 PASS, site build PASS, **54/54 unit tests PASS** (10 suites). Independently verified Lovable `ready` with `latest_commit_sha` equal to final GitHub HEAD.
- Source PNG master V3 SHA256 `9aac52baeac03d61a35ea9809d3580128952de1ae14d77f43c97a5fb7585c50d` unchanged; desktop, mic, WebGL pearl interior light, gentle breath, hover and click preserved. Detailed handoff [V3.9.1 Mobile title/scale fix](docs/canon/MEDEUS_V3_9_1_MOBILE_SCALE_SINGLE_TITLE_2026-10-13.md). Preview https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/ .
- `SOURCE_QA=PASS`, `LOVABLE_SYNC=PASS`, `REAL_MOBILE_BROWSER_VISUAL_SIGNOFF=PENDING`, `STAGE_COMPLETE=FALSE`. Never infer user acceptance from source tests alone.


## 2026-10-13 — V3.9.2 Mobile microphone lowered
- User explicitly requested "Микрофон опусти ниже" / "Сама" after mobile screenshot. `recall&` = `EXTEND` the latest mobile-only V3.9.1. Only moved microphone; globe dimensions, surface, independent touch/voice functions and desktop unaffected.
- `MrPenser/medeus-master-asset` source: mobile microphone is lowered up to **40 CSS px in portrait**, **20 CSS px landscape**, clamped to visible space (`mobile-layout.ts` commit `56fbae966578857945ff8cc01b5769fa51425b1c`). Stage `b8d4bda804dea0a0b78463a1fdb629f85b9bc1fb`, `df61b950f3cacbced8de27c6aef570a5e90c3378` shares moved microphone location with pointer hover/click/touch tests and passes displacement to background renderer. Mobile original-scene compositing `d0325091690f1fc7fccbf0e7fb76396d45b79dfd` hides ONLY baked original mic via soft alpha feather to avoid ghost twin, source PNG unchanged.
- `mobile-layout.test.ts` commit `8a2b383d3c3731e0a81fb9b03e86aed7da69ee85`, CI gate `673174c86bc9abec964a936ee599ca6318deeb59`. GitHub run `38405058510` `PASS`: two WebGL GLSL ES100 programs and site build PASS, **58/58 tests PASS**, 10 suites. Website HEAD `673174c86bc9abec964a936ee599ca6318deeb59`. Original V3 SHA256 `9aac52baeac03d61a35ea9809d3580128952de1ae14d77f43c97a5fb7585c50d` unchanged.
- Canonical detail: [V3.9.2 lowered mobile mic](docs/canon/MEDEUS_V3_9_2_MOBILE_MIC_LOWER_2026-10-13.md). Preview https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/ .
- `SOURCE_QA=PASS`, `LOVABLE_SYNC=CHECK_PENDING`, `USER_MOBILE_VISUAL_SIGNOFF=PENDING`, `STAGE_COMPLETE=FALSE`. The user's prior screenshot's big headline and background seams are a separate open mobile visual defect; do not claim resolved by mic relocation.

## 2026-10-13 — V3.9.3 mobile single branded header and single-pass nebula
- User Android Chrome screenshot conclusively shows duplicate text: HTML `ASK WHAT MATTERS` at top, **baked** `MEDEUS` + `ASK WHAT MATTERS` in a second aligned bitmap layer, and hard horizontal joins. "Микрофон на месте. Текст дубль с наложением". Treat previous V3.9.2 mobile visual user result as FAIL on duplicated title, despite mic position acceptance. Decision `EXTEND` mobile renderer and semantic header, `SUPERSEDE` only the double-pass background, not master art or native mic interactions.
- Verified source root cause: `mobile-field.ts` renders one lateral nebula cover followed by an aligned V3 source strip beginning at only 7.5% height. That leaves embedded logo/tagline in the copied strip and joins two mismatched cosmic compositions. The additional top mobile HTML tagline duplicates the source. New `mobile-field.ts` commit `e25b390fdb60bac872a5900e5c6848c3c5e5352b`: exactly ONE full-viewport `drawImage` of the approved V3 left-lateral nebula crop (never copies old logo, baked big globe or mic). No seam, no ghost/source overlay, no new art.
- Mobile-only header in `MedeusStage.tsx` `4984dffdc0b6ebf2368fe59194f483d92776eac3`, `de5e8f6ca87bfaafbf06f5e0318fb2dd9d2d5b6f` now renders a single `MEDEUS` name + one `ASK WHAT MATTERS` subline in safe-area HTML. Desktop unchanged. Mobile mic stays lowered as previously accepted and independently reactive, V3.9 pearl sphere and small size unchanged.
- Mobile test `4fa2a0b26e46de4e0bc96c377605edb706ef0ad7`, test harness regex fix `bb2aac6c2ac2c1c30e58b8417f475c61d88131c1`; CI gate `b9b33131730a0c137ecfed4fec6182f9abf4a1ae`, trigger expansion `bda4b4935451ea6b520fd889b01c8e9165ca3472`. Final website HEAD `bda4b4935451ea6b520fd889b01c8e9165ca3472`, Actions `38411074573` SUCCESS: 58/58 tests, WebGL orb+mic GLSL ES100 and build PASS. Lovable project `76dd8168-469d-4edb-88f6-f313be1c1de8` SHA independently matches same HEAD; preview https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/ .
- Canon detail: [V3.9.3 mobile single brand/seamless cosmos](docs/canon/MEDEUS_V3_9_3_MOBILE_SINGLE_BRAND_SEAMLESS_BACKGROUND_2026-10-13.md). Immutable V3 master PNG SHA256 `9aac52baeac03d61a35ea9809d3580128952de1ae14d77f43c97a5fb7585c50d` unchanged.
- `SOURCE_QA=PASS`, `CI=PASS`, `LOVABLE_SYNC=PASS`, `MOBILE_USER_VISUAL_SIGNOFF=PENDING`, `STAGE_COMPLETE=FALSE`. Ask user to inspect actual Android/iOS; do not infer user approval from static code tests.


## 2026-10-13 — V3.9.4 LILAC sphere color
- User direction "Сделай шар лиловым" followed by "Сама": user-authorized color-only change to the large sphere; `recall&` = `EXTEND` V3.9 inner luminous volume, preserving V3.9.3 mobile title/background and already accepted lower microphone.
- Website `MrPenser/medeus-master-asset` `orb-field.ts` color commit `0dec3483971bb9ba499d6e89983275a18949db7f` changes lilac base/body/depth and inner emission tint + transmitted edge, without changing the emission strength, geometry, water, click, hover, breathing, mic or UI. Tests `77a0dac79569f3677210c3b0593cf1380e898970`; QA `8d8dec4b0f0f542e7f13a42784d45993c86c872a`.
- Final source HEAD `8d8dec4b0f0f542e7f13a42784d45993c86c872a`: GitHub Actions `38424331561` complete SUCCESS — both shader programs GLSL ES100 PASS, production build PASS, 58/58 tests PASS (10 suites). Lovable project `76dd8168-469d-4edb-88f6-f313be1c1de8` `ready` and independently synced at exact same commit SHA.
- [MEDEUS V3.9.4 lilac orb](docs/canon/MEDEUS_V3_9_4_LILAC_ORB_COLOR_2026-10-13.md). Preview https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/ . Immutable V3 master SHA256 `9aac52baeac03d61a35ea9809d3580128952de1ae14d77f43c97a5fb7585c50d` unchanged.
- `SOURCE_QA=PASS`, `LOVABLE_SYNC=PASS`, `USER_LILAC_COLOR_VISUAL_SIGNOFF=PENDING`, `MOBILE_REAL_GPU_QA=PENDING`, `STAGE_COMPLETE=FALSE`. Do not infer visual approval from CI.

## 2026-10-13 — V3.9.6 Dark lilac body with bright inner emitter
- Owner required dark sphere illuminated from inside; user authorized direct edit ("Сам"). EXTEND V3.9.5 internal glow. Code-only dark palette and stronger volumetric emission in src/lib/medeus/orb-field.ts (website commit 57a4b11c7ee55095043a8db6e2067bb3fdb5c016). Preserve zero rotation, existing water, breath, hover, click, original mic and all mobile layout/fixes.
- Website HEAD de68f2f44e2487e6196a6f76bb6b7f47aac7c5b8; GitHub Actions 38428240191 SUCCESS, GLSL ES100 and Vite PASS, 59/59 unit tests PASS. Lovable project 76dd8168-469d-4edb-88f6-f313be1c1de8 exact same mirrored SHA and ready.
- Canon: docs/canon/MEDEUS_V3_9_6_DARK_SPHERE_INNER_LIGHT.md; preview https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/ . Locked V3 source SHA256 9aac52baeac03d61a35ea9809d3580128952de1ae14d77f43c97a5fb7585c50d unchanged.
- SOURCE_QA=PASS; LOVABLE_SYNC=PASS; USER_VISUAL_ACCEPTANCE=PENDING; STAGE_COMPLETE=FALSE.


## 2026-10-13 — V4 APPROVED IMAGE installed and interactive
- User directed "все устанавлива на сайт а анимируй", "разрешаю делай", "дал доступ . работай". `RECALL` disposition `EXTEND` running ten-state site and `SUPERSEDE` only the default visual source/pearl material; no AI re-rendering of approved art.
- EXACT chosen `космический_вихрь_medeus.png` imported byte-for-byte to website `MrPenser/medeus-master-asset/src/assets/MEDEUS_MASTER_VISUAL_V4_APPROVED.png`. Size 1448x1086, SHA256 `773f67be7fea7fb8b3dd63b88f58dd55d01e82b0724ed3098db317a8d4f8d5b6`, Git blob `da31f9de8c27a61d4821e86a789d2e21de9257e2`. V4 has no side labels or drawn orbital paths, has darker purple orb with closed luminous center and full smoky edge, mic lower. Original V3/V2 remain immutable backups.
- Active renderer now **samples V4's real pixels for the full sphere**, not synthesized flat pearl; keeps soft irregular breath, low-alpha outer smoky glow, local viscous hover and one expanding outbound click ring, no UV rotation, preserving independent lowered microphone voice/hover/press, ten FSM, no duplicate mobile brand, and responsive safe areas. Website code commits: asset `d316bf3c6309e32d2b2ffd0c51335be405e3db6e`, placement `51c3aac16d4bacc08af829159154ac70544921ce`, orb motion `8835d822e3b21359545e42f127f3ff98d6e677e5`.
- Unit/QA `64dbc5e74c9ecd323db7a9a680f5dc00172ebb43` HEAD, GitHub Actions `38443949668` **SUCCESS**, both GLSL ES100 shader and Vite site jobs pass, **60/60 tests PASS** in 10 suites. Live Lovable project `76dd8168-469d-4edb-88f6-f313be1c1de8` independently matched `ready` at same commit.
- Canon authority: [V4 exact approved scene installed/animated](docs/canon/MEDEUS_V4_APPROVED_SCENE_ANIMATED_2026-10-13.md). Preview: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/ .
- `IMAGE_HASH=PASS`, `SOURCE_QA=PASS`, `LOVABLE_SYNC=PASS`. `USER_VISUAL_SIGNOFF=PENDING`, `REAL_MOBILE_GPU_QA=PENDING`, `STAGE_COMPLETE=FALSE`. Public publish not yet performed; project `is_published=false` in last read. Do not label public production until an actual deploy.


## 2026-10-14 — V4.1 asynchronous local color flares
- Latest owner instruction: keep approved V4 scene exactly as fixed, add *soft sunlike color flares* in multiple parts of the core at DIFFERENT times, not a synchronized whole-sphere recolor. Explicit execution consent: "сама". Disposition `EXTEND` only; original artwork, microphone, and smoke kept intact.
- Active website `MrPenser/medeus-master-asset`: `src/lib/medeus/orb-field.ts` now adds `v4SolarFlares(p,T,motion)` — four broad independently moving pastel lilac/rose/ice-lilac patches, staggered smooth pulse envelopes and additive bounded low-energy RGB modulation, only inside `approvedV4` after exact source sampled; no texture spin or overlay rings. Shader commits `fe1cf789cd8a629d126a45ac10516a808a9d1f21` and regression scope fix `1e2d4620fdd5d5b005d9e848db62d6a27630311c`.
- Tests + CI gates: `bad86f4ec4d257ac1dacee28c10ed62c34838557` and `99c4d21675f9eb60a76b89f4e967795dfe2b5442`. GitHub Actions **38523096670** exact HEAD **99c4d21675f9eb60a76b89f4e967795dfe2b5442**: orb/mic GLSL ES100 PASS, production build PASS, **62/62 tests PASS** (10 suites); Lovable status `ready`, mirror at identical SHA.
- Exact V4 PNG `MEDEUS_MASTER_VISUAL_V4_APPROVED.png` SHA256 `773f67be7fea7fb8b3dd63b88f58dd55d01e82b0724ed3098db317a8d4f8d5b6` remains unchanged; V3 rollback and all ten FSM, separate microphone voice/press/hover, accessibility reduced-motion and layout remain in place. No public publication.
- Canonical specification: [MEDEUS V4.1 local solar flares](docs/canon/MEDEUS_V4_1_LOCAL_SOLAR_FLARES_2026-10-14.md). Preview https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/.
- `SOURCE_QA=PASS`, `LOVABLE_SYNC=PASS`, `V4_1_VISUAL_SIGNOFF=PENDING`, `MOBILE_REAL_GPU_QA=PENDING`, `STAGE_COMPLETE=FALSE`. Do not count tests as proof the user likes visual intensity.


## 2026-10-14 — V4.2 halo solar bursts and independent color families
- User rejected V4.1 because **whole sphere, especially white, brightened too strongly**. Current owner direction: **separate soft sun-like flares on smoky halo** plus **independent source-white/source-violet/source-lilac luminosity** (not a global RGB tint). Classification `EXTEND` locked V4 / `SUPERSEDE` V4.1 additive wide-flare implementation.
- Website `MrPenser/medeus-master-asset` source commit `20e326e240fa150dc9c50d0194d848cbbb59450e` replaces additive `v4SolarFlares` with `v4HaloBursts` applied only in `if(approvedV4 && r>rim)`, and original-pixel-color-masked `v4IndependentColors` inside. Each family retains original hue via small multiplicative gain (white 2.2%, violet 4.8%, lilac 3.5% max) with independent slow envelopes/noise. Deleted global `c=authentic*(1.+.015*sheen*uMotion)` and additive interior flare. Four localized halo flashes have distinct independent phases and positions, no orbital drawings or rotation.
- Tests `f452d5c5b1ad0fc0c7c161a2fbf7b6c59d6efd7d` plus harness fixes `90d02697f6ac76bcfa55a5bbe4892b351a213975` / `46a1ac344a051773c466a7f4b942d9a644e73d1e`; CI `89023d96bf09061ed160214d1e9999223d3e64c4`. Final website HEAD `46a1ac344a051773c466a7f4b942d9a644e73d1e`. GitHub Actions `38524494645` **SUCCESS**, GLSL ES100 orb/mic and Bun/Vite build PASS, **63/63 tests PASS (10 suites)**.
- Locked master V4 PNG SHA256 `773f67be7fea7fb8b3dd63b88f58dd55d01e82b0724ed3098db317a8d4f8d5b6` unchanged, V3 backup unchanged; no microphone, 10-state FSM or responsive layout regression. No public deployment.
- Complete canon: [V4.2 halo flares and intrinsic colors](docs/canon/MEDEUS_V4_2_HALO_SOLAR_BURSTS_COLOR_SEPARATION_2026-10-14.md). Preview https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/.
- `SOURCE_QA=PASS`, `USER_VISUAL_SIGNOFF=PENDING`, `REAL_BROWSER_MOBILE_QA=PENDING`, `STAGE_COMPLETE=FALSE`. Lovable mirror verified independently before claiming sync.


## 2026-10-14 — V5 living star: kinetic convection and erupting corona
- Latest user explicitly rejects V4.2 as visually motionless: "ореол статичный! цвета тоже! ... живую звезду ... внутренние и внешние процессы", authorizes execution "сама". `RECALL_DISPOSITION=EXTEND` immutable V4 image with `SUPERSEDE` V4.2's weak decorative effects as default, but leave exact A/B fallback `?star=off`.
- Website `MrPenser/medeus-master-asset`: shader `cc863927fc97d5cb85db79b3fdf99ee9767c6b6e` implements **moving original V4 source filaments** via time-varying bounded optical convection, independent thermal/convective/granulation cells, separately excited white/violet/lilac families and spatially evolving external corona with FOUR erupting directional prominence areas. Optical width increases from prior 0.087 to up to ~0.245 radius, frame/canvas `ORB_BOX=1.30`; no sphere rotation or ring. A/B switch via `uStar` /`?star=off` added with stage `4bdc18b52f7990a73fa04983916b9590bf29bf97`.
- Updated numeric source-motion tests `c4511b081a992d7e0880c45e0877d3b8e036bd2c`; workflow `413b9efb2b3c4c93c91ce172f155289744676547`; HEAD `413b9efb2b3c4c93c91ce172f155289744676547`. Actions `38528498056`: production build PASS, orb/mic GLSL ES100 PASS, **67/67 unit tests PASS in 10 suites**.
- Master V4 PNG SHA256 `773f67be7fea7fb8b3dd63b88f58dd55d01e82b0724ed3098db317a8d4f8d5b6` unmodified, V3 backup, 10 FSM, mic and voice/text, responsive layout intact. No public publishing.
- Detailed canon: [V5 live star](docs/canon/MEDEUS_V5_LIVE_STELLAR_CONVECTION_CORONA_2026-10-14.md); preview https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/.
- `SOURCE_QA=PASS`, `USER_VISUAL_SIGNOFF=PENDING`, `REAL_DESKTOP_MOBILE_QA=PENDING`, `STAGE_COMPLETE=FALSE`. Lovable matching SHA must be independently verified; GitHub CI does not guarantee aesthetic realism.


## 2026-10-14 — V5.1 eight-direction active stellar corona
- Owner feedback V5 is improved but corona must be **more active** and produce independently animated prominences at **ALL** positions (upper/lower/lateral/diagonals); user explicitly authorized direct changes. `RECALL_DISPOSITION=EXTEND_V5_CORONA_ONLY`, previous V5 internal stellar convection is retained.
- Website `MrPenser/medeus-master-asset`: `src/lib/medeus/orb-field.ts` commit `27e3cb2d43e80fc3ffc8d2ee3c3cf7cb85de2e3c` extends corona to eight non-synchronous compass/diagonal prominence sectors, layered moving billows/filaments and dynamically changing reach up to ~0.335 radii. Outer region clip .35, `ORB_BOX=1.43` preserves margin through hover/breath; no orbital lines or UV sphere spin. No additive increase in overall interior/white luminosity.
- Shader and view preserve exact locked V4 PNG SHA256 `773f67be7fea7fb8b3dd63b88f58dd55d01e82b0724ed3098db317a8d4f8d5b6`, independent microphone, voice/text FSM, soft breath, `?star=off` V4.2 comparison and other rollback modes.
- Test commit `8ab8c6a62d46289f7477e51a079dffa7a2cb420b`, CI commit/final HEAD `357a9aaa27d4e23292234ce298926f1510a8d18f`. Actions `38529906932`: GLSL ES100 shader PASS, production site build PASS, **68/68 tests PASS** over 10 suites, including independent time samples for all compass sectors and safe maximum viewport extent.
- Canonical source: [V5.1 eight-sector eruptive corona](docs/canon/MEDEUS_V5_1_EIGHT_SECTOR_ERUPTIVE_CORONA_2026-10-14.md). Preview: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/.
- `SOURCE_QA=PASS`, `USER_VISUAL_SIGNOFF=PENDING`, `REAL_DESKTOP_MOBILE_GPU_QA=PENDING`, `STAGE_COMPLETE=FALSE`; Lovable requires final exact SHA mirror verification before labeling SYNC PASS; not publicly published.


## 2026-10-14 — V5.2 stronger localized mouse hover
- User asked explicitly for stronger cursor hover response on approved V5.1 ("сделай отклик на наведение курсора сильнее") and authorized direct GitHub changes ("разрешаю"). `EXTEND` V5.1 orb hover only; preserve original approved V4 image, all 10 FSM, mic hover/click, and no global sphere whiteout or new orbit.
- Website `MrPenser/medeus-master-asset` source commit `8b572cc734cd9467d24f30031bbe8dcbc3d50aa9`: V5-only local surface tug .165→.235, hover edge bulge .050→.075, water refraction lens .042→.064; localized lilac emission signal increases over 3x while spatially confined; adjacent corona sector brightens through angular falloff, **not** whole corona. The preexisting one-way click pulse unchanged. Quad `ORB_BOX=1.46` prevents extra corona clipping under hover/breath.
- `?star=off` retains exact prior V4.2 hover, classic/volume/breath fallbacks unchanged. V4 PNG SHA256 `773f67be7fea7fb8b3dd63b88f58dd55d01e82b0724ed3098db317a8d4f8d5b6` unmodified; mic not touched.
- Test commit `23454ca7b4dbf6af72f2b46df03ed2b9d021c953`, CI commit and HEAD `503c4d6b61543c8149c36f15cd7974441506a158`. GitHub Actions `38614705807`: shader and site PASS, **69/69 tests PASS** over 10 suites. Lovable `ready` / `agentFinished=true` verified at exact SHA `503c4d6b...`, preview https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/.
- Full canon: [V5.2 strong hover](docs/canon/MEDEUS_V5_2_STRONG_LOCAL_HOVER_2026-10-14.md).
- `SOURCE_QA=PASS`, `LOVABLE_SYNC=PASS`, `USER_VISUAL_SIGNOFF=PENDING`, `MOBILE_REAL_BROWSER_QA=PENDING`, `STAGE_COMPLETE=FALSE`. No public production deployment.


## 2026-10-14 — V5.3 visibly projecting plasma tongues outside the corona
- User states previous V5.2 prominences are **NOT VISIBLE**. Corrected root cause: the eight former numerical prominence envelopes merely tinted/alpha-modulated a diffuse narrow halo and produced no extended visible jet silhouettes. `RECALL_DISPOSITION=EXTEND_V5_2_CORONA_ONLY`; previous visible-acceptance must not be claimed.
- Live website `MrPenser/medeus-master-asset` shader commit `d486da46513adb16bf2039513fd5fd383bdd6af3` adds `v53PlasmaTongue`: **spatially extended curved outward hot-core plasma jets** with independent timed growth, bend, opacity taper and thin luminous spine, rendered for all eight independently phased compass sectors. Max jet length ~0.39 radius outside the star; scope gate extended .35 → .43, `ORB_BOX` 1.46 → 1.55 with hover/breath margin. Former diffuse corona remains subordinate: jet-driven alpha `alpha=clamp(alpha*.38+.78*visiblePlume+.16*brightSpine,0.,.96)`. The original V4 image and interior star, lower mic, click/hover, 10 FSM, V4.2 `?star=off` fallback remain intact.
- Numeric/eight-sector regression commit `11f2bcea11fe3355beb006785106225ef25e91b7`; CI HEAD `c47a5af2b3c92543436c861e6b7f25c553836277`. Actions run `38616233746` completed SUCCESS (GLSL ES100 compile, Vite/Bun production build, **70/70 tests in 10 suites PASS**). Lovable `ready`, `agentFinished=true`, verified at exact same SHA.
- Canon [V5.3 visible prominences](docs/canon/MEDEUS_V5_3_VISIBLE_PROMINENCES.md), preview https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/ .
- `SOURCE_QA=PASS`, `LOVABLE_SYNC=PASS`, `USER_VISUAL_SIGNOFF=PENDING`, `REAL_BROWSER_GPU_QA=PENDING`, `STAGE_COMPLETE=FALSE`. Attempt to retrieve latest Lovable screenshot for direct image verification was not supported; numerical tests do NOT establish final aesthetic visibility. If user still cannot see jets, next step MUST examine real live frames/compositing rather than only raise shader gains.


## 2026-10-14 — V5.4 coronal plasma sheets replace rejected worm jets
- User visually rejects V5.3: "они как черви". Correct diagnosis: `v53PlasmaTongue` used a single smooth Gaussian tube with overbright narrow spine. V5.3 `USER_VISUAL_ACCEPTANCE=FAIL`. New `EXTEND` corona while `SUPERSEDE` only tubular jet shape; preserve V4 exact master, independent mic, approved V5.2 hover, 10 FSM, 8 eruption sectors and `?star=off` rollback.
- Website `MrPenser/medeus-master-asset`, shader `9465dd06fddd830f0170816798a12220cbf28555`: removed V5.3 core; new `v54CoronalFan` splinters one short root into asymmetric diverging plasma curtains, turbulent time-changing broken edges, transparent central rifts and fragmented small emissive filaments. Broad violet-lilac light, **not** solid homogeneous white glowing 'worms'; eight independently timed compass sources retained. Exclusion radius `.43` and `ORB_BOX=1.55` unchanged.
- Source tests `08f933e963121c459d961f7f76cd95a6dde3fb93` confirm two separated wings >8x center density high in plume and stable connected base; CI `8ff057f11d35f4e8c117f3ada5b95c844fbe29b1` asserts no `v53PlasmaTongue`, eight V5.4 forks, pixel source untouched, builds. GitHub Actions `38619899068`: WebGL ES100 GLSL PASS, production build PASS, **71/71 tests PASS** (10 suites).
- Canon: [V5.4 forked solar plasma](docs/canon/MEDEUS_V5_4_FORKED_SOLAR_PLASMA_2026-10-14.md). Preview https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/.
- `SOURCE_QA=PASS`, `CI=PASS`, `USER_VISUAL_SIGNOFF=PENDING`, `REAL_BROWSER_GPU_QA=PENDING`, `STAGE_COMPLETE=FALSE`; Lovable precise SHA sync needs current verification.


## 2026-10-14 — V5.5 shorter corona and physically reactive cursor, not light
- User corrects V5.4: corona flashes too tall and hover must NOT be luminance-based; authorized direct edit ("разрешаю"). `RECALL_DISPOSITION=EXTEND`: retained exact approved V4 scene, shortened V5.4 torn, branching solar prominences, replaced V5 hover light response with **only local shape, height, texture distortion and single physical click wave**; independent mic and all ten FSM unchanged.
- Live repo `MrPenser/medeus-master-asset`: shader `b56616aeb42f33f5e90f3f2e08f490d663537c70`. Fan reach `.08+.31*surge` → `.06+.18*surge` (max 39%→24% of radius), quicker tip attenuation, narrower branches, `rim+.28` clip vs `rim+.43`, `ORB_BOX=1.42`. Height hover .285 instead of .235, bulge .095 instead of .075, source-lens displacement .092 instead of .064; no added V5 hover light on either corona or star, V4.2 A/B `?star=off` retains historical response.
- Tests `1af82ac3d2b405d56a75a9a5552541f3fcdb3053` plus inherited assertions correction `1b5c8f0f56c819bb49199352dab29f1b7cbdec15`; CI workflow `5e11c5286c6a9d20b34f7cc0bdc1c55dac0101d3`. Final website HEAD `1b5c8f0f56c819bb49199352dab29f1b7cbdec15`, GitHub Actions **38622238804 SUCCESS**, GLSL ES100 + production build PASS, **72/72 tests in 10 suites PASS**. Lovable `ready` at identical SHA; preview https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/ .
- Canon [V5.5 short corona + mechanical hover](docs/canon/MEDEUS_V5_5_SHORT_CORONA_PHYSICAL_HOVER_2026-10-14.md).
- Source art V4 PNG SHA256 `773f67be7fea7fb8b3dd63b88f58dd55d01e82b0724ed3098db317a8d4f8d5b6` unchanged; no new artwork, no public publication. `SOURCE_QA=PASS`, `LOVABLE_SYNC=PASS`, `USER_VISUAL_SIGNOFF=PENDING`, `REAL_BROWSER_GPU_QA=PENDING`, `STAGE_COMPLETE=FALSE`.


## 2026-10-14 — V5.6 live microphone line audio response (input RMS / output TTS boundary)
- Owner requested practical code implementation: existing thin horizontal lines on both sides of lowered mic must move **in time with actual user speech and with spoken MEDEUS response**. Direct instruction "сделай сама". `RECALL_DISPOSITION=EXTEND_V5_5`; do not generate new audio/rings/art, do not change approved PNG or large-star shader.
- Website `MrPenser/medeus-master-asset` main HEAD `5fb18bd6af890507af58db195c75ada404c4583b` implements new `mic-voice-lines.ts` (real mic PCM RMS via Web Audio Analyser after recognition begins, adaptive noise-threshold & motion smoothing; exact original two baked waveform strips animated at V4 mic (706,830); no animation at rest and proper MediaStream/AudioContext cleanup); `speech.ts` exposes native recognition speech activity; `response-channel.ts` and `temporary-greeting.ts` forward TTS start/boundary/end; `MedeusStage.tsx` integrates controller and renders at exact responsive mic geometry. Native SpeechSynthesis PCM is **not accessible**: output articulation follows speech boundary timing, not measured sound volume. No recognition = no real input RMS; coarse recognizer speech activity fallback if analyser denied. No extra controls or auto-play; original V4 image, V5.5 star, mic liquid hover/press, ten FSM and existing voice/text routing preserved.
- New test suite `mic-voice-lines.test.ts`; GitHub Actions `38624077560` exact SHA: GLSL ES100 PASS, production build PASS, **76/76 tests passed in 11 suites**. Lovable `ready`, `agentFinished=true`, `latest_commit_sha` exact same HEAD; preview https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/. Master V4 PNG SHA256 `773f67be7fea7fb8b3dd63b88f58dd55d01e82b0724ed3098db317a8d4f8d5b6` unchanged. No public production publish.
- Canon: [V5.6 mic-side spoken waveform strips](docs/canon/MEDEUS_V5_6_SPEECH_REACTIVE_MIC_LINES_2026-10-14.md).
- `SOURCE_QA=PASS`, `LOVABLE_SYNC=PASS`, `USER_VISUAL_SIGNOFF=PENDING`, `LIVE_MIC_PERMISSION_AND_TTS_BOUNDARY_QA=PENDING`, `STAGE_COMPLETE=FALSE`. Must verify real speech response in supported browser with mic permission and TTS; source tests alone do not prove tactile visual cadence.


## 2026-10-14 — V5.7 true motion of baked V4 microphone waveform pixels
- User rejects V5.6 visually: "рисованные полоски остались статичными а сверху появились звуковые прямы е линии . это не то". `SUPERSEDE` V5.6 line renderer only, `REUSE` existing microphone amplitude and TTS speech-boundary detection; no new artwork, no static duplicate.
- Root cause found directly on EXACT 1448x1086 approved PNG: original mic center V4 (706,830), **baked waveform center y=860**, 30px lower (V5.6 extra synthetic bars were painted near y=836); original baked waveform stayed static in cosmic background. Corrective code now splits original RGB waveform into separated pixel strips using source x358..640 and x772..1054 / y808..912 and a temporary cleaned background derived solely in memory. Repaints source pixels using Canvas2D `drawImage` vertical warping, driven by actual mic WebAudio RMS and output TTS timing. No new `stroke/lineTo` bars or circles anywhere in final render, and static source strips no longer remain in source-derived background. At silence source waveform reproduces at 1x height. Approved PNG unchanged SHA256 `773f67be7fea7fb8b3dd63b88f58dd55d01e82b0724ed3098db317a8d4f8d5b6`.
- Website `MrPenser/medeus-master-asset`: new `src/lib/medeus/mic-waveform-material.ts` (RGB pixel extraction/clean presentation only), stage integration `31a69103fa8bd9422fdab49f4293e20e3717913b`, rejected painted-bar removal `befe0ba6c5ed767d57a1312c2a73ef92d61ce550`. Numeric and fake-image-custody tests `src/lib/medeus/mic-waveform-material.test.ts`, revised voice tests, extended CI. Final website HEAD `96e8191e6a8d25d423470acb4f793afa85610b5b`.
- GitHub Actions `38626034095` completed SUCCESS at exact HEAD, orb/mic GLSL ES100 PASS, build PASS, **80/80 tests in 12 suites PASS**; Lovable mirrored exact HEAD `ready`, `agentFinished=true` with preview https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/. No public production publish.
- Canon [V5.7 genuine waveform material](docs/canon/MEDEUS_V5_7_AUTHENTIC_MIC_WAVEFORM_MATERIAL_2026-10-14.md). `SOURCE_QA=PASS`, `LOVABLE_SYNC=PASS`, `USER_VISUAL_SIGNOFF=PENDING`, `REAL_BROWSER_MIC/TTS_QA=PENDING`, `STAGE_COMPLETE=FALSE`.


## 2026-10-15 — V5.8 microphone waveform field artifact fix
- User screenshot `Screenshot_4.png` shows rectangular damaged-nebula regions near mic voice strips; user says "есть артефакты полей действия звуковых полос". Prior V5.7 visually NOT signed off. `RECALL_DISPOSITION=FIX_EXTEND`; do not repaint V4 master or use new equalizer lines.
- Root cause verified in site source: V5.7 `separateApprovedMicWaveform` interpolated **entire rectangular 282x104 source areas** from top/bottom sky rows, causing obvious hard-boundary nebula blocks. V5.8 now modifies only conservatively detected bright local-contrast waveform pixels inside smooth x/y feathered regions, computes local sky from 8 vertical neighbor points, and preserves all other RGB pixels bitwise in RAM-only presentation canvas; RGB residual reconstructs original at silence. Original V4 visual and microphone/stellar interaction/voice recognition/TTS wiring remain unchanged.
- Website `MrPenser/medeus-master-asset` source fix `8c99c8e85cb605852ca7dd113db20879a0f0af64`; regression `9c60ae9058b88dc4394865b15ffc51dabb6430c5`, CI final HEAD `1ce0789e6d8edf15953103bd703ddf0478303c07`. GitHub Actions `38682640674`: actual GLSL ES100 compile PASS, production build PASS, **81/81 tests PASS in 12 suites**. Synthetic test verifies strong unrelated nebula is bitwise untouched even inside strip bounding rect, no bright line outside true band, and source RGB reconstruction at rest. Lovable `ready` mirrored code-bearing fix; later commits change only tests/workflow.
- Canon: [V5.8 fix audio-field rectangles](docs/canon/MEDEUS_V5_8_MIC_WAVEFORM_ARTIFACT_FIX_2026-10-15.md). Preview https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/ .
- `SOURCE_QA=PASS`, `CI=PASS`, `USER_VISUAL_SIGNOFF=PENDING`, `REAL_BROWSER_MIC_QA=PENDING`, `STAGE_COMPLETE=FALSE`. If screenshot still shows fields, inspect actual browser canvas compositing and screenshot frames; don't claim screenshot artifact definitively removed by static tests.


## 2026-10-15 — V5.9 speech waveform source-center correction and voice sensitivity
- User reports after V5.8 that rectangular nebula blocks are almost gone but original mic lines have essentially **no visible response** to speech. `RECALL_DISPOSITION=FIX/EXTEND`, V5.8 visual signoff remains pending. Owner screenshot shows original baked waveform aligned with mic center, but V5.7/V5.8 assumed y=860 (30px below actual mic center at y=830).
- Website `MrPenser/medeus-master-asset` code commits: `4133d5401ae79d87bebbe281ab62914d3e779408` real source wave center corrected y=830, source strip ys 808→778, less severe brightness/contrast gating and stronger original-pixel drawImage deformation; `9c7a70ef652c3fb18a4bf16ec1679268a0d3c8ef` improves microphone RMS sensitivity and speech-recognizer onSpeechStart fallback even if parallel analyser reports suppressed PCM, strengthens native TTS boundary unavailable visual activity while voice actually speaking; `fcfb3f255351eed88ea03fee54577c5c21e0ed72` adds strictly opt-in `?waveProbe=1` synthetic movement diagnostic to isolate audio capture failure vs native waveform render failure. Default remains ONLY real input amplitude / TTS onstart-onboundary-onend timing, no permanent synthetic bars. V4 original image SHA256 `773f67be7fea7fb8b3dd63b88f58dd55d01e82b0724ed3098db317a8d4f8d5b6` unchanged; existing mic/large orb interactions, 10 FSM and nebula artifact protection remain.
- Tests `8c1996c46095ce9b34e6e12cb5fe55c925182cba`, `e76f1bcb2fa89c95f099e2a39191d37cb4b3d89e`; CI `24c632ca3d06d827de31989188b86673ee551b46`; inherited stale trough test correction `f4b81b3bbf9d7d4abc7c58cbfacb610d16c05b44` (final HEAD). GitHub Actions `38684085458` completed SUCCESS at exact HEAD: real GLSL ES100 compile, production build and **83/83 unit tests PASS (12 suites)**. Lovable `ready`/finished mirrored last code-bearing+CI commit; subsequent final commit tests only. No public publishing.
- Canon: [V5.9 waveform reactivity + alignment](docs/canon/MEDEUS_V5_9_WAVEFORM_REACTIVITY_AND_ALIGNMENT_2026-10-15.md). Preview https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/ and separate diagnostic https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/?waveProbe=1 .
- `SOURCE_QA=PASS`, `CI=PASS`, `LOVABLE_CODE_MIRROR=PASS`, `USER_VISUAL_SIGNOFF=PENDING`, `LIVE_MIC_&_TTS_QA=PENDING`, `STAGE_COMPLETE=FALSE`. If demo probes move while real speaking doesn't, inspect ASR permission and PCM browser path; if even demo does not move, inspect source image pixel-mask isolation and scene layer stacking. Do not pass static tests off as actual browser animation acceptance.


## 2026-10-15 — Owner rollback: restore V5.5 STATIC mic waveform, reject V5.6–V5.9
- User explicitly rejects voice-reactive waveform attempts ("ерундаверни статичнуюкартинку"). Decided `SUPERSEDE` V5.6–V5.9 microphone-wave rendering, `RESTORE` accepted **static original V4 bitmap waveform** and pre-experiment V5.5 website logic. Do NOT reintroduce audio-reactive mic line experiments unless the owner explicitly requests anew. Keep living-star V5.5 and all its accepted stellar / mechanical hover behaviors unchanged.
- **Atomic forward-only** website commit `f6eb5308e74bf0074cb3acf2e5e6e4ab0f6088b0` in `MrPenser/medeus-master-asset` RESTORES THE EXACT FULL GIT TREE of V5.5 historical commit `1b5c8f0f56c819bb49199352dab29f1b7cbdec15`: both tree IDs `aa1aa5263edbc8810ffd522bd195af3c034e1c9e`. No reset/force/amend; existing Lovable live GitHub connection safe.
- Restored original `MedeusStage.tsx`, `speech.ts`, `response-channel.ts`, `temporary-greeting.ts` and QA workflow blobs; deleted four experimental `mic-voice-lines*` / `mic-waveform-material*` modules/test files. Existing original PNG pixel SHA256 `773f67be7fea7fb8b3dd63b88f58dd55d01e82b0724ed3098db317a8d4f8d5b6` unaffected. No overlay, region masking, animated drawn bars, double microphone stream, waveProbe, or additional background artifacts.
- Actions `38707866999` COMPLETED SUCCESS at exact rollback HEAD: shader job PASS (GLSL ES100), site production build PASS, **72/72 tests in 10 suites PASS**. Lovable `ready`, `agentFinished=true`, latest SHA `f6eb5308...` matched exact website HEAD; public site has not been published.
- Canon [static waveform restoration](docs/canon/MEDEUS_V5_5_STATIC_MIC_WAVEFORM_RESTORED_2026-10-15.md). Preview https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/.
- `EXACT_V5_5_TREE_RESTORED=PASS`, `SOURCE_QA=PASS`, `CI=PASS`, `LOVABLE_SYNC=PASS`. `USER_VISUAL_SIGNOFF_OF_RESTORATION=PENDING` only for end-user browser confirmation; no new change to artistic master.
