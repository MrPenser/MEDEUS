# MEDEUS V3.5 — native V3 texture and depth; approved 3-axis spin, no wet sheen
Date: 2026-10-13
Status: SOURCE_QA=PASS / LOVABLE_MIRROR=VERIFIED / USER_VISUAL_SIGNOFF=PENDING

## User authority and disposition
- User accepted the planetary spin of V3.4: "вращение норм." Preserve its three tilted axes, angular rates, relative positions, and overall silhouette.
- User rejected the liquid rendering: "но шейдер убери -он плох. верни глубину тестуру прежгней сферы только без дыры"; then explicitly "делай. сама".
- `recall&`: checked previous V3.2 transfer, V3.4 canon, current GitHub sources/tests/CI and synced Lovable project. Classification: **EXTEND** V3.4's accepted planetary motion; **SUPERSEDE** only the unwanted default wet optical presentation. No new image, new 3-D mesh, new microphone, new FSM state or redesign.
- "Remove shader" means remove visually poor extra fluid sheen/distortion, not removal of the GPU pixel-coordinate sampling pipeline required to rotate a locked 2-D V3 master.

## Implemented source
Working repo: `MrPenser/medeus-master-asset` / `main`.
- `src/lib/medeus/orb-field.ts` code commit `de9f1d880a1e9c0da444ad0fe49d15b01dce4963`: `oceanSphereRotation` exactly retains V3.4 3-axis Rodrigues formula and rates. `oceanVolumeCurrent` returns only `oceanSphereRotation(p,T)-p` (no extra moving water noise).
- **Original image authority**: `vec3 originalV3=tex(pBelow).rgb;` supplies almost all DORMANT native sphere texture. `statePresence` retains 10 existing cognitive visual states with subordinate organic motion (DORMANT 0.02, AWARE 0.10, REVEALED 0.08, other states 0.35). Preserves sharp original detail, baked color and native depth rather than replacing ~24% of all pixels with a 3-donor average as V3.4 did.
- **No central iris**: 3 V3-only donor samples `oceanLayerA/B/C` are restricted inside 0.86 sphere radius and weighted toward luminous, structured source pixels. A source-color-based `whitePlateau` restricts replacement to achromatic overexposed parts; `exchange=.92*whitePlateau*uMotion`, with no baseline global mixing and no radial center aperture mask. Source-derived donor luminance receives a limited tonal floor to avoid a black well, not a rendered glow, rings, particle or image replacement.
- **Remove wet shader**: default `uVolumeFlow>.5` has no synthetic specular lamps, fresnel sheen, or broad idle water noise; optical refraction attenuated for default to slopes 0.012 (from 0.056) and hover lens 0.022 (from 0.104). Physical hover/click localized ripples and original breathing remain functional.
- **Historical fallback**: `?volume=off` / `?core=off` retains the pre-V3.5 wet shader and old behavior, `?surface=classic` remains the original classic optical mode. No unrelated mouse/press/mic/voice changes.
- `src/lib/medeus/core-flow.test.ts`: commits `1019682a55972a2f678fc2d911695ac4321f7833`, `d1859f5284bad8eadc7c8b533d5bb0584bc2cbe9`, adds tests for source-fidelity, no default wet sheen, 3-axis/20s numeric position drift, iris removal, PNG hash, ten FSM, separate mic.
- `.github/workflows/medeus-liquid-orb-qa.yml`: commit `5e1bb558c0a966ba58643f516ac09cc5c805726f`, verifies shader compilation, material fidelity, fallback, original immutable master, 10 states, microphone.

## Verification
- Working site HEAD: `d1859f5284bad8eadc7c8b533d5bb0584bc2cbe9`.
- GitHub Actions run `38373966682`: shader job PASS; Bun/Vite site build PASS; **39/39 tests PASS (9 suites)**.
- Lovable project `76dd8168-469d-4edb-88f6-f313be1c1de8`: `ready`, `agentFinished=true`, latest_commit_sha `d1859f5284bad8eadc7c8b533d5bb0584bc2cbe9`; independently matched to GitHub HEAD.
- Preview: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/
- Immutable PNG `src/assets/MEDEUS_MASTER_VISUAL_V3_NO_CAPTIONS.png` SHA256 `9aac52baeac03d61a35ea9809d3580128952de1ae14d77f43c97a5fb7585c50d`, verified by tests and unchanged.

## Evidence boundary / next decision
- `SOURCE_QA=PASS`; `LOVABLE_SYNC=VERIFIED`; `V3_4_ROTATION_USER_APPROVED=TRUE`.
- `V3_4_WET_SHADER_USER_ACCEPTED=FALSE`; `V3_5_NATIVE_TEXTURE_USER_VISUAL_SIGNOFF=PENDING`; `V3_5_NO_HOLE_USER_VISUAL_SIGNOFF=PENDING`; `MOBILE_REAL_GPU_QA=PENDING`; `STAGE_COMPLETE=FALSE`.
- Source tests and metadata do **not** prove actual aesthetic acceptance. Ask user to inspect live desktop/mobile at rest, hover and press for 20–40s, retaining strong enough whole-globe spin, original depth/color/detail, no ugly liquid overlay and no central aperture/dark well.
