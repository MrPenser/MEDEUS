# MEDEUS V3.2 — CONTINUATION / INHERITANCE HANDOFF
Date: 2026-10-13
Type: user-commanded project transfer (Передача)
Authority: latest explicit user instructions over earlier experimental descriptions.

## 1. Source authority and verified live state
- Primary website source: `MrPenser/medeus-master-asset`.
- Canon and handoff repository: `MrPenser/MEDEUS`.
- Current site HEAD: `8130f4aa59188f533fb8c4879fad3fcfe1bfb29b`.
- Lovable project ID: `76dd8168-469d-4edb-88f6-f313be1c1de8`; status `ready`, last mirrored commit `8130f4aa59188f533fb8c4879fad3fcfe1bfb29b` (verified via current project lookup, not assumed).
- Preview: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/
- Latest GitHub Actions run `38367445856` for same site HEAD: GLSL ES100 shader job PASS, Bun/Vite site build PASS, **38/38 automated tests PASS** (9 suites).
- Distinguish `SOURCE_QA=PASS` and `LOVABLE_SYNC=PASS` from `USER_VISUAL_SIGNOFF=NOT_GRANTED`.
- No user-facing code/edit completion was requested by this transfer command; this handoff records exact current state and pending work.

## 2. Approved and frozen baseline
- Master **V3** image only: `src/assets/MEDEUS_MASTER_VISUAL_V3_NO_CAPTIONS.png`, verified immutable SHA256 `9aac52baeac03d61a35ea9809d3580128952de1ae14d77f43c97a5fb7585c50d`, 1672 x 941 pixels. Old V1/V2 remain as backup, not active. Do not generate, replace, recolor or paint any image, and do not change the master hash.
- Source pixel sphere geometry: `cx=836, cy=403, r=224`.
- Mic in `src/lib/medeus/presentation.ts`: `micX=836, micY=810, micHitRadius=60`.
- Approved interactive shell: non-identical idle breathing, fluid hover attraction/inertia, **one outward-only** real-contact wave (no inward rebound or oscillating ring train).
- Independently responding microphone planet: 95ms-follow/180ms-release hover, localized press wave, voice activation; mic click must NOT cause a phantom central-orb wave. Mic behavior user accepted with **"фикс"**.
- Exactly 10 cognitive FSM states; keep classic optical fallback `?surface=classic`, keyboard, voice and response channels, desktop/mobile layout.
- User has **REJECTED** all visible orbital track lines, surface pox/stars, glow dust, rare crystalline dashes, spoked/petal/triangle patterns, fog, haze and artistic image replacements. Explicit instruction "**не рисуй мне здесь больше ... только вноси в код изменения движений**" overrides any creative visual concepts.

## 3. Open product defect and latest acceptance target
User rejected prior center-only V3.1 motion as "**это просто сфинкр космоса ... убери дырку!!!**".
Latest direction: "**да по всей сфере шейдер. а не только по центру. и пусть будет общее движение вокруг разных собственных орбитальных осей (оси не прорисовывать естественно...**".

Translate to acceptance contract:
1. The former separate central light aperture/hole must cease to read as a stationary, circular opening or a moving iris. Whole sphere should feel like one cohesive living ocean, not a halo around a center patch.
2. Motion applies continuously **across the entire liquid sphere**, including center and off-center regions, not limited by any radial core mask.
3. Implement **several independently oriented, tilted, volumetric rotation/transport axes**, with different slowly changing angular velocities and positions, **none drawn as geometry**. Avoid simple uniform screen-plane spinning, synchronized concentric orbits, fixed vortex singularities and symmetric angular spokes.
4. Appearance must come ONLY from advecting, warping and mixing authentic V3 source pixels; never create a new flat core, static synthesized color, dot/star layer or external planet/text bleed. Do not blur or muddy the scene.
5. Preserve approved original liquid membrane breathing, its hover and physical click, all ten states, V3 master, separate mic, old text/voice channels and layout.
6. Do not call success from static source assertions alone: visual QA (desktop + mobile, rest and interaction, 20–40 seconds) must confirm no aperture/iris after implementation. If not confirmed, remain NOT_ACCEPTED.

