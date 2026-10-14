# MEDEUS V5.5 — Shorter solar prominences and non-luminous physical hover

Date: 2026-10-14
User directive: "слишком высокие всролохи. и сделай отклик не световой", explicitly authorized "разрешаю".
Decision: EXTEND the live V5.4 corona and cursor mechanics only. Keep the V4 source image authority and all other approved features.

## What changed (implemented, not a proposal)
Website `MrPenser/medeus-master-asset`, branch `main`.
- Shader commit `b56616aeb42f33f5e90f3f2e08f490d663537c70`, `src/lib/medeus/orb-field.ts`:
  - `v54CoronalFan` lifetime-dependent radial reach `.08+.31*surge` → `.06+.18*surge` (max jet height ~24% rather than 39% of sphere radius). Faster fading `smoothstep(.58,.86,rise)` vs `(.73,1.02)`. Fork spread `.045+.085*rise` and sheet width `.060+.018*rise`, with proportionally reduced twist/turbulent displacement. Keep eight independently erupting directions and torn, branched shape (no worm tubes).
  - Max coronal region `rim+.43` → `rim+.28`; quad `ORB_BOX=1.55` → `ORB_BOX=1.42`. Required margin: 1+.012 breath + .095 local deformation + .28 corona = 1.387 < 1.42.
  - Living star's hover no longer **adds light** to the corona (`hoverCorona` alpha/RGB boost eliminated). Neither hover nor click generates additional emissive color on the V5 living-star source: former `c+=vec3(.36,.18,.56)*...` removed, V4.2 historical color response guarded `if(!livingStar)` for exact A/B rollback.
  - Instead, mechanical hover increases the deforming height field (.235 → .285), broadens field decay (5.0 → 4.2), increases local contour bulge (.075 → .095), lens texture displacement (.064 → .092), and broadens lens footprint in V5 only. The existing **single outward-only** physical click wave remains, independent microphone hover/press/voice remains.
- Tests commit `1af82ac3d2b405d56a75a9a5552541f3fcdb3053`, inherited old-expectation correction `1b5c8f0f56c819bb49199352dab29f1b7cbdec15`; dedicated tests for physically present hover, absent light, clipped shorter corona and maintained eight sectors. CI workflow `5e11c5286c6a9d20b34f7cc0bdc1c55dac0101d3` checks reduced fan geometry, nonluminous V5 and prior invariants.
- Site final verified HEAD `1b5c8f0f56c819bb49199352dab29f1b7cbdec15`.
- GitHub Actions `38622238804` at exact HEAD: completed SUCCESS; real GLSL ES100 orb/mic compilation PASS, Bun/Vite production build PASS, **72/72 tests passed across 10 suites**. Earlier intermediate runs failed due to old test assertions expecting intentionally removed light/old hover coefficients; corrected, not hidden.
- Lovable project ID `76dd8168-469d-4edb-88f6-f313be1c1de8`: status ready/agentFinished; `latest_commit_sha` matched final HEAD on 2026-10-14; preview https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/ . No public production publish (`is_published=false`).
- Original V4 scene `MEDEUS_MASTER_VISUAL_V4_APPROVED.png` SHA256 `773f67be7fea7fb8b3dd63b88f58dd55d01e82b0724ed3098db317a8d4f8d5b6` retained unchanged, V3 historic backup, 10 FSM and `?star=off` V4.2 fallback protected.

## Acceptance
`SOURCE_QA=PASS`; `WEBGL_ES100=PASS`; `PRODUCTION_BUILD=PASS`; `UNIT_72_72=PASS`; `LOVABLE_SYNC=PASS`.
`USER_VISUAL_SIGNOFF=PENDING`, `REAL_BROWSER_GPU_QA=PENDING`, `STAGE_COMPLETE=FALSE`. Tests prove shader source geometry and deterministic behavior; do not claim actual visual approval. User to check 20–30 seconds that jets are shorter and pointer distorts rather than brightens.
