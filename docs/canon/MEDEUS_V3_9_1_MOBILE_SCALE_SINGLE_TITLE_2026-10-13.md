# MEDEUS V3.9.1 — Mobile sphere scale and single header repair
Date: 2026-10-13
Status: SOURCE_QA=PASS, CI=PASS, LOVABLE_SYNC=VERIFIED, USER_MOBILE_VISUAL_SIGNOFF=PENDING, STAGE_COMPLETE=FALSE.

## User-reported failure and recall
- User on mobile: "Слишком большая сфера тект сверху накладывается на название".
- Latest prior inherited mobile baseline: GitHub website repo `MrPenser/medeus-master-asset` HEAD `c99b38dbc0bbab298c0bcc5dc5de443229a553b7`, Lovable project `76dd8168-469d-4edb-88f6-f313be1c1de8`.
- Diagnosis by source inspection:
  - Mobile `mobileSceneGeometry` let a globe reach nearly 94% viewport width in portrait.
  - `paintMobileCosmicField` drew the ENTIRE source image once as a cover and a second time aligned with globe. That yielded an enormous baked original orb underneath the live WebGL globe and duplicate source headline.
  - `MedeusStage.tsx` independently rendered a CSS overlay `ASK WHAT MATTERS` making the original text overlap and appear doubled.
- Decision: `EXTEND` mobile-only layout/rendering, `SUPERSEDE` earlier full-image cover approach. No new image, no source PNG rewrite, no changes to desktop, mic, voice, 10 FSM or accepted V3.9 pearl inner emitter.

## Implementation
Website GitHub branch `main`:
- `src/lib/medeus/mobile-layout.ts` commit `ab5e9e288f74d1b825ef2010ea5a8962b77089e3`: portrait sphere diameter capped at 76% of viewport width (landscape 66% width, often height bound); title clear zone increased to 86px (portrait) or 44px (landscape); bottom reserved 34/18px. Globe positioned nearer 42% height while preserving shared isotropic source/orb/mic/response transform.
- `src/lib/medeus/mobile-field.ts` commit `11f5c8b49bcfe3944cdf363d4d672dddfd578b7c`: mobile cover samples *only a lateral cosmos section* of the original V3 bitmap, explicitly avoiding the baked giant orb and upper heading. Aligned content samples original source only below original title strip (top ~7.5%), so only ONE top title remains: the responsive CSS element already in `MedeusStage.tsx`. Crop is runtime mobile-only sampling of approved asset (not mutation or regeneration). The orb and mic are still rendered above aligned content at exactly matched coordinate transform. Full desktop bitmap unchanged.
- `src/lib/medeus/mobile-layout.test.ts` commit `1c20ddb7ec4100c791830663ba1db8fe25c5c70d`: 10 phone/landscape geometries, 76% portrait cap, title clearance, safe areas, mic/answer placement, sampling-only original image, unique HTML title, original interaction invariants.
- `.github/workflows/medeus-liquid-orb-qa.yml` commit `ca7bdb1eb0d1810a96e6ea931d04c663200a64be`, and harness repair `b041a253cdee783fab57be0da562879ba074f657`: assert smaller globe, side-cosmos cover + aligned content crop, unique heading, original master image hash, stage/voice/mic states, mobile GPU budget. A prior CI run failed because an obsolete string check expected one-line `c.drawImage(image` while the new image draw uses multiple lines (test harness issue, not shader failure). Final harness accepts source-preserving multiline call.

## Verified evidence
- Final source HEAD `b041a253cdee783fab57be0da562879ba074f657`.
- GitHub Actions run `38403198586` completed SUCCESS: GLSL ES100 orb and mic shaders PASS; Bun/Vite build PASS; **54/54 tests PASS** (10 suites).
- Lovable project `76dd8168-469d-4edb-88f6-f313be1c1de8` status `ready`, latest_commit_sha exactly `b041a253cdee783fab57be0da562879ba074f657`, independently verified.
- Live preview https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/
- Original master PNG `src/assets/MEDEUS_MASTER_VISUAL_V3_NO_CAPTIONS.png` SHA256 `9aac52baeac03d61a35ea9809d3580128952de1ae14d77f43c97a5fb7585c50d` unchanged. Desktop mode source/geometry untouched.

## Hard boundaries
- `SOURCE_QA=PASS`, `CI=PASS`, `LOVABLE_SYNC=PASS`.
- `MOBILE_REAL_BROWSER_VISUAL_SIGNOFF=PENDING`, `ANDROID_IOS_GPU_QA=PENDING`, `STAGE_COMPLETE=FALSE`.
- User to observe portrait and landscape mobile: exactly one headline at top; smaller orb not touching it; independent smaller mic below; keyboard doesn't dismiss on tapping orb; one click wave from real contact. Code/test success is NOT an observed visual acceptance.
