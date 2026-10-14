# MEDEUS V5 — Live star: convective plasma and erupting corona

Date: 2026-10-14
Owner authority: "ничего не изменилось!!! ореол статичный! цвета тоже!... представить себе живую звезду ... создать анимацию внутренних и внешних процессов ... сама ... мало делаешь."
Decision: EXTEND exact V4 site art, SUPERSEDE insufficient V4.2 decorative light animation as the default. Preserve V4.2 via reversible `?star=off`.

## Implemented (not just proposed)
Working repo: `MrPenser/medeus-master-asset` main. Verified HEAD `413b9efb2b3c4c93c91ce172f155289744676547`.

- `src/lib/medeus/orb-field.ts` change `cc863927fc97d5cb85db79b3fdf99ee9767c6b6e`: `v5Convection` makes four-octave large-turbulent noise and fine-scale independent vectors, visibly advecting source V4 filaments. Flow fades to zero at the limb to preserve approved contour, does not rotate/reproject/replace V4 master, and is motion-budgeted.
- `v5StellarInterior` models two-layer slow/mid convection and fast granular cellular structures, with local white/violet/lilac source RGB masks and independent moving heat pockets. Modulation is spatial, asymmetric and source-aware; no full-disc synchronized whiteness. There is bounded local light/plasma tint, not a uniform static flat overlay. Not a physical hydrodynamic or astrophysical plasma solver.
- `v5StellarCorona` is a broad dynamic nonperiodic field using drifting billows, filaments and flicker and four independently appearing localized prominence regions anchored to different directions. Its optical extent changes continuously by local activity, compared to old fixed nearly invisible 0.087 radius haze. Default corona extends out to ~0.245 nominal extra orb radii with up to 0.8 compositing alpha, clipped safely by `ORB_BOX=1.30` and source geometry. No rigid drawn orbits, circular strokes or UV rotation.
- Genuine active V5 default: `bool livingStar=(approvedV4 && uStar>.5)`; V5 corona outside rim and source-preserving convection/material inside rim. Code retains prior V4.2 `v4HaloBursts` and `v4IndependentColors` ONLY as fallback with `?star=off`. Existing `?surface=classic`, `?volume=off`, `?core=off`, `?breath=off` remain.
- `src/components/medeus/MedeusStage.tsx` commit `4bdc18b52f7990a73fa04983916b9590bf29bf97`: V5 on by default, `stellarEnabled.current=params.get("star") !== "off"` and passed into the orb frame. No mic, text/voice, FSM/interaction changes.
- `src/lib/medeus/core-flow.test.ts` commits `7d64c15fced569559d3cdcdcb31d4245ce750673` / `c4511b081a992d7e0880c45e0877d3b8e036bd2c`: 4 new tests, including mathematically computed convective pixel displacements at T=0 and T=7 across three sample locations (significant drift), limb immobilization, prominence reach, GLSL source and classic fallback. The first numeric test failed because a sample location was inside the cutoff, corrected to outside cutoff. Production shader passed even during the intermediate test failure; latest tests pass.
- `.github/workflows/medeus-liquid-orb-qa.yml` commit `413b9efb2b3c4c93c91ce172f155289744676547`: source/invariants gates for V5 fluid motion and 3D-looking coronas; real GLSL ES100 compilation of orb + mic, site build.
- Run `38528498056` COMPLETED SUCCESS at exact HEAD. **67/67 tests passed in 10 suites**, both shader and site jobs pass. https://github.com/MrPenser/medeus-master-asset/actions/runs/38528498056 .
- Exact source visual PNG `src/assets/MEDEUS_MASTER_VISUAL_V4_APPROVED.png` untouched SHA256 `773f67be7fea7fb8b3dd63b88f58dd55d01e82b0724ed3098db317a8d4f8d5b6`. V3 is still retained backup. V4 microphone independent and lower, 10 FSM states preserved, no duplicated labels or new planets/art.

## Boundaries and acceptance
- SOURCE_QA=PASS, CI=PASS, SHADER_GLSL_ES100=PASS.
- Lovable project `76dd8168-469d-4edb-88f6-f313be1c1de8`, preview https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/ ; wait for exact HEAD mirror verification before marking LOVABLE_SYNC=PASS.
- USER_VISUAL_SIGNOFF=PENDING, REAL_DESKTOP_MOBILE_OBSERVATION=PENDING, STAGE_COMPLETE=FALSE. Source tests demonstrate materially stronger time-varying optical fields but do NOT prove actual perceptual quality/physical realism in user's browser. Need observe 20–40s at rest/hover/click/mobile, and compare `?star=off` fallback for intensity/performance.
- No public production publish authorized or performed.
