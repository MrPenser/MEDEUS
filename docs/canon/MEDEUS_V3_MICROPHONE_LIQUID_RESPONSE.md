# MEDEUS V3 — Microphone Living Ocean Response

Status: SOURCE_IMPLEMENTED / CI_PASS / LOVABLE_SOURCE_SYNC_VERIFIED / VISUAL_APPROVAL_PENDING
Date: 2026-10-13

## Authorized behavior
The user requested that the lower microphone planet react **like the central liquid sphere** BOTH on hover and on actual press.

- At hover, micro planet surface pulls toward the pointer with ~95 ms viscous spring lag, slowly releases over ~180 ms, refracts verified V3 optical pixels and briefly shows a subtle icy reflection. Passive hover never activates speech, state transitions, or touch waves.
- Pressing the microphone generates one localized **outward-only** decaying ripple on the microphone with center at the actual contact point; no repeating orbital rings, no returning waves, and no permanent decoration.
- Microphone pointer-down continues to start the existing voice-input pathway and all keyboard fallbacks. A microphone click **does not generate a fictitious ripple in the big central orb**; central orb contact remains separate.
- Default rest pixels on the overlay are sampled from the untouched V3 bitmap. No new foreground mic icon, no image redraw, no palette modification, no new decorative stars/orbits/fog.

## Implementation
Website repository: MrPenser/medeus-master-asset
- src/lib/medeus/mic-field.ts, commits `80b96f589f2d96d486f9284251359ce8a75de7ff`, `fa05d243c253b20f4f1ae8f6999fc13defcf3c3d`. Independent lightweight WebGL fragment shader samples `MEDEUS_MASTER_VISUAL_V3_NO_CAPTIONS.png`, localizes both optical interactions within original microphone disc, has exact V3 colors when idle and single Gaussian propagating crest `ringRadius=.95*age`. Source URL/hash unchanged.
- src/lib/medeus/mic-motion.ts commit `4e26bf22e458e592ca2432b9d3f32e1f192debe2`. Pure mic-local coordinate normalization and viscous hover integration, 95 ms attraction/180 ms release, monotonic ripple radius.
- src/components/medeus/MedeusStage.tsx commit `aceec6a5cb2a0bcd1cfdebeaae338cb4be8317e2`. New independent `micCv` canvas, source-coordinate and responsive mobile/desktop placement using `PRESENTATION.micX/micY/micHitRadius`, separate hover/contact refs, physical mic press integration and independent click target. All old speech callbacks retained. Image-derived master remains immutable.
- src/lib/medeus/mic-motion.test.ts commit `adb18f7fd468301f1b2cf24aa2dd72e4f22be60c`. Five tests for hover lag, decay, local hit position, monotonic outward wave, paused background-tab timestep clamping.
- .github/workflows/medeus-liquid-orb-qa.yml commits `7b918e608e2bb04040bb1639d31db2fc941c0931` and CI parser correction `93e420a24c609fa92e77ad02071a2ef96acde5e2`. Validates WebGL ES100 for both separate shaders, all ten canonical FSM states and no old crystal/stars, unchanged V3 master SHA and approved response invariants.
- CI run **38364507391** PASS in both jobs: Vite production build PASS, **34/34 tests PASS across 8 suites**, GLSL ES100 orb and mic PASS.
- Lovable project `76dd8168-469d-4edb-88f6-f313be1c1de8` returned Ready and read-file probes verified mic-field, mic-motion, and MedeusStage integration. User live visual acceptance pending.

## Non-negotiable V3 baseline
- MASTER_ASSET.version remains V3 with SHA256 `9aac52baeac03d61a35ea9809d3580128952de1ae14d77f43c97a5fb7585c50d`.
- Old V2 and V1 files untouched as backups.
- Approved cosmic panorama/planets, no orbit lines, 10 original FSM states, original liquid sphere breathing, hover and one-way touch ripple, speech/text channels preserved.
- Source QA does not prove perceptual acceptance. Ask for targeted mic hover/press browser feedback if needed.

Preview: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/
