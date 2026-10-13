# MEDEUS V3.4 — repair of user-rejected invisible spin and central iris
Date: 2026-10-13
Classification: EXTEND of V3.2 / SUPERSEDE only V3.3 failed optical dynamics.
Authority: user's live browser feedback overrides earlier source-only PASS.

## User visual failure before repair
- V3.3 user report: "мы вернулись к дыре. вращения сферы как планеты- нет! шецдер не виден".
- Record V3.3 as USER_VISUAL_FAIL, despite 38/38 automated tests and shader compilation.
- Direct diagnosis in V3.3 `orb-field.ts`: intended projected 3-D material rotation was attenuated by *0.72 at field creation and *0.68 when sampled, i.e. only ~49% of projected movement. Slow 0.0023–0.0044 rad/s axis rates compounded weak visibility.
- V3.3 baked flat/near-white optical material blended to donors at only 81% even for maximally bright plateau, allowing a stationary-looking bright aperture.
- This diagnosis uses exact code plus user observation; do not claim a quantitative visible result from source-only inspection.

## Website changes
Repository `MrPenser/medeus-master-asset` main:
- `src/lib/medeus/orb-field.ts` code commit `cd4fae1814be5b633b92e948349796fe6b66b44f`.
  - Whole globe original-source optical material now uses full axis-rotated projected coordinates (`return rotated-p+suspended`, applied without attenuation).
  - Three differently tilted 3-D Rodrigues rotation axes with slow independently changing angular rates (`0.017`, `-0.011`, `0.009` rad/s base; no drawn axes/tracks). This is a front-hemisphere source-image optical illusion, NOT proof of a physically complete 360-degree back texture.
  - Liquid drift jitter amplitude dropped to `0.006`; slow donor jitter <= `0.029`. Overall water *motion speed* is low while the whole surface's original light-field landmarks travel.
  - Original V3 white plateau repair samples *three* moving source neighborhoods: `oceanLayerA/B/C`. Weighted source-color donors are sampled only within radius `0.86` to avoid surrounding planets/text; color-based criterion fades white neutral flat pixels across the entire projected globe (no central radial mask) with exchange up to `0.975`. Original source PNG bytes are never edited.
- `src/lib/medeus/core-flow.test.ts` updated in `05aa2a1829b90e91379016242fa488344ac06a6f`:
  - Structural and numerical tests use the declared 3D Rodrigues geometry to assert 20-second globe movement of representative center/edge material points, low angular rate limits, three source donors, source SHA256 and rollbacks.
- `.github/workflows/medeus-liquid-orb-qa.yml` updated in `e61dcb4dc1c0a609dcbe83b5ca2af231a701eca5` with follow-up harness assertion fix `8e9a36c5f82ae8745b5f9c0a872f80ca46f8104b`.
  - Old harness failed when checking obsolete pre-V3.4 whitePlateau formula (CI harness failure, not proven shader compile/product failure).
- Final GitHub website HEAD `8e9a36c5f82ae8745b5f9c0a872f80ca46f8104b`: Actions run `38372328909` completed success; WebGL GLSL ES100 orb/mic compilation PASS, Bun/Vite production build PASS, 38/38 unit tests PASS across 9 suites.

## Immutable project constraints
- V3 exact PNG `src/assets/MEDEUS_MASTER_VISUAL_V3_NO_CAPTIONS.png`, SHA256 `9aac52baeac03d61a35ea9809d3580128952de1ae14d77f43c97a5fb7585c50d`, preserved.
- Approved large-sphere breath, hover and single outward click crest; independent mic hover/press and voice behavior; all ten FSM states, panorama, mobile/desktop, keyboard, localization and response channel unchanged.
- No new image, new static painted material, orbital graphic, ring track, stars, haze or overlays.
- Feature rollback `?volume=off`, `?core=off`; optical classic rollback `?surface=classic`.

## Acceptance & limitations
- `SOURCE_QA=PASS`, `CI=PASS`, `NUMERIC_ROTATION_GATE=PASS`.
- `V3_3_USER_VISUAL=FAIL` (superseded).
- `V3_4_USER_VISUAL_SIGNOFF=PENDING`, `NO_HOLE_VISUAL_PASS=UNVERIFIED`, `DESKTOP_MOBILE_REAL_BROWSER_MOTION_QA=PENDING`, `STAGE_COMPLETE=FALSE`.
- The full original front image is a baked 2D texture. It cannot supply never-photographed backside data. This renderer produces 3D projected motion of source pixels, not a new physically correct 3D globe asset.
- Need user to compare 20-40 seconds at rest, hover and press on desktop/mobile, and confirm the whole-orb spin reads like a planet without center iris, overly strong shader, deformation or seams.
- Lovable project ID `76dd8168-469d-4edb-88f6-f313be1c1de8`, preview https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/. Latest verified mirror must be checked separately from GitHub; GitHub Actions PASS alone does not prove Lovable sync.
