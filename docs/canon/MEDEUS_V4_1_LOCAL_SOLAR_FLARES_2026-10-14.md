# MEDEUS V4.1 — asynchronous soft localized chromatic flares
Date: 2026-10-14
Disposition: EXTEND approved V4 source rendering, not replacement of master artwork.
User request: "фиксируем. теперь добавь эффект изменения цвета на всей сфере ное не сразу везде а типа вспышек мягких на солнце" followed by explicit "сама".

## Design authority and constraints
- Approved V4 composition, 1448 x 1086 PNG at `src/assets/MEDEUS_MASTER_VISUAL_V4_APPROVED.png`, SHA256 `773f67be7fea7fb8b3dd63b88f58dd55d01e82b0724ed3098db317a8d4f8d5b6`, remains **byte-identical**. No image generation or asset recreation.
- Four *independent* broad soft light patches drift slowly in separate areas of the sphere, modulate asynchronously, and fade with nonzero dark intervals. Lilac/pink-violet/ice-lilac tint at deliberately low strength; no synchronized whole-sphere repaint, spinning/UV re-projection, stripes, orbit lines, center aperture, particles or external specular.
- The effect remains in the **approvedV4** shader branch only. Outside nebula, header/side planets, lower microphone (including distinct mic hover/click and voice capture), ten FSM states, reduced-motion preference, classic and legacy fallbacks are not altered.
- Keep original breathing, native source texture `vec3 authentic=tex(sourceP).rgb`, user interaction and outer smoky translucent rim unchanged.

## Source implementation and evidence
Website `MrPenser/medeus-master-asset` on `main`:
- `src/lib/medeus/orb-field.ts` introduced `vec3 v4SolarFlares(vec2 p, float T, float motion)`; four elliptical smooth exponential spatial lobes (`fieldA/B/C/D`) with distinct slowly wandering positions, four differently rate- and phase-modulated non-negative temporal envelopes (`phaseA/B/C/D`), and subtle additive color (`return tint*(.17*motion)`). Composite `c=clamp(c+v4SolarFlares(p,uTime,uMotion),vec3(0.),vec3(1.));` applied only to authentic V4 source sampling, before existing independent hover and one-way click feedback. No new shader uniforms, external textures or global blend.
- Source code commit `fe1cf789cd8a629d126a45ac10516a808a9d1f21` followed by function-position isolation fix `1e2d4620fdd5d5b005d9e848db62d6a27630311c`. The latter addresses a **harness substring-boundary** failure: legacy material QA previously included the new solar function, erroneously rejecting its `sin` time envelopes; shader behavior itself was not shown defective.
- `src/lib/medeus/core-flow.test.ts` adds two tests for spatial flare separation, independent time envelopes, V4 source retention, 10 FSM, no rotation and reduced-motion factor, most recent test commit `bad86f4ec4d257ac1dacee28c10ed62c34838557`.
- `.github/workflows/medeus-liquid-orb-qa.yml` similarly enforces helper/lobe placement, timbre/palette and fallback preservation; last workflow commit `99c4d21675f9eb60a76b89f4e967795dfe2b5442`.
- Verified website HEAD `99c4d21675f9eb60a76b89f4e967795dfe2b5442`. GitHub Actions run `38523096670`: completed **SUCCESS** with orb/mic GLSL ES100 compilation PASS, site Bun/Vite production build PASS, **62/62 tests PASS across 10 suites**.
- Lovable preview project `76dd8168-469d-4edb-88f6-f313be1c1de8`, latest checked `ready`, `agentFinished=true`, commit SHA identical to GitHub HEAD. Preview: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/ .
- Production public publish not performed (`is_published=false`).

## Acceptance
- `SOURCE_QA=PASS`, `CI=PASS`, `LOVABLE_SYNC=PASS`.
- `USER_VISUAL_ACCEPTANCE=PENDING`, `REAL_DESKTOP_MOBILE_GPU_QA=PENDING`, `STAGE_COMPLETE=FALSE` for this new animation addition. Visual observation must confirm perceptible but restrained local color flares across ~20–40s rather than whole-disc flashing.
- Prior V4 scene is user-locked as baseline; if V4.1 looks too strong, attenuate `.17` **only** after owner feedback and retest, don't repaint the source or change unrelated interaction mechanics.
