# MEDEUS V3.7 — homogeneous white-lilac pearl water sphere

Date: 2026-10-13
Authority: latest explicit user's instructions supersede the V3.6 visual approach.
Decision: EXTEND the existing sphere interaction system; SUPERSEDE the cosmic-source appearance of the big sphere ONLY.
Status: SOURCE_QA=PASS, LOVABLE_SYNC=PASS, USER_VISUAL_SIGNOFF=PENDING, STAGE_COMPLETE=FALSE.

## User request
- "слушай это не то. замени цвет сферы на однородный переливающийся перламутровый бело лиловый с водной поверхностью как раньше и эффектами при наведении и и нажатии более выраженными" followed by explicit permission "сама".
- No new still image or text labels. The visual result is a runtime WebGL procedural material for the big sphere. Do not call image_gen or modify art files.
- Keep no rotation/no visible orbital tracks. Preserve gentle breathing from V3.6, independent microphone, 10 FSM states and responsive interaction channels.
- Colors requested specifically soft white/lilac pearl, uniform water, no cosmic dark hole.

## Live implementation
- Website repository: `MrPenser/medeus-master-asset`.
- `src/lib/medeus/orb-field.ts` commit `f68d3835c55538a7aa77ae85f6c3ecf7c17d5caa`: adds `pearlSphereColor` with white, pastel lilac and lavender source-independent color palette; gently evolving FBM pearl value, 3D spherical-cap normal perturbed by water height, broad soft specular and fresnel/hover/click glints. Explicit light-color minimum prevents a dark central aperture. No source-image texture/color sampling used for the default new pearl material; existing original V3 PNG remains a separate immutable source for site/backups/rollback/microphone.
- `oceanHeight` in default globe now has subtle resting water undulation (0.45 of original gyre/detail) and stronger hover bulge, .165 vs .104 height; physical click single outward expanding crest .145 vs .080, radius speed .84 vs .78, monotonic age; no inward rebound. Contour hover amplitude .050 vs .033; optical response default refraction .018 vs .006 and lens .042 vs .014. Legacy fallback retains previous values with `?volume=off` or `?core=off`.
- Gentle non-identical CPU breath unchanged, ±1.2% maximum from `breathing.ts`, `?breath=off` available. Three-axis planet spin remains **removed**.
- Default `uVolumeFlow` controls pearl material despite historical name. `?surface=classic` preserves original classic optical rendering.
- `src/lib/medeus/core-flow.test.ts` commit `5a494801b995b47dde389302a01620b9cf6d31ea`: validates palette, no image source in pearl shader, single outward click, hover strength, rollback, 10 states, PNG SHA, mic behavior.
- `.github/workflows/medeus-liquid-orb-qa.yml` commit `7b3741bc8a5649185820a5f0440812166cb91df0`: source and actual GLSL ES100 compilation gates, both big orb and independent microphone, PNG immutable custody.
- Latest website HEAD: `7b3741bc8a5649185820a5f0440812166cb91df0`.
- GitHub Actions `38377339488`: shader job PASS; site build PASS; **39/39 tests passed (9 suites)**.
- Lovable project `76dd8168-469d-4edb-88f6-f313be1c1de8`, ready, agentFinished=true, latest_commit_sha exactly `7b3741bc8a5649185820a5f0440812166cb91df0` after verified separate read.
- Preview: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/

## Immutability and scope
- Source PNG `src/assets/MEDEUS_MASTER_VISUAL_V3_NO_CAPTIONS.png`: SHA256 `9aac52baeac03d61a35ea9809d3580128952de1ae14d77f43c97a5fb7585c50d` **unchanged**. This is no longer the default big sphere optical appearance; it remains the original scene source and historical optical fallback.
- Microphone separately rendered, not modified. No phantom big-orb click on mic click. Desktop/mobile scene and surrounding stars/planets/text unchanged.
- 10 FSM states preserved; pearl does not currently use organic state-colored texture in default. User did not ask to restore visible state differentiation. Continue only after visual approval or additional user direction.
- If user rejects result, `?volume=off` gives preceding liquid/source-sphere look for comparison, and `?surface=classic` retains classic.

## Strict acceptance
- `SOURCE_QA=PASS`, `WEBGL_GLSL=PASS`, `UNIT_TESTS_39_39=PASS`, `LOVABLE_SYNC=VERIFIED`.
- `USER_VISUAL_SIGNOFF=PENDING`, `HOVER_CLICK_VISUAL_ACCEPTANCE=PENDING`, `MOBILE_REAL_GPU_QA=PENDING`, `STAGE_COMPLETE=FALSE`.
- Real desktop/mobile observation at idle, hover, physical click ~20-40s is still required. CI tests do not establish pearl aesthetic or physical look to user.
