# MEDEUS V3.9 — internally emissive white-lilac pearl sphere, no surface glare
Date: 2026-10-13
Classification: EXTEND V3.8's procedural white-lilac water sphere; SUPERSEDE only external surface specular presentation.
Status: SOURCE_QA=PASS, CI=PASS, LOVABLE_SYNC=PENDING_AT_RECORDING, USER_VISUAL_SIGNOFF=PENDING, STAGE_COMPLETE=FALSE.

## User's directive
- User: "блики с поверхности убрать. сделать как будто внутренний источник света изнутри сферы" (typed partly under an incorrect keyboard layout). Direct execution authorized: "сама".
- Keep pearl white/lilac, optical volume and soft breathing, no planetary rotation, visible hover and physical click effects but as inner-emission changes, not external surface glare.
- No still image generation or mutation of source master; source-only shader change.

## Implementation / provenance
Website repo `MrPenser/medeus-master-asset`:
- `src/lib/medeus/orb-field.ts` commit `395b95581746f881ea8d2b9e3e2fee6846ad1a18`. Replaced only default `pearlSphereColor` with volume-driven internal emissive optical material:
  - `geometryNormal` and `waterNormal` preserve curvature and localized water displacement.
  - `refracted` source-independent optical coordinates, `nearLayer`, `farLayer`, `thickness=2*z`, `scatter`, `grain` retain gently moving pearl subsurface volume.
  - Integrated source `emitterDepth=1.-exp(-thickness*1.05)`, broad slightly off-center `coreGlow` without aperture masks, `depthGlow`, low-density lilac body, `emissive` white/lilac photons. Diffusive transmission at curved limb replaces artificial surface highlight.
  - Default material has NO `reflect(...)`, NO `specA/specB`, NO `vec3 specular` nor directional external surface specular lamp. Historical classic/liquid rollback still retains its old code independently.
  - `localHover` and a single age-monotonic outward `outward` crest brighten `emissive`, not the reflected shell. Existing large-sphere hover/click surface response remains intact; microphone unaffected.
  - Slightly softened modern alpha limb `0.974 -> 0.966` to reduce visual glass shell without flattening volume.
- `src/lib/medeus/core-flow.test.ts` commit `3cc7f92477802dfb20b414d4c5e8302f03d4c71f`: optical depth numeric checks, no-reflected default pearl, hover/click, no rotation, mic and exact source PNG custody.
- `.github/workflows/medeus-liquid-orb-qa.yml` commit `1946c2ea5a39b737adf045784ed434cd769be862`, adds explicit no-surface-reflection, internal-emitter guards.
- Website HEAD `1946c2ea5a39b737adf045784ed434cd769be862`.
- GitHub Actions run `38380002533`: both GLSL ES100 shaders (big sphere and mic) PASS; Bun/Vite production build PASS; **40/40 tests PASS across 9 suites**.
- Lovable project `76dd8168-469d-4edb-88f6-f313be1c1de8`, preview https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/. Mirror HEAD must be confirmed separately from GitHub CI.

## Locked invariants
- Original master `src/assets/MEDEUS_MASTER_VISUAL_V3_NO_CAPTIONS.png` is unchanged SHA256 `9aac52baeac03d61a35ea9809d3580128952de1ae14d77f43c97a5fb7585c50d` (whole scene still uses it; default big sphere alone uses generated shader material).
- No new graphic rings, no visible orbit axes, no planet spin, no broad fast currents, no dark iris. All ten FSM states, existing UI, separate microphone, voice and text channels, touch/hover behavior remain. Radius breathing remains ±1.2% clamp.
- `?volume=off`, `?core=off`, `?surface=classic`, `?breath=off` remain rollback toggles.

## Acceptance boundary
- `SOURCE_QA=PASS`, `CI=PASS`; not proof of aesthetic success.
- `ACTUAL_MESH_3D=NOT_IMPLEMENTED`: still procedural volumetric-looking fragment shader on a sphere silhouette.
- `USER_VISUAL_SIGNOFF=PENDING`, `INTERNAL_LIGHT_VISUAL_APPROVAL=PENDING`, `MOBILE_REAL_GPU_QA=PENDING`, `STAGE_COMPLETE=FALSE`.
- Next: user desktop/mobile idle, hover, click 20–40s, check light feels internal rather than a shiny skin; no hole, white blown-out plateau, flat effect, high-speed currents, or stripes.
