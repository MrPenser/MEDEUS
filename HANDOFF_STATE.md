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
