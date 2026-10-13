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


## 2026-10-13 — Living Ocean V1.3: intrinsic nonrepeating breathing
**User visual sign-off:** V1.2 accepted ("хорошо оставляем"); user then asked why sphere does not breathe by itself.

**Cause:** The liquid V1.2 shell only had moving underwater UV flow and surface normals plus click/hover deformation. Its **sphere silhouette/physical apparent volume remained at radius 1.0** at rest, so motion resembled a stationary vessel with moving liquid rather than a living inhaling/exhaling ocean.

**V1.3 implementation in private website repo `MrPenser/medeus-master-asset`:**
- Pure CPU animation function `src/lib/medeus/breathing.ts`, initial commit `0712505c27d35fbeae8dd4ae8bf3e29041eb6b1b`, corrected stronger phase decorrelation commit `1ddd4a002f90bf4ac9eca46fe5ac2e038b747a12`. Phase and strength vary by smoothed deterministic noise; default radius oscillations within about ±2.6%; reduced-motion amplitude 30%. Unlike a uniform sine oscillator, consecutive cycles differ naturally.
- `src/lib/medeus/orb-field.ts` commit `f841dd41ea2f3e5d41fa85884cdfd4b6b6838293` adds `uBreath` to liquid sphere **contour**, underwater-image UV scale and spherical-cap surface normals, to make the sphere itself expand/contract organically. Enlarges transparent WebGL canvas margin `ORB_BOX` from 1.04 to 1.09 to avoid clipping during inhale + hover tug; immutable bitmap and its geometry remain unchanged.
- `src/components/medeus/MedeusStage.tsx` commit `8c2d1d946c5c10e11517a011d0316e0da0ade675` passes the time-animated breathe parameter; **on by default**. Switch `?breath=off` returns the user-accepted **V1.2 liquid** behavior, while `?surface=classic` returns original classical clean sphere; no new visible controls.
- Unit tests `src/lib/medeus/breathing.test.ts` check real radius modulation, amplitude bounds, nonidentical consecutive cycles, reduced motion. First run detected too-similar cycles; amended phase variation rather than weakening test. New CI triggers on breath source and tests, regression checks for sphere contour + underwater scale, commit `8dafcf887478cca53f48b4a24df89dac59c2854c`.
- **Acceptance boundaries:** ten FSM states and their V1.2 organic rendering unchanged; one-way click ring and hover attraction unchanged; frozen source master not edited. Visual acceptance of V1.3 and real-mobile performance **PENDING** until direct inspection. This is a WebGL optical breathing effect, not a physically simulated ocean.

Links:
- V1.3 default: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/
- V1.2 liquid with breathing off: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/?breath=off
- Historical classic sphere: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/?surface=classic


## 2026-10-13 — Living Ocean V1.4: submerged micro-stars
**User approval / intent:** user approved living V1.3 breathing and explicitly requested sparse, chaotic, internally submerged micro-stars with individual lives, births, deaths and motion. User then authorized direct implementation ("делай сама", "даю разрешение").

**Implemented directly in private website repo** MrPenser/medeus-master-asset:
- src/lib/medeus/micro-stars.ts — commit e7daf916538fc09415493e46c0a422125a26944e. Exactly 14 asynchronous lifecycled light points, randomized x/y/depth/lifetime (11–31s), no regular orbit or grid, slow redirected random drift, continuous independent birth/brightening/extinguishing and rebirth at a different location. Sizes, temperatures and halo strengths differ. Not all are simultaneously visible.
- src/lib/medeus/orb-field.ts — commit 13796cbf704d4b7497fa58f17142c312afa32f5d. CPU paints a transparent 256×256 star lightmap, uploads at most once every 80ms (12.5fps), shader samples one star texture at *refracted underwater coordinate pBelow* before outer liquid Fresnel/sheen. This is an embedded star-depth layer, not a fixed HUD or UI overlay. No per-pixel nested star loop. Optional star-lightmap failure must not blank main sphere.
- src/components/medeus/MedeusStage.tsx — commit 482289de7a91d076bf68587a0d32e8ca75b1ff3e. Stars on by default only in liquid mode; ?stars=off restores approved breathing V1.3; ?surface=classic remains exact historical opt-out. The user-facing control layout is unchanged.
- src/lib/medeus/micro-stars.test.ts — commit 69ee4ebd5ba0b03ea835a6a4fb260c3ea85c31d3; five deterministic unit tests: sparse random population, asynchronous birth/death, slow drift and new positions, ten-state illumination only, reduced-motion support.
- CI workflow .github/workflows/medeus-liquid-orb-qa.yml updated at ee2d658a9f9d4c490467d6e171ef207abf5dd244 to gate lightmap internals, 0.08s upload throttle, state preservation, classic rollback and stars-off toggle.

