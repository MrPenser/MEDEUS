# MEDEUS — Living Ocean Surface Trial V1
**Date:** 2026-10-12
**Status:** USER_AUTHORIZED_EXPERIMENT / REVERSIBLE_SOURCE_DEPLOYED / SHADER_AND_BUILD_QA_PASS / DEVICE_ACCEPTANCE_PENDING

## Exact user vision
«сферу жидкой», «как бы живым океаном под водами которого происходят процессы созданные нами как 10 состояний. но поверхность реагирует только как жидкость».
User explicitly rejected the humanoid/druid face ("пока откажемся от этой идеи") and requested launch ("запускай", typed on English keyboard "pfgecrfq").

## Product rules
1. Keep **one** spherical core, sourced solely from the **immutable SHA256-verified** approved master `MEDEUS_MASTER_VISUAL_V1_LOCKED.png` (SHA256 `52244e15720d0dd40faa04914a44f8051a6466c166973b2609ea5d58f0e1de88`).
2. Exactly **ten inherited inner states** remain untouched: DORMANT, AWARE, LISTENING, RECEIVING_TEXT, PROCESSING, EMITTING, MATERIALIZING, REVEALED, DEEPENING, ERROR_SILENCE. The liquid membrane is **not** an eleventh state and has no independent cognitive dynamics.
3. One translucent, continuous liquid surface is layered optically over the existing underwater light/UV animation: gentle moving waves at rest, refractive displacement of submerged state textures, silver-lilac specular and rim highlights.
4. **Real taps** (sphere or existing microphone trigger) cause expanding, fading surface waves at actual contact origin; **hover and state transitions do not trigger new splash events**.
5. Existing lilac photon/glyph emission, keyboard input, microphone recognition, mobile layout, greeting audio and response-channel rules are unchanged. No face/human figure enters production.
6. Respect `prefers-reduced-motion` through existing motion amplitude (0.35).
7. **Reversible at runtime without code rollback**:
   - Default liquid: `https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/`
   - Exact previous classic shader appearance: `https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/?surface=classic`
   - Feature flag stored only in ref from URL on initial scene mount, no extra UI buttons. If needed, code rollback is supported by Git history.

## Implementation / custody
- Live source repository: `MrPenser/medeus-master-asset` (**private**).
- `src/lib/medeus/orb-field.ts`: `oceanHeight`, `oceanPressure`, refractive UV offset, screen-space normals/sheen, WebGL1-safe non-destructive shader. Git commit `671791cdca49a1448e5c6bcf7c312b42bd68545a`; blob `f15510ee8bd2349e39e5429b4ba928d55c864a02`.
- `src/components/medeus/MedeusStage.tsx`: default `liquidSurface=true`, URL `?surface=classic` disables membrane, `lastSurfaceContact` marks real pointer touches and supplies `touchAge`. Git commit `18112821e9d0d53cd74b01b50f66cce0f737f393`; blob `d9a098e6816803c694da73daa41de692a375c4d1`.
- Automated compile/build/test workflow `.github/workflows/medeus-liquid-orb-qa.yml` commit `7c82a1e8b1dc2f0438a792a48f64d651cc6ee106`; GitHub Actions run `38291613068`. Initial QA run `38291613068` detected real shader error (`active` is GLSL reserved) and npm installer failure (`edgesOut`; installer/harness-specific). Corrected GLSL name in source commit `b6650a40b3898b52dd2d61aa7c7bad729aeffed2`, and switched workflow to the project's canonical `bun.lock` in commit `0a1675a1df7ec866116e4d3bf5c7c3d4908ca881`. **Verified QA run `38291850459` = SUCCESS**, both jobs: shader GLSL ES100 PASS, exact ten states PASS; Vite production build PASS; 2 test files PASS, 6 tests PASS. No regression of existing tests detected. This is source/build assurance, **not human visual or mobile-device QA**.
- Browser visual performance and user approval = **NOT YET OBSERVED**. This trial is not a final visual lock.

## Rejected alternatives
- No permanent humanoid face, no druid, no devil/angel face or conventional character rendering.
- No flat static wallpaper, no freely rotating hard-surface/solid sphere, no new UI panels or labels to signify fluid.
- No generative redraw of master bitmap, no replacing 10 state shader with one generic water animation.

## Acceptance
- User judges whether it behaves like a living ocean rather than glass/jelly/chrome.
- Desktop and portrait-mobile fluid animates smoothly with no blank WebGL orb.
- Touch creates visible concentric waves while submerged state effect remains recognizable.
- `?surface=classic` matches original appearance.
- All 10 states remain accessible through `?tour=1`; all visual proportions and mobile keyboard behavior unchanged.


## Operational first launch
- Lovable status `ready`, verified git source sync at shader correction `b6650a40b3898b52dd2d61aa7c7bad729aeffed2`. The workflow-only QA commit may synchronize after that without changing page behavior.
- Default version: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/
- Reversible classic compare: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/?surface=classic
- QA verdict: `SHADER_COMPILE=PASS`; `TEN_STATES_PRESERVED=PASS`; `BUILD_BUN_VITE=PASS`; `UNIT_TESTS=6_PASS`; `MOBILE_GPU_PERFORMANCE=NOT_TESTED`; `USER_VISUAL_APPROVAL=PENDING`.
