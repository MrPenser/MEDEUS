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


## 2026-10-13 — V1.6: user rejects star freckles, approved liquid restored

**User visual feedback on V1.5:** "нет!!! это как оспа на теле океана" — visible dots were perceived as surface skin blemishes rather than distant stellar births. This is an explicit **REJECTED_VISUAL**, overriding earlier automated shader/test PASS. Increasing brightness/size was the wrong corrective action. Do not quietly restore that design.

**Immediate protective rollback**: website repo MrPenser/medeus-master-asset, src/components/medeus/MedeusStage.tsx commit 5f8130572602cecc3fefc304a31931b0967f62e6, changes default from stars-on to **stars OFF**. Experimental effect must be expressly requested as ?stars=deep. Default preview is again the previously accepted V1.3 **living, breathing, pointer-responsive, outward-ripple ocean with NO starspots**. No base shader, ten-state FSM or immutable verified master alteration was required for the rollback. Lovable ready and source-sync confirmed at rollback SHA 5f813057....

**Separate visual research, V1.6 deep-only opt-in**:
- src/lib/medeus/micro-stars.ts commit 6b9ffac672635c784781c9294d61e225a17010a3: only **10** stars (down from 14), now restricted to inner radial <=0.59 in orb units, small <=1px reference pinprick centres, very weak 3–5px halo, dimmer cool/lilac emission, randomized depth/lifetime/slow drift, asynchronous birth-death and respawn. Do NOT render large sharp/ringed glowing spots.
- src/lib/medeus/orb-field.ts commit d4caa35f3f8202dba61c3bdafdc78314d5c7827a: remove 2.6× pox-emission mode, implement much softer 1.45× under-water luminescence multiplied by inner-ocean envelope, explicit outer-shell exclusion and background cloud occlusion. Still uses refracted underwater pBelow coordinates before fluid sheen.
- src/lib/medeus/micro-stars.test.ts commit cf34cf7eb4b18b1a76174b03b0ab69e1c151479c: raster regression test asserts sparse <=10 population, sub-1px source cores, max 4.9px halos, positional restriction to deep core.
- .github/workflows/medeus-liquid-orb-qa.yml commit 1def24ff3bd9b0487a6a4cfe1b6d45a13c092dc1: default star-off hard gate, ?stars=deep opt-in, deep occlusion and no cosmetic freckles. Source CI run **38351217510**: WebGL1 GLSL compile PASS, Bun/Vite build PASS, 16/16 unit tests PASS in 4 files. Several intermediate runs failed due to stale old CI assertions; final source/run passed. Do not label those harness transitional failures as product regressions.

**Preview split (non-destructive):**
- DEFAULT / accepted **starless ocean**: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/
- OPTIONAL / unapproved deep micro-star experiment: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/?stars=deep
- Classic full rollback: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/?surface=classic

**Hard constraints:**
- V1.5 pox rejected; DO NOT enable without new user visual approval.
- V1.6 experiments default OFF; USER_VISUAL_SIGNOFF=NOT_GRANTED, REAL_BROWSER_PERCEPTION=UNVERIFIED.
- Preserve V1.3 liquid breathing, V1.2 one-way touch ripple and viscosity hover, and all ten original states; no new surface ornaments or geometrical repetitions; master SHA stays locked.


## 2026-10-13 — Living Ocean V1.7: rare crystal-clear interior flashes
**Authorized user request:** after visually rejecting V1.5 star freckles/pox and V1.6 invisible distant stars, user chose instead *редкие кристально чистые всполохи без тумана и мутностей* and explicitly ordered autonomous implementation (*исполняй сама*).

**Architectural decision:** close the star-particle rendering path entirely: no circles, sprite alpha textures, 256px star lightmap, texture uploads, permanent specks, ambient fog or haze. Preserve the confirmed visually approved living ocean baseline (breathing, cursor traction, physical one-way ring) as the default; experimental crystalline event is opt-in only via ?light=crystal pending user visual signoff.

