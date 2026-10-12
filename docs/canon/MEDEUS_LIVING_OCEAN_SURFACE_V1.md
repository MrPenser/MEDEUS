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


## 2026-10-12 — Liquid v1.1: fluid stillness + cursor attraction
**Real user QA feedback on v1:** mouse-click response was good; idle water appeared like cheap rocking 2-D wallpaper; **hover without clicking did nothing**, although the membrane should be slightly drawn toward and lag behind the cursor.

**V1.1 user-requested correction now in website source:**
- `src/lib/medeus/orb-field.ts` commit `a8990df7fd54262856b5aa8f41eaff38e5825421`: replace axis-aligned rocking sines with *asymmetric, domain-advected circular gyres*; proper 3-D spherical-cap optical normal for specular/reflections, two soft drifting highlights, local hover-raised liquid height/UV lens and tiny silhouette tug toward the cursor. This is an optical shader approximation, not full Navier-Stokes physical simulation.
- `src/components/medeus/MedeusStage.tsx` commit `048b68ec734885f41ff2a49b1071e1dac81aac02`: record passive pointer motion within 1.12 orb radii, map to normalized orb coordinates, move membrane position toward target with exponential inertia **145ms**, release over **230ms**, no click required. Touchscreen pointer movements are excluded from hover to avoid native keyboard/touch interference. On pointer leave, strength decays smoothly; `prefers-reduced-motion` reduces hover amplitude.
- **Click impact preserved** with same expanding wave equation/envelope; original locked bitmap never rewritten. Classical `?surface=classic` ignores the added fluid/hover uniforms, leaving the original optical shader path.
- Strong code custody gate: the **entire original `sampleState(...)` function (all 10 inner states; 2,656 characters) was compared byte-for-byte against earlier commit `0a1675a1...` and is EXACTLY UNCHANGED**. Vertex shader is unchanged as well.
- CI: GitHub Actions `38293138422` `shader=success` (GLSL ES100), `site=success` (Bun Vite build, existing tests); complete checked source `048b68ec734885f41ff2a49b1071e1dac81aac02`. Lovable `get_project` source sync reports matching commit and `ready`.
- User-facing trial/compare links remain unchanged. `USER_VISUAL_QA_V1=REJECTED_IDLE_AND_HOVER`; `V1_1_SHADER_SOURCE_QA=PASS`; `V1_1_USER_BROWSER_VISUAL_QA=PENDING`; `FINAL_VISUAL_LOCK=NOT_GRANTED`.


## 2026-10-12 — Living Ocean V1.2: one-way ripple and organic interiors
**Direct user feedback, second in-browser trial:** on physical click outward wave initially looked good, but subsequently what looked like rings moved backward and concentrated toward the center when the inner visual state changed; non-click hover still too weak; an inner state manifested apparently identical triangles pulling inward. User explicitly requested removing identical shapes and repeated patterns while retaining the ten-state architecture. Explicit permission to implement directly.

**Root cause proven in source before modification:** the legacy `sampleState` shader contained (i) AWARE `sin(d*34.-t*11.)` radial oscillation, (ii) LISTENING `sin(r*25.+T*7.4)` inward wave, (iii) RECEIVING_TEXT `sin(a*9.+...)` ninefold angular spokes, and (iv) PROCESSING `off = ... p * c` center compression. Those state visuals could be mistaken for liquid reversing even when the outer click pulse was expanding.

**Solution, not merely parameter tuning:**
1. `src/lib/medeus/orb-field.ts` commit `de8723a9b2d168c73f5f22310ac73803ce0fcb9f`: retain **original** `sampleState` function untouched as strict `?surface=classic` rollback; add `sampleOrganicState` for **all ten** same underlying FSM states in liquid mode (advected FBM currents, independent density/shear/exposure, no radial/angular geometry, repetitive spokes, central contraction or inward wave). Liquid changes are visual; `states.ts` unchanged.
2. Liquid surface `oceanHeight`: substitute irregular smoothly advected value-noise flow for repetitive gyre sine bands. Surface touch becomes one **positive Gaussian crest** with `ringRadius=.78*uTouchAge`, monotonically outward in time, damped `exp(-uTouchAge*1.12)`, expires after 3.4s, and **no sinusoidal phase or inward return**. Surface stays separate from FSM transitions.
3. Hover magnetic effect heightened: pressure `.104` vs `.052`, refraction lens `.104` vs `.040`, contour rim tug `.033` vs `.019`, moving highlight `.14` vs `.075`, spatial radius broader. Does **not** trigger click/speech.
4. `src/components/medeus/MedeusStage.tsx` commit `14503fb6d577f9b4fc7dcc158ed006e7024afc58`: hover spring follow 95ms and release 180ms; independent `lastSurfacePoint` ensures a click ring remains anchored to the actual physical impact even across UI/FSM transitions, preserving existing mic/keyboard semantics.
5. Strengthened shader/CI guards in `.github/workflows/medeus-liquid-orb-qa.yml` commit `8fbec81e4bf4fcde927374971d615b12e0431d2f`: verify all ten organic branches present, no trig/angle geometry in the new shader segment, strictly expanding click radius/no periodic sinusoidal surface wave, stronger hover and preservation of legacy shader fallback. GitHub Actions v1.2 run `38295646821` is independent from previous build run; record final result after checking.

**Custody:** immutable master `MEDEUS_MASTER_VISUAL_V1_LOCKED.png` SHA256 `52244e15720d0dd40faa04914a44f8051a6466c166973b2609ea5d58f0e1de88`; untouched. Canonical **ten FSM states** still `DORMANT, AWARE, LISTENING, RECEIVING_TEXT, PROCESSING, EMITTING, MATERIALIZING, REVEALED, DEEPENING, ERROR_SILENCE`. No eleventh state; visual process is not a new agent.

**Preview** https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/ ; rollback https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/?surface=classic ; mobile visual-performance and user acceptance are **not automatically proven** by shader compilation/build tests.
