# MEDEUS V3.8 — volumetric optical pearl correction

Date: 2026-10-13
Decision: EXTEND the pearl-water sphere from V3.7; user visual feedback rejects its flat appearance. Do not treat V3.7 as visually approved.
User feedback: "говно екак будто 2d" (looks like 2D).
Status: SOURCE_QA=PASS / LOVABLE_MIRROR=VERIFIED / VISUAL_ACCEPTANCE=PENDING / STAGE_COMPLETE=FALSE.

## Recall and diagnosis
- V3.7 had a near-uniform base illumination (.85 + weak key/fill), a globally flat-bright color clamp (minimum RGB around .75), and a broad 14% transparent edge. These factors erase spherical curvature and make the sphere look like a flat pearl disc.
- User did not authorize generating another image: keep all changes strictly in website shader source.
- Supersede only the look of V3.7 big-sphere pearl material; preserve the white-lilac material direction, stronger real hover/click, gentle non-identical breath, no rotation, unchanged mic, 10 FSM states, and source V3 master.

## Changes
Website repo `MrPenser/medeus-master-asset`:
- Shader `src/lib/medeus/orb-field.ts`, code commit `5e37cef24188eb8b3b9212ef4b77677ece2da685` with immediate GLSL ES100 reserved-word repair `47cba6d083bed72e0d09b3d5a5320385d6161901`.
- `pearlSphereColor` now models a spherical-cap geometry normal (z = sqrt(1 - normalized radius squared)), a separate fluid normal perturbed by physical water slope, directional key/fill lights, body-light contrast and thickness-aware silhouette shading. This is an **optical approximation of 3D depth in a fragment shader**, not a new physical 3-D triangle mesh.
- Two separately refracted internal FBM layers move subtly and contribute to a thickness-scattering pearl body using the front hemisphere z coordinate. `refract(-view, geometryNormal, .78)` affects layered parallax; no orbital-axis UV mapping or radial iris geometry.
- White-lilac pearl tones remain, but a richer lilac shadow under real directional lighting increases visible volume. Two distinct water highlight lobes track the surface normal. V3.7's broad bright global clamp was replaced with a low safety floor (RGB [.30,.23,.43]); source color is not sampled in default V3.8.
- Replaced default 14% alpha feather with 2.6% edge softness (`smoothstep(.974*rim,rim,r)`) to make the curved limb read like glass/water. Historical fallback keeps its .86 feather.
- More-visible physical hover and only one nonreversing click crest from V3.7 are preserved. Soft ±1.2% breathing stays, no planet rotation or texture stretching.
- No modification to `src/assets/MEDEUS_MASTER_VISUAL_V3_NO_CAPTIONS.png` (SHA256 `9aac52baeac03d61a35ea9809d3580128952de1ae14d77f43c97a5fb7585c50d`). No microphone modifications.
- V3.8 tests `src/lib/medeus/core-flow.test.ts` commit `2d06c13d56680705d9cbe5f4fa5e48f27d5e40c5`: 3D normal / separate refracted layers / directional lighting / sharp rim / numerical illuminated-side versus shadow-side difference gate, retention of mic, 10 FSM, original art and click. CI workflow `64f5a5c1e2e1ce4f55c76cdf267708d345d8b8aa` enforces these source and shader invariants.

## Verified results
- Website GitHub HEAD: `47cba6d083bed72e0d09b3d5a5320385d6161901`.
- Actions run `38378407498`, completed success: real GLSL ES100 WebGL orb and mic shader compilation PASS; Bun/Vite production site build PASS, 40/40 tests passed across 9 suites.
- The first intermediate build had `active`, which GLSL ES100 reserves. Renamed to `clickAlive` in `47cba6d0`; final shader compilation success verified. Intermediate CI failures do not represent final source status.
- Lovable project `76dd8168-469d-4edb-88f6-f313be1c1de8`, ready, latest_commit_sha equals final website SHA.
- Preview https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/
- Rollback `?volume=off`, `?core=off`, `?surface=classic`, `?breath=off` unchanged.

## Acceptance boundaries
- `SOURCE_QA=PASS`, `CI=PASS`, `LOVABLE_SYNC=PASS`.
- `TRUE_3D_MESH=NOT_IMPLEMENTED` (fragment optical model). `USER_VISUAL_SIGNOFF=PENDING`, `ACTUAL_DEPTH_VISUAL_SIGNOFF=PENDING`, `MOBILE_REAL_GPU_QA=PENDING`, `STAGE_COMPLETE=FALSE`.
- Do not promote or claim V3.8 visual satisfaction from test counts alone. Inspect static vs hover vs physical click on desktop/mobile ~20-40s for convincing dimensional depth, clean pearl surface and no dark central hole, fake rings, stripes, or excessive flow. If 3D is still unconvincing, a genuinely geometry-backed sphere/renderer is a distinct considered next step; it is not yet built.