**Production changes, GitHub site repo MrPenser/medeus-master-asset:**
- src/lib/medeus/crystal-flashes.ts commit aa302d4c36ccbbe3dfeede5cce798e5f775de7a8: event-driven **at most one active crystalline flash**, irregular first glimpse at +1.8…3.4s, further independent arrivals every 5.5…11.5s after completion, event duration 0.48…0.94s, randomized position (radius <=0.43), angle, half-length (0.033…0.070 radii), width (0.0032…0.0052 radii), depth, intensity. Smooth brief birth/death envelope; no repeating particles/orbits/geometry. Optional reduced-motion dims to 37%. No new state; 10-state current visual intensities act only as modulation.
- src/lib/medeus/orb-field.ts commit f343872bbf081ed3c012404dc6b76cff9f3ed204: remove runtime imports, shaders, GPU textures/uploads and additive star specks entirely. Render single **crisp, tapered luminous sliver** analytically in GLSL ES100 with uCrystal/uCrystalShape, calculated from **pBelow** (same underwater refraction as existing ocean), depth shell exclusion beyond ~0.45 to .65 radius, no translucent circular halo, mist, noise field or glow sprite. Apply beneath original approved outer water Fresnel/sheen. No additional GPU texture cost.
- src/components/medeus/MedeusStage.tsx commit 5098877980aaa57d0ec765a7b36d9d5241059ac3: remove stars=deep UI/preview activation; enable **crystal flashes only with ?light=crystal**. Default root remains accepted living V1.3 with no extra light objects; classic restoration still ?surface=classic.
- src/lib/medeus/crystal-flashes.test.ts commit c27cef933bd2d4d99880d87866b175e340e4d127: five deterministic tests verifying startup visibility, rare placement/temporal independence, no permanent spots, motion reduction and state-level modulation only.
- Regression workflow .github/workflows/medeus-liquid-orb-qa.yml commit a1abc08480dc6f4a45c3bcc772586333fd79eebf: explicit static assertions prohibit uStarTex/MicroStarField/star-lightmap path returning, protect submerged pBelow coordinates, interior-only envelope and opt-in starless default. GitHub Actions **38354547301** shader GLSL ES100 PASS, Bun/Vite production build PASS, all **21/21 tests PASS** (5 files).
- Lovable project 76dd8168-469d-4edb-88f6-f313be1c1de8 reported ready and matching latest site commit a1abc08480dc6f4a45c3bcc772586333fd79eebf. Read-file probes confirmed live stage uses light=crystal opt-in, orb-field lacks star texture and imports the new event system, dedicated event module is synchronized.

**Visual QA boundary:** user has NOT yet approved V1.7. No browser-level perceptual test claimed. V1.7 is a controlled experiment; base accepted ocean remains official. Master image (immutable SHA256 52244e15720d0dd40faa04914a44f8051a6466c166973b2609ea5d58f0e1de88), ten-state FSM and original classic renderer remain unmodified.

**URLs:**
- Crystal experiment: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/?light=crystal
- Approved base without light events: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/
- Original classical sphere: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/?surface=classic


## 2026-10-13 — V1.8: NO ORBITS, NO CRYSTAL LINES

**Visual user verdict:** user explicitly REJECTED experimental thin crystal flashes ("ерунда какието просто ооочень редкие черточки") and commanded "убери в конце концов все орбитыыы!!!". Previous V1.7 is NOT accepted. No further star/crystal decorative attempts should be deployed without user approval. Approved baseline remains breathing water, pointer magnetic drag, click's outward-only ring, ten original states.

**Root cause of persistent orbits:** six orbit ellipses plus horizontal scaffold/guide beads are baked into the immutable verified original panorama. The prior `src/lib/medeus/orbit-cleanup.ts` cleanup used limited ring-width coverage and a luminance prominence condition; dull arc segments and crossings (sampling other parts of the same guide) survived. Merely removing WebGL orbit code does not remove these raster lines.

**Actual source fixes in private website repo `MrPenser/medeus-master-asset`:**
- `src/lib/medeus/orbit-cleanup.ts` commit `8676896b62f5170ccfe42249258ba121c75cf9cf`: replace brightness-gated orbital suppression with a geometry-complete mask for 6 source-defined ellipse guides, continuous horizontal beam and 4 decorative nodes, rebuilding affected pixels from nearby **unmasked original cosmic donor pixels** along each line normal. Protected approved orb interior and immutable original pixels never touched. One in-memory derivative on load, shared across desktop and mobile.
- Follow-up real product bug found by new unit tests: at intersections the normal could sample still-on-beam pixels; commit `6bc3c8b16b74f939c98e8be8ed3ac15d61c9928f` prioritizes perpendicular donor sampling for horizontal-beam crossings.
- Orb rim node x944,415 fell inside former protected radius and remained; commit `b6b45855403d3a43b716c981a4eb8d3204444a5d` supports removing rim ornament within the WebGL-transparent edge while protecting true inner orb.
- `src/lib/medeus/orb-field.ts` commit `8741bf9c87868d2ee3b288c6bc7f4914776c949b`: remove rejected crystalline GLSL lines/related uniforms and renderer invocation; no star textures or particle logic. Ten organic state shader and approved breathing/hover/contact optical equations unchanged.
- `src/components/medeus/MedeusStage.tsx` commit `99939e9a8b3a24e122d72ce79580294671e8a8c7`: eliminate `?light=crystal` runtime activation and debug state. Current default and former experiments now show the accepted clean liquid visual.
- New `src/lib/medeus/orbit-cleanup.test.ts` commit `48c1acd28f30e24d46afcac892ce0f9f868c1d80`: three tests, including synthetic full-size master frame with bright/dim ellipse tracings, beam/nodes, orb pixel-preservation and reject malformed data. A real product defect was detected and corrected; the tests remained strict, not weakened to hide defects.
- `.github/workflows/medeus-liquid-orb-qa.yml` commit `eb1e58e477c836fb61e3070f4d8ca066b2aaed23` asserts no star/crystal renderer, checks in-memory orbit cleanup used by the presentation and desktop/mobile painting paths, preserves all ten state guards, outward-only wave and breathing. Earlier workflow red was caused by a brittle regex assertion and real orbit crossing bugs; final passed.
- **Final GitHub Actions run `38355671430` for website source commit `b6b45855403d3a43b716c981a4eb8d3204444a5d`: shader GLSL ES100 PASS, Bun Vite production build PASS, **24/24 tests PASS (6 suites)**, including 3 new orbit tests. Lovable project `76dd8168-469d-4edb-88f6-f313be1c1de8` confirmed `ready` and exact commit synced.

