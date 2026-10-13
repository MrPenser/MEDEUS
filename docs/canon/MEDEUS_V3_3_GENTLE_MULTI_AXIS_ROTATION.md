# MEDEUS V3.3 — gentle whole-sphere multi-axis rotation
Date: 2026-10-13
Status: SOURCE_IMPLEMENTED / CI_VERIFIED; USER_VISUAL_APPROVAL=PENDING.

## Authority / recall&
- Supersedes only the unfinished V3.2 *movement model*, not V3 approved optical master, interaction shell or site product architecture.
- User latest command: "слишком сильный шейдер не нужен с высокими скоростями течений!. и еще хаотичное вращение вокруг своих осей всей сферы добавь"; explicit permission: "делай сама".
- Prior source: V3.2 handoff `docs/canon/MEDEUS_V3_2_TRANSFER_2026-10-13.md`, product site HEAD `8130f4aa59188f533fb8c4879fad3fcfe1bfb29b`.
- Disposition `EXTEND`: tune existing verified V3-sampling liquid shader; no asset remake, extra overlay, or new state.
- Website source authority: `MrPenser/medeus-master-asset`.
- Product/canon repository: `MrPenser/MEDEUS`.

## Implemented source (website)
- `src/lib/medeus/orb-field.ts` commit `55ee406e90043b071f354772aba4eb2cd0147042` (blob `a209da11bc53fac54270e14cc7384528e1353c6b`).
- `oceanAxisTurn`: GLSL ES100 Rodrigues axis-angle rotation; `oceanSphereRotation` projects the verified V3 sphere to a hemisphere and applies three distinct tilted rotations with independently changing rates. The **pixels** of the entire sphere rotate together; axes are mathematical only, never rendered as rings, lines or objects.
- Axes: `(.82,.25,.51)`, `(-.36,.86,.43)`, `(.21,-.54,.81)`, normalized; nominal angular rates `-0.0044`, `+0.0031`, `-0.0023` rad/s with small incommensurate smooth rate modulation. This is deterministic quasi-irregular rotation, not stochastic physical turbulence or a true volumetric backside renderer.
- Subdued V3 material currents: suspended detail displacement amplitude `0.013`, whole-current gain `0.72`, applied gain `0.68`, donor jitter gains `0.052/0.054`; donor evolution slowed to `0.011–0.017` time factors.
- Retain source-color-based center-hole correction: source white plateau blend `(.13 + .68*whitePlateau)*uMotion`, no radial center patch. Keep true approved-source donor sampling bounded by `oceanInteriorMaterial` within `0.88` of the sphere radius; no surrounding text/planets.
- `src/lib/medeus/core-flow.test.ts` commit `52a8398ebd58a3ed6d7953d1d8e54212cf369868` (blob `f4ea9881bfeafbc66783eedab6f63f9fc988468a`) tests the three axes, rate bounds, subdued transport, center correction, source hash, rollbacks and mic.
- `.github/workflows/medeus-liquid-orb-qa.yml` commit `df25d815f3c931a64ad061ecec50bf1e517aabdd` (blob `50472721262328d227151a9b14cdc9a1b5f51b1d`) tests GLSL ES100, preservation of FSM/mic/master and V3.3 rotation.
- Full V3.3 site CI HEAD: `df25d815f3c931a64ad061ecec50bf1e517aabdd`.
- GitHub Actions run **38370699038**, conclusion **success**, both shader and site jobs successful; 38/38 tests PASS (9 suites); Bun/Vite build PASS, vertex+fragment GLSL ES100 checks PASS.

## Immutable and approved behavior
- PNG `src/assets/MEDEUS_MASTER_VISUAL_V3_NO_CAPTIONS.png` SHA256 `9aac52baeac03d61a35ea9809d3580128952de1ae14d77f43c97a5fb7585c50d` unchanged.
- Preserved: liquid membrane breathing, hover inertia, one outward-only physical click wave, distinct independently responding mic with voice capture, all 10 original FSM states, keyboard/mobile/desktop and no classic-path changes.
- Rollbacks: `?volume=off` or `?core=off` disables V3.3 optical rotation/mixing; `?surface=classic` reverts liquid visual path.

## Strict verification boundary
- `SOURCE_QA=PASS` and `TESTS=38/38_PASS`. Product shader changes were committed; both jobs in Actions run 38370699038 passed.
- `USER_VISUAL_SIGNOFF=PENDING`, `NO_CENTRAL_HOLE_VISUAL_PASS=UNVERIFIED`, `MOBILE_REAL_GPU_PASS=PENDING`, `STAGE_COMPLETE=FALSE`.
- Need user 20–40s inspection in browser on desktop and mobile at rest, hover and physical click: visually gentle flowing whole sphere, irregular orientation, no heavy streams, visible axis tracks, border tearing, sampling artifacts or static iris.
- Lovable project `76dd8168-469d-4edb-88f6-f313be1c1de8`, preview `https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/`; verify live latest code mirror, never assume GitHub HEAD automatically equals Lovable HEAD.
- This is not production sign-off and does not activate ASTRADELIA integration or real forecasting.