**Immutable custody:** verified master asset SHA256 52244e15720d0dd40faa04914a44f8051a6466c166973b2609ea5d58f0e1de88 unchanged. All ten FSM states, V1.2 one-way click ring, hover attraction, V1.3 irregular breathing unchanged. A micro-star lifecycle is **not** an eleventh cognitive state.

**Verification:** source commit 482289de7a91d076bf68587a0d32e8ca75b1ff3e, GitHub Actions run 38349716794: shader GLSL ES100 PASS; Bun/Vite build PASS; all 15 tests PASS (4 suites). Enhanced QA run 38349765671 was initiated on workflow commit ee2d658..., pending separate final confirmation. Lovable project reported ready, synced to workflow commit ee2d658.... User visual acceptance and real-device GPU performance remain **PENDING**.

**Runtime trials:**
- V1.4 liquid + breath + submerged microstars: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/
- Approved V1.3 liquid + breathing, no stars: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/?stars=off
- V1.2 liquid with breathing/stars disabled: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/?stars=off&breath=off
- Historical classic: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/?surface=classic


## 2026-10-13 — V1.5: micro-stars visibility recovery
**User visual QA:** V1.4 received direct feedback: "пока ничего не видно" — no visible stars. This is a true product perceptual defect, distinct from the previously passing shader/build harness checks.

**Code diagnosis:** some star cores were only ~0.55px at 256px lightmap resolution; after alpha painting, alpha multiplication in the fragment shader, star-state gain 0.33 for idle, and complex existing galaxy pixels, emissions could be imperceptible. This explains likely faintness, but is not yet validated in the user's browser.

**Implementation directly in website repo MrPenser/medeus-master-asset:**
- src/lib/medeus/micro-stars.ts commit 39c565fe9851f71bcb98a8a4c04fb192fdf04c21. Exactly 14 sparse stars remain; random sizes increased to a clear minimum ~1.75px reference core with painted bright-dot radius >=1.19 lightmap px, larger translucent halo, brighter independent life and birth flashes, asynchronous start ages. Idle DORMANT illumination gain raised 0.33 -> 0.80; ERROR_SILENCE stays nearly dark. No uniform orbits, grids or identical cycles.
- src/lib/medeus/orb-field.ts commit 6caf412ba9e6613decc741a3a65b994c318b2222. Underwater additive emissive signal corrected: stellarEmission = micro.rgb * (micro.a * 2.6) * uStarGain * depthFade. Star coordinates still use pBelow from liquid refraction; stellar light is composited BEFORE the liquid sheen, and never overlays HUD. Stars-off and classic variants unaffected.
- CI visibility guards commit 4f5a1c2bfdb404c289fb678753eeea1c5c33990a.
- src/lib/medeus/micro-stars.test.ts commit 355de90d284cfa88feefe0413063e96f1f81e076: additional deterministic raster test verifies several painted stellar cores with visible >=1.19px radii and bright halo stops while keeping population small.
- GitHub Actions run 38350464654: GLSL ES100 shader gate PASS, Bun Vite production build PASS, full test suite PASS. Visual perception on user hardware and real-device GPU performance are PENDING — automated test success is not user visual acceptance.

**A/B:** V1.5 default with micro-stars: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/ ; approved V1.3 without stars: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/?stars=off

Immutable verified master bitmap, ten canonical FSM states, one-way touch ring, hover, autonomous breathing and voice/keyboard remain unchanged.
