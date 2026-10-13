# MEDEUS V3.9.6 — Dark lilac sphere with bright interior emitter

Date: 2026-10-13
Prior user instruction: "Темный! Со светом изнутри"; explicit implementation authorization "Сам" after a text patch had been described.
Decision: EXTEND V3.9.5 optically volumetric pearl sphere. Supersede the light all-lilac palette; preserve V3.9.3 mobile text and cosmos repair, mobile microphone relocation, the 10 FSM states, existing touch/hover and soft breathing, no rotation.
Asset custody: V3 source PNG remains immutable, SHA256 9aac52baeac03d61a35ea9809d3580128952de1ae14d77f43c97a5fb7585c50d.

## Production source
Private repo MrPenser/medeus-master-asset branch main:
- src/lib/medeus/orb-field.ts commit 57a4b11c7ee55095043a8db6e2067bb3fdb5c016:
  - dark body palettes lightLilac=(.46,.28,.78), lilac=(.34,.16,.62), deepLilac=(.14,.05,.28), low density (.30+.14*z+.05*scatter), muted limb transmission.
  - inner source made substantially brighter: coreLilac=(.88,.70,1.); coreGlow thickness-integrated with 1.15 attenuation coefficient, Gaussian spatial attenuation 1.75; emissive coefficients (.34*coreGlow + .16*depthGlow) and secondary internal lilac pulses. Additional floor (0.08,0.02,0.18); final upper cap (.96,.90,1).
  - no reflected surface specular, opaque white center, image generation, axial rotation or added rings; relative original hover and click behavior remains unchanged.
- src/lib/medeus/core-flow.test.ts commit 63583882a8ee29368c18d61bc3c028318a8825ec: color, volume, one-way click and mic preservation source invariants.
- .github/workflows/medeus-liquid-orb-qa.yml commit de68f2f44e2487e6196a6f76bb6b7f47aac7c5b8: matching assertion updates.
- Final website HEAD de68f2f44e2487e6196a6f76bb6b7f47aac7c5b8.

## Verified evidence
- GitHub Actions run 38428240191 completed success at exact website HEAD; orb+mic GLSL ES100 compiled, Bun/Vite site build passed, 59/59 tests passed across 10 suites.
- Lovable project ID 76dd8168-469d-4edb-88f6-f313be1c1de8 independently matched same HEAD and ready status.
- Preview https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/

## Acceptance gate
SOURCE_QA=PASS; CI=PASS; LOVABLE_SYNC=PASS.
USER_DARK_INNER_LIGHT_VISUAL_SIGNOFF=PENDING; ACTUAL_MOBILE_GPU_QA=PENDING; STAGE_COMPLETE=FALSE.
Static tests prove code/compilation, not perceived 3D depth or final aesthetic satisfaction. Continue from this source HEAD; do not accidentally restore earlier pale palette.
