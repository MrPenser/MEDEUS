# MEDEUS V3.9 — responsive mobile scene and touch GPU adaptation

Date: 2026-10-13
User mandate: "Адапт для мобильных".
Disposition: EXTEND existing V3.9 verified pearlescent internal-light design. Preserve desktop, live state machine, mic independence, exact V3 image, all other approved visual behavior.
Status: SOURCE_QA=PASS / CI=PASS / LOVABLE_SYNC=PENDING_FINAL_VERIFICATION / MOBILE_VISUAL_SIGNOFF=PENDING / STAGE_COMPLETE=FALSE.

## Code changes
Website repo `MrPenser/medeus-master-asset` branch `main`.

1. `src/lib/medeus/mobile-layout.ts` CREATED commit `3d90c7b281971332ea0d1fcd37660fd90187045b`: pure mobile `mobileSceneGeometry` computes one isotropic transform for the verified V3 background, pearl sphere, mic, and response, limited by available viewport width and height, portrait/landscape safe top and bottom, with optional additional safe-area insets. Explicitly positions answer between lower orb edge and upper mic edge. Desktop transform stays unchanged.
2. `src/components/medeus/MedeusStage.tsx` commits `6c1755e917a1eddc4f0533f425a5fccfe733b44a` and `a94315a12b0f288f893551300b944ad5aaf606ad`: uses the shared geometry exclusively on `mobile`; desktop still uses original `fit(vw,vh)`. Orb texture, scene, microphone and input overlay share transform; mobile answer baseline avoids orb/mic overlap and respects `visualViewport` height while the keyboard is present. Restores existing original "ASK WHAT MATTERS" title in mobile upper visible safe area because the panoramic source title otherwise crops above the screen. Transparent native mobile textarea clip path tightened from 49% to 45% of the ORB_BOX square, aligning actual tappable area with visible sphere. Phone touch down/drag drives the already approved water hover for the touched orb OR the independent microphone, resetting on up/cancel without phantom orb ripple from mic. Native keyboard focus / speech routing remain untouched. `visualViewport` resize listener added for orientation/keyboard changes; resize retains its existing focused-keyboard guard to avoid dismissing IME. Mobile-only rendering throttled to approximately 30–36 visual FPS and DPR capped to 1.25; desktop remains original 1.5 DPR/unthrottled.
3. `src/lib/medeus/mobile-field.ts` commit `21136f1b967533cfb94c3f2bf5d03532dbcbeff2`: mobile panorama DPR capped at 1.25 to match the WebGL/fog buffers. The exact V3 bitmap derivative continues to render without generated substitute art or new overlays.
4. `src/lib/medeus/mobile-layout.test.ts` CREATED commit `e6ff012ef4d0e52f3679e1560e9020d01f2af090`: tests geometry across 10 viewport sizes (small phones, tall phones, landscape) + top/bottom safe-area insets + shared coordinate/answer transform + keyboard input + touch/mic separateness + reduced GPU rendering.
5. `.github/workflows/medeus-liquid-orb-qa.yml` commit `c99b38dbc0bbab298c0bcc5dc5de443229a553b7`: enforces mobile geometry/interaction/DPR invariants while preserving the V3.9 GLSL ES100 proof and all 10 cognitive states.

## Verified evidence
- Final website source HEAD `c99b38dbc0bbab298c0bcc5dc5de443229a553b7`.
- GitHub Actions run `38390516042` completed **SUCCESS** for both `shader` and `site`; GLSL ES100 fragment and vertex for sphere and mic PASS; production Bun/Vite build PASS; **53/53 unit tests** across **10 suites** PASS, including mobile geometry and touches. This is code/test evidence, not actual responsive browser-device screenshot acceptance.
- Lovable project `76dd8168-469d-4edb-88f6-f313be1c1de8`, preview https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/. Verify latest mirrored commit separately; a `ready` status alone is not proof of the final mirror SHA.

## Non-negotiable preserved constraints
- Locked master `src/assets/MEDEUS_MASTER_VISUAL_V3_NO_CAPTIONS.png` remains bytes unchanged (SHA256 `9aac52baeac03d61a35ea9809d3580128952de1ae14d77f43c97a5fb7585c50d`).
- V3.9 pearlescent internally illuminated sphere: no surface mirror glare, no axial rotation, subtle breathing, strong real hover and single outward physical click wave. Unchanged orb shader, mic shader, 10 FSM states, voice/keyboard demo behavior. No new visual assets or added futuristic panels.
- Desktop scene and pointer behavior unchanged. The site remains a demo, not a forecasting or conversational backend integration. Preserve `?volume=off`, `?core=off`, `?breath=off`, `?surface=classic` rollback.

## Strict gate
`SOURCE_QA=PASS`, `GLSL_ES100=PASS`, `SITE_BUILD=PASS`, `UNIT_TESTS=53_53_PASS`.
`LOVABLE_SYNC=PENDING_FINAL_CHECK`, `REAL_ANDROID_DEVICE_QA=PENDING`, `REAL_IOS_DEVICE_QA=PENDING`, `LANDSCAPE_VISUAL_QA=PENDING`, `USER_VISUAL_ACCEPTANCE=PENDING`, `STAGE_COMPLETE=FALSE`.
Next: observe portrait and landscape mobile browser views (including soft keyboard, mic tap, water touch, no input dismissal and safe-area visibility) before owner acceptance.
