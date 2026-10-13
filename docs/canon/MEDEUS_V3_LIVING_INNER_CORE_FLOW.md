# MEDEUS V3.1 — Living Inner-Ocean Material Turnover

Status: SOURCE_IMPLEMENTED / GLSL_ES100_PASS / BUILD_PASS / 38_OF_38_TESTS_PASS / LOVABLE_SYNC_VERIFIED / USER_VISUAL_ACCEPTANCE_PENDING
Date: 2026-10-13

## User report and constraints
After fixing V3 microphone hover and click, the user reported: "сфера. дышит но внутри какбудто зияет огромная статичная дыра" and explicitly ordered autonomous SOURCE-CODE MOVEMENT ONLY. "не рисуй мне здесь больше ... только вноси в код изменения движений". Do NOT generate or replace an image, do NOT paint new light objects, haze, circles, orbit tracks, cosmetic stars, or decorative rings.

## Root cause from verified source and pixel inspection
- Central orb source is the immutable V3 PNG. The bright near-white core is baked into the approved image. Raster center at source (836,403) is near RGB(1,1,1); the lowest-contrast aperture appears static when only outer membrane and a small state-specific UV drift move.
- Previous oceanBreath updated radius, underwater pBelow scale and membrane normal. Former sampleOrganicState per-state drift (typically |off| about .02–.08 normalized units) could not adequately transport authentic source pixels across the central static white region.
- Changing the master would violate V3. Instead relocate the optical **material sampling coordinates** over time and feed surrounding genuine V3 material into central image.

## Exact implemented change
- Private site repo MrPenser/medeus-master-asset:
  - src/lib/medeus/orb-field.ts commit `087781f7417e2184e0bde0308704ab92f03f76b2`: `uCoreFlow` optional flag. GLSL `innerOceanCurrent(p,T)` uses TWO independent advected, non-axis-aligned procedural noise fields, motion rates .092/.056 and .062/.083. Only the central material coordinates `pBelow` are displaced, with a wide, feathered `1-smoothstep(.23,.78,length(pBelow))` mask. Additionally `innerOceanDonor(T)` samples real V3 texels along a shifting irregular non-orbital path from nearby center-adjacent area, mixing `(.24+.36*aperture)*exchange*uMotion` into the exposed bright core, feathering to zero by radius ~.61. This replaces the static optical aperture with continually exchanging original ocean material. The 10 original organic state functions, classic state code, outer contour, hover and one-way touch ring remain unchanged. No overlay or synthetic center color.
  - src/components/medeus/MedeusStage.tsx commit `bdf56f095432b8a481322ae45a3d292c2b2ffe8c`: new internal flow **ON BY DEFAULT**, `?core=off` disables just the inner-core turnover for clean before/after comparison while keeping accepted breathing, microphone hover/press and state machine.
  - src/lib/medeus/core-flow.test.ts commit `0c792f4512f2bb489efaf9fd45bb3ea8cebdd8ec`: 4 tests check source-based advective flow, no orbital/trigonometric repeating geometry, feathered center, rollback and microphone independence.
  - .github/workflows/medeus-liquid-orb-qa.yml commit `d1afdd562ff1a0a98b7d701f7da340a02d5105a7`: enforce GLSL movement fields / restoration flag / V3 master hash / ten-state constraints / microphone behavior. GitHub Actions run `38366441437`: 2 shaders GLSL ES100 PASS, Vite production build PASS, all **38/38 tests PASS** across 9 test suites.
- Lovable project 76dd8168-469d-4edb-88f6-f313be1c1de8 status Ready at source SHA `d1afdd562ff1a0a98b7d701f7da340a02d5105a7`.

## Pixel-based mathematical sanity check (not browser acceptance)
Sampled original approved V3 original from known SHA256-matching file at (836,403); base center luminosity ≈ 0.996. Offline evaluation of shader's time-advected current + original-texel donor core mixing for time t=0,6,12,18,24,30,40 gives approximate center luminance .471/.569/.687/.839/.636/.597/.663 (sampling approximated on CPU). This demonstrates materially non-static optical content relative to the static source; it is NOT a rendering screenshot and not yet a GPU visual-perception guarantee.

## Invariants / signoff
- Source PNG **unchanged**: V3 SHA256 `9aac52baeac03d61a35ea9809d3580128952de1ae14d77f43c97a5fb7585c50d`, 1672x941. V1/V2 backup untouched.
- Main sphere autonomous breath V1.3, hover inertial membrane, one-way physical outward crest, ten canonical states, independent microphone planet liquid hover+press and speech/text channels unchanged.
- User visual acceptance: PENDING. On comparison `?core=off` returns previous static V3 center for A/B, not a different picture.
- **No new images or decorative visual props**; all changes are to dynamic optical sampling and motion only.

Default preview: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/
Legacy center A/B: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/?core=off
