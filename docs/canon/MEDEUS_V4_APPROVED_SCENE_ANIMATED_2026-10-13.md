# MEDEUS V4 — approved scene asset integrated, sphere animated

Date: 2026-10-13. Disposition: EXTEND the existing site runtime; SUPERSEDE V3.9.6 default big-sphere cosmetic source and master composition. User explicitly authorized implementing and animating their last approved image with no side text and lower microphone: "все устанавлива на сайт а анимируй", then "разрешаю делай", "дал доступ . работай". No new image generated during implementation.

## Canonical chosen visual
- The exact latest owner-approved still image from ChatGPT conversation: `космический_вихрь_medeus.png` (not earlier V1/V3 nor earlier generated revisions).
- Dimension 1448 x 1086 RGB PNG. SHA256 `773f67be7fea7fb8b3dd63b88f58dd55d01e82b0724ed3098db317a8d4f8d5b6`.
- Contains "MEDEUS" and "ASK WHAT MATTERS" at the top, central deep purple sphere with closed luminous internal material and smoky full-perimeter glow, no orbit tracks or side-corner text, left/right small planets, and LOWER mic (roughly 706,830) with its own "SPEAK" subline.
- **Original image bytes preserved exactly**, not regenerated, recropped, repainted or re-encoded. The GitHub binary blob is `da31f9de8c27a61d4821e86a789d2e21de9257e2`, independently verified against local Git blob SHA1. New path `src/assets/MEDEUS_MASTER_VISUAL_V4_APPROVED.png` committed through tree/commit/ref `bf3eaa483e34100f4a79a337038ea832403c5bd0`.
- Immutable historical V3 `src/assets/MEDEUS_MASTER_VISUAL_V3_NO_CAPTIONS.png` SHA256 `9aac52baeac03d61a35ea9809d3580128952de1ae14d77f43c97a5fb7585c50d` remains in repo along with V2 backup and V1 metadata.

## Website implementation
Repository `MrPenser/medeus-master-asset`, default branch main:
- `src/lib/medeus/asset.ts` `d316bf3c6309e32d2b2ffd0c51335be405e3db6e`: imports V4 master and verifies its SHA-256 at runtime before rendering. Declares 1448x1086 and V4 source orb position `cx=704, cy=420, r=224`. V3 reclassified as unchanged backup.
- `src/lib/medeus/presentation.ts` `51c3aac16d4bacc08af829159154ac70544921ce`: lower microphone `x=706,y=830,r=56`, answerY=712, preserves source pixels, no graphic/label masks.
- `src/lib/medeus/orb-field.ts` `8835d822e3b21359545e42f127f3ff98d6e677e5`: active V4 shader now samples the **exact V4 source image** (`vec3 authentic=tex(sourceP).rgb;`) for the whole sphere, replacing the synthetic solid pearl body previously seen in V3.9.6. Retains slow organic, ±1.2%-clamped breathing and one physical outward-only click wave; localized damped pointer distortion and small lilac click/hover luminance. New low-opacity, irregular nonperiodic lilac **smoky haze along the full outer perimeter**, bounded by radius 1.087 of the orb, no drawn rings/axes/particle spokes. **NO planetary rotating texture/UV** (the previous ring-stripe defect remains suppressed). Historic `?surface=classic`, `?volume=off`, `?core=off`, `?breath=off` controls retained.
- Existing `MedeusStage.tsx` runtime stays intact: desktop image panorama from approved V4 asset, source-aligned big orb and separate mic GPU canvases; independent microphone click/hover/voice functionality; all ten FSM states; pointer gestures and text/keyboard input. Mobile has separately drawn single HTML brand and a one-pass side-only source nebula background, avoiding baked duplicate text and old mic ghost.
- `src/lib/medeus/master-v2.test.ts` `daaad741e1d484f89b2e92179df6370bceafc514`: tests exact new PNG hash, all backup hashes, image dimensions, V4 geometry and 10 FSM.
- `src/lib/medeus/core-flow.test.ts` `16b9e529e50336fbcf7fe30aa99d7da8c459743d`: tests native V4 source material, circumferential smoky edge, no spin, gentle contact/one-way click, source custody, mic independence.
- `src/lib/medeus/mobile-layout.test.ts` `ef24da7d7f675bdd0d0030b76f3ec8603cfafdf2`, final `64dbc5e74c9ecd323db7a9a680f5dc00172ebb43`: uses actual V4 coords and verifies intended 2-source-pixel x-offset of mic from orb, allowing correctly aligned touch canvas on mobile. Prior test failure was an obsolete zero-offset assumption, not a demonstrated product failure.
- Workflow `.github/workflows/medeus-liquid-orb-qa.yml` commit `563a74f0938a48d189c9c1dc45ba41ec945b63b1`: GLSL ES100 orb/mic compile, new approved-image hash, V3/V2 image custody, V4 text-free/mobile/fallback/hover/click conditions, Bun/Vite build and unit tests.

## Evidence and gates
- Current website HEAD `64dbc5e74c9ecd323db7a9a680f5dc00172ebb43`.
- GitHub Actions run `38443949668`: **completed SUCCESS**, both `shader` and `site` jobs passed, GLSL ES100 orb/mic valid, build passed, **60/60 tests PASS in 10 suites**.
- Lovable project `76dd8168-469d-4edb-88f6-f313be1c1de8` reports `ready`, latest_commit_sha matches same HEAD after separate verification. Preview: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/
- Lovable production `is_published=false` as last verified. **Do not claim this was publicly deployed.** User can inspect fully integrated preview first; production publishing is a distinct stage. No ASTRADELIA backend or economic forecasting claimed.
- `RECALL_DISPOSITION=EXTEND_AND_SUPERSEDE_VISUAL_ONLY`, `ASSET_CUSTODY=PASS`, `SOURCE_QA=PASS`, `LOVABLE_SYNC=PASS`; `REAL_DESKTOP_MOBILE_VISUAL_QA=PENDING`, `USER_VISUAL_SIGNOFF=PENDING`, `STAGE_COMPLETE=FALSE`.

## Next
- Real browser/phone check at rest for 20–40s plus hovered core, clicked core, microphone hover/click, compact Android/iOS portrait and desktop ultra-wide, with particular attention to sharp image fidelity, no duplicate baked lettering, lower mic hit coordinate, no static core hole, and no visible fake orbit or seam. User approval necessary to lock V4 production visual.
