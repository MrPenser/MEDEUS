# MEDEUS V5.1 — all-around active coronal prominences

Date: 2026-10-14
User directive: "уже лучше. более активные процессы на поверхности короны. и протуберанцы в разных ее частях а не только сверху - ДОБАВИТЬ." Followed by explicit approval: "разрешаю".
Decision: EXTEND already implemented V5 stellar shader, preserve locked V4 source and prior activity, update CORONA ONLY. No reason to raise global/inner white brightness or regenerate an image.

## Implementation authority
Active website repo `MrPenser/medeus-master-asset`, main HEAD `357a9aaa27d4e23292234ce298926f1510a8d18f`.
- Shader `src/lib/medeus/orb-field.ts` commit `27e3cb2d43e80fc3ffc8d2ee3c3cf7cb85de2e3c`: replaces only `v5StellarCorona` with a visibly boiling multi-scale turbulent corona: billowA/billowB, finer moving filA/filB, flicker. Prominences have EIGHT independent time envelopes and angularly concentrated anchor directions: west/east/north/south + NW/NE/SW/SE. No rotating whole-sphere UV and no drawn orbit lines. Variable local plume reach `min(.335, .11+.10*boiling+.065*prominence+.030*threadHeat)`, density, taper and emission; frame cadence independent of hover or clicks.
- Corona clip boundary increased from .245 to .35 of the orb's radius; `ORB_BOX` expanded 1.30 -> 1.43 to avoid clipping with max 1.2% breath and 5% hover limb expansion. It remains a diffuse opacity/spectral field outside the natural orb; no hard concentric ring.
- Intentionally did NOT brighten the star's entire interior. `v5StellarInterior` remains source-color-aware and protected against global whiteout. Source V4 PNG unchanged SHA256 `773f67be7fea7fb8b3dd63b88f58dd55d01e82b0724ed3098db317a8d4f8d5b6`.
- No modifications to independent mic, input channels, 10 FSM, lower mic scene, backgrounds, typography, V3 backup or rollback `?star=off`. `?star=off` continues to render V4.2 coronal behavior in the same expanded but transparent quad; classic/volume/breath rollback unaffected.
- Tests `src/lib/medeus/core-flow.test.ts` commit `8ab8c6a62d46289f7477e51a079dffa7a2cb420b`: exact 8-sector shader gates, numeric changing corona reach and budget, time-sampled asynchronous directional eruption envelopes, sample moments confirming visibility of east/south/west/north at different times, top and bottom, preserved V4 controls. No claim of full fluid simulation.
- Workflow `.github/workflows/medeus-liquid-orb-qa.yml` commit `357a9aaa27d4e23292234ce298926f1510a8d18f` extends GLSL ES100 shader/static custody checks to eight sectors, corona reach and 1.43 quad. CI run `38529906932`: COMPLETED SUCCESS on exact HEAD, GLSL orb and mic shader validation PASS, Vite/Bun production site build PASS, **68/68 tests PASS over 10 suites**. https://github.com/MrPenser/medeus-master-asset/actions/runs/38529906932

## Scope and acceptance
- Proven: `SOURCE_QA=PASS`, `CI=PASS`, `GLSL_ES100=PASS`, `UNIT_TESTS=68_68_PASS`.
- Lovable project ID `76dd8168-469d-4edb-88f6-f313be1c1de8`, preview `https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/`. Synchronization must be verified independently at exact website HEAD before claiming.
- `USER_VISUAL_SIGNOFF=PENDING`, `REAL_DESKTOP_MOBILE_GPU_QA=PENDING`, `STAGE_COMPLETE=FALSE`; need actual 20–40s user visual check verifying distributed prominences, not merely code/test passes.
- Not physically accurate stellar hydrodynamics; this is aesthetic procedural WebGL plasma motion inspired by stellar corona.
- No public production publishing requested or performed.
