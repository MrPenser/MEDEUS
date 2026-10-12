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
