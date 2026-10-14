# MEDEUS V4.2 — isolated solar bursts on halo, independently lit source colors

Date: 2026-10-14
Disposition: EXTEND locked V4 scene and V4.1 animation; SUPERSEDE V4.1 broad additive light which user rejected.
Stage: SOURCE_QA=PASS / FINAL_LOVABLE_MIRROR=PENDING_AT_WRITING / USER_VISUAL_SIGNOFF=PENDING / STAGE_COMPLETE=FALSE.

## Authority and user rejection
User: "сейчас изменения общей ярокости белого цвета слишком сильные и всей сферы!!! нето! нужно как на солнце чтобы по ореолу происходили отдельные вспышки и при этом общий цвет в отдельности реагировал по своему. например фиолетовый сам по себе становился ярче а белый сам по себе. и.т.д.", followed by "сама".
Explicit decisions:
1. Sunlike light bursts take place **around the outside smoky limb**, spatially distinct and nonsynchronous, not across the full disc.
2. Interior whites, violets and lilacs alter *only the intensity of their original source pixels* at independent timings. The entire source image must never be globally whitened/repainted.
3. Keep actual approved V4 image, two independent mic/orb interactions, ten FSM states, subdued breath, no UV rotating sphere/iris/rings/striping, previous accepted smoky halo.

## Live source / implementation
Website repo `MrPenser/medeus-master-asset`:
- `src/lib/medeus/orb-field.ts` source fix commit `20e326e240fa150dc9c50d0194d848cbbb59450e`.
- Deleted former wide four-lobe additive `v4SolarFlares()` and removed `c=clamp(c+v4SolarFlares(...))` from inside V4 sphere.
- New `v4HaloBursts(p,T,motion)`: FOUR elliptically-local Gaussian light regions centered at distinct locations on the circumference (azimuths specified by independent XY positions, not orbit rotation), independent slow envelopes and lilac/rose colors. These illuminate the outward diffuse smoky halo **only inside** `if(approvedV4 && r>rim)`, through `burstEnergy`, localized alpha, and tinted mist. Never applied to the interior.
- New `v4IndependentColors(original,p,T,motion)`: source-RGB-defined `whiteMask`, `violetMask`, `lilacMask` based on original luminance/chroma/differences of red/green/blue. Each is multiplied by separate independent long-wave envelopes and drifting FBM local modulation. Max incremental gain coefficients 0.022, 0.048, 0.035 respectively; source RGB is multiplied (hue-preserving) not added, and clipped to [0..1]. No additive white overlay.
- Removed old whole-orb `c=authentic*(1.+.015*sheen*uMotion)` because it could still make entire sphere brighter/darker together. Current default `c=v4IndependentColors(authentic,p,uTime,uMotion);` after original `tex(sourceP)` sample, followed by separate existing hover/click localized illumination. `uMotion` respects reduced motion. Original external scene and mic unchanged.
- Verification of actual approved V4 PNG sample pixels (read-only): source orb's strongly white and low-chroma regions represent ~7% of visible sphere pixels, violet ~32%, lilac ~15% at meaningful mask strength. Ensures white modulation is sparse and non-global; no pixels were edited.
- Test commits `f452d5c5b1ad0fc0c7c161a2fbf7b6c59d6efd7d`, `90d02697f6ac76bcfa55a5bbe4892b351a213975`, and harness correction `46a1ac344a051773c466a7f4b942d9a644e73d1e`. Tests assert separate halo-only code path, color-specific masks and multiplicative original sampling, independent timing, reduced motion and legacy invariants. Initial test asserted exactly zero intensity of one flash at ALL arbitrary times; this was an overly strict test, not a demonstrated rendering bug. Final assertion accepts <0.02 for near-extinguished intervals.
- CI workflow `89023d96bf09061ed160214d1e9999223d3e64c4` enforces V4.2 architecture and original custody.
- Final website HEAD `46a1ac344a051773c466a7f4b942d9a644e73d1e`. GitHub Actions run `38524494645` completed success at exact HEAD: GLSL ES100 orb and mic shader compile PASS, Bun/Vite production build PASS, **63/63 unit tests PASS across 10 suites**.

## Immovable invariants
- Active master `src/assets/MEDEUS_MASTER_VISUAL_V4_APPROVED.png`, 1448x1086, SHA256 `773f67be7fea7fb8b3dd63b88f58dd55d01e82b0724ed3098db317a8d4f8d5b6`, unchanged; V3 backup `9aac52baeac03d61a35ea9809d3580128952de1ae14d77f43c97a5fb7585c50d`.
- Approved V4 background, no side text/orbits, lowered independent mic, 10 states, mobile layout, click one outward crest, breath, shader fallback flags remain.
- No public production publish requested; Lovable project's preview can be opened at https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/.

## Acceptance
- Source build/test checks are technical only; `V4_2_VISUAL_SIGNOFF=PENDING`, `MOBILE_REAL_GPU_QA=PENDING`, `STAGE_COMPLETE=FALSE`. Visually inspect around 30–40 s for local, uneven, soft flares on the existing smoke halo and independently brightening intrinsic violet/white/lilac filaments; ensure no synchronized whitening of disc, static center hole or overt spot/line/ring.