## 4. Actual current V3.2 implementation — IMPORTANT distinction
Current site HEAD **already contains** a first V3.2 `uVolumeFlow` implementation:
- `src/lib/medeus/orb-field.ts` at blob SHA `36d891407ef4040e36079eaa77c14b638a93d8d8`. Contains GLSL `oceanVolumeCurrent(p,T)` with two advected noise fields and non-axis-aligned shear, `oceanLayerA(p,T)`, `oceanLayerB(p,T)` sampling original V3 material, `oceanInteriorMaterial(q)` preventing adjacent-planet/text sampling, and `whitePlateau` from per-pixel source COLOR instead of a central radius mask. New flow is NOT multiplied by a center-radius envelope.
- `src/components/medeus/MedeusStage.tsx` at blob SHA `79ebad95e3f61319eff7135e442148c34d65029c`: `livingVolumeEnabled.current = params.get("volume") !== "off" && params.get("core") !== "off"`; frame passes `volumeFlow: liquidSurface.current && livingVolumeEnabled.current`. Both `?volume=off` and legacy `?core=off` compare to the earlier V3 image motion; default is V3.2 flow.
- `src/lib/medeus/core-flow.test.ts` blob `a30fb970261705c5d122474ff4398d87919cc7b4`: 4 V3.2 tests verify absence of previous radial-core masks and whole-sphere source-material mixing, classic rollback, mic preservation.
- CI `.github/workflows/medeus-liquid-orb-qa.yml` blob `9a556ded2e1c4b245fa754fcdc615942cd21ee30`.
- Historical site commit chain: `641511dbfea4b45aa542fdf76642173d7f70a89f` whole-sphere rewrite; `bdfdbf9678d8505e55bd19136e5daf7746a8ca6e` stage enablement; `6aef6b91612e831a9846620b141f39177d1d9dfa` bound sampling to sphere; `92bdcd81618d7bade8deb9edb0d40d728abc2fb0` new tests; `8130f4aa59188f533fb8c4879fad3fcfe1bfb29b` final QA gate, PASS.

**Critical gap:** current `oceanVolumeCurrent` is an advected NOISE/SHEAR vector field, and the two layer offsets are irregular displacements. This is **NOT** an explicitly designed mixture of multiple tilted rotation axes as requested in the latest user message. V3.2 passes automated tests but user has NOT visually accepted it. Therefore `FULL_SPHERE_FLOW_SOURCE=IMPLEMENTED`, `MULTI_AXIS_DYNAMICS=REQUIRED_NOT_YET_IMPLEMENTED`, `HOLE_REMOVED_VISUALLY=UNVERIFIED`, `STAGE_COMPLETE=FALSE`.

## 5. Next engineer's required implementation
- Start from current site HEAD, not V3.1 `uCoreFlow` or prior GitHub/Lovable preview.
- Replace or extend only the **liquid-mode optical displacement** in `orb-field.ts` with 3 (or more) **nonsynchronous, differently tilted axis** components. Potential implementation: use a normalized hemisphere material frame and axis-specific tangent velocity fields, blended with smooth off-center supports and independently drifting rates. If using 3-D rotation or Rodrigues formula, carefully bound UV projections to the original orb and avoid pulling background objects. Spatial advection must remain smooth and non-singular at every axis center. Never DRAW axis lines, circles or orbits.
- Treat source-born near-white static center by exchanging authentic V3 material across the entire sphere; no central circular radius envelope. Avoid over-darkening into a different static black hole.
- Keep or improve `oceanInteriorMaterial` sampling bounds and `?volume=off` rollback.
- Expand `core-flow.test.ts` and shader QA gates to verify multiple independent axis definitions and weighted per-axis motion as well as no core-radius mask, no periodic/stationary center, classic rollback, exact master hash, 10 FSM and independent microphone input.
- Validate WebGL ES100, desktop/mobile 20–40s animation including hover/click, Bun/Vite build and all tests. Only then submit preview for visual user approval. No image-generation tool.

## 6. Handoff status (strict)
`HANDOFF_READY=TRUE` (this document contains exact authority, paths, commits, QA and next task).
`CONTINUATION_READY=TRUE` (can continue safely on current HEAD).
`SELF_CONTAINED=TRUE_FOR_THIS_SCOPE` (source still authoritative, never replace with summary).
`USER_VISUAL_SIGNOFF=FALSE`.
`MULTI_AXIS_ROTATION_COMPLETE=FALSE`.
`NO_STATIC_HOLE_USER_ACCEPTANCE=FALSE`.
`FULL_CORE_GATE=OPEN_FOR_DEVELOPMENT_ONLY`, `STAGE_COMPLETE=FALSE`.

Do NOT mutate a technical source file during a handoff-only command. Next user instruction should drive implementation.