**Invariant and acceptance:** original master `MEDEUS_MASTER_VISUAL_V1_LOCKED.png`, SHA256 `52244e15720d0dd40faa04914a44f8051a6466c166973b2609ea5d58f0e1de88`, remains byte-identical. Cleans an ephemeral presentation copy, not asset. Ten canonical states and existing mobile layout preserved. Real user browser **NO_ORBITS_VISUAL_ACCEPTANCE=PENDING**, device screenshot QA not independently performed; source tests prove modeled geometry only, not all possible unmodeled raster marks.

**Preview:** https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/ . Bypass stale cached page with Ctrl+F5. Classic `?surface=classic` still allows comparing original sphere optical surface **but now also receives orbital-cleaned background**, i.e. classic is not an orbital rollback.


## 2026-10-13 — MEDEUS V3: exact approved image, no microphone captions
**Request and consent:** User visually approved a newly generated MEDEUS cosmic-vortex image after asking to remove the inscriptions above the microphone, then explicitly ordered "внедряй". The newly generated file from the current conversation is the *direct source* of V3, not a recreated artwork or an approximate text overlay.

**Immutable image identity:**
- Source: user-approved generated `космический_вихрь_medeus.png` (2026-10-13).
- Final GitHub site asset: `MrPenser/medeus-master-asset/src/assets/MEDEUS_MASTER_VISUAL_V3_NO_CAPTIONS.png`.
- Real original byte SHA256 = `9aac52baeac03d61a35ea9809d3580128952de1ae14d77f43c97a5fb7585c50d`, 2,218,455 bytes, PNG RGB 1672x941.
- Git blob SHA = `40620e1238b7c6ab2098c8f3c9d6c12e0d4899c6`; adding binary asset via Git-tree commit `f610cff5322b4c6e2445243e493f733e751aaa27`.
- `src/lib/medeus/asset.ts` commit `130f474b9e27d976db440ada7b9afeba5fe40d95`: renders V3 by default, runtime SHA256 verification switched to exact V3 hash, V1 and V2 retained as backups (V2 SHA256 `0dd41f6c5f1381136920480e23a3c9389604834a331e6b8bcfd4e22480f5b2ba`).
- `src/lib/medeus/presentation.ts` commit `93109509eb377b6bde6be75df209f05304914cba`: identity presentation, no old captions or masks, orb center 836,403 and radius 224; baked microphone center 836,810; full aspect 1672x941 maintained for desktop/mobile and WebGL.
- `src/lib/medeus/master-v2.test.ts` commit `79e3676ad9c73f83561a5c744514a85903697b31`: verified V3 full binary SHA256 + IHDR dimensions, V2 backup unchanged, original 10-state FSM, all UI target bounds.
- `.github/workflows/medeus-liquid-orb-qa.yml` commit `1120511e783818fb2731874d6a4740ed74a0d144`: asserts exact V3 PNG bytes, V2 backup bytes, WebGL shader, ten FSM state guards and site build.

**Verification:** GitHub Actions run `38362174590`: shader/GLSL ES 1.00 PASS; Bun/Vite production build PASS; **29/29 unit tests PASS** across 7 test suites, includes SHA256 of installed PNG and preserved backup. Lovable source check: asset.ts imports V3 and correct SHA, project status ready, Lovable project file inventory confirms V3 PNG binary exists alongside V2. Direct preview: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/ .

**Product gate:** SITE_SOURCE_QA=PASS; APP_PREVIEW_AVAILABLE=TRUE; USER_BROWSER_VISUAL_SIGNOFF_ON_DEPLOYED_V3=PENDING. Do not alter ten canonical FSM states, liquid-water interaction, independent breathing and user-controlled microphone, and never revert to rejected orbits/crystal dashes.
