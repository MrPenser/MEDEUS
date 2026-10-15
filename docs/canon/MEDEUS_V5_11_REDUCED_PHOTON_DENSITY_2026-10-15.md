# MEDEUS V5.11 — Reduced visible photon density, native crystal and glyph preservation

Date: 2026-10-15.
User: "ок. сделай меньшее количество фотонов" → "сама". Decision: EXTEND approved V5.10 with a smaller **visible photon population only**, no user request to change image, crystal assembly or timing.
Disposition: EXTEND V5.10, no new visual asset, no extra shader, microcrystal workflow unaffected.

## Executed change
Active site GitHub `MrPenser/medeus-master-asset`, branch `main`, final HEAD `ca02da3f39f780b1025d08204da24d0f73c70cef`.
- `src/lib/medeus/glyph-fog.ts` commit `df0866d81297fa3392bce3a8ebb8d8afa878cc97`: added named limits `EMISSION_PHOTON_LIMIT=60`, `TRAVEL_PHOTON_LIMIT=90`, `PHOTON_SAMPLE_DIVISOR=2`, with `photonStep(N,limit)=max(2,ceil(N/max(1,limit)))`. This guarantees at most 60 emitted particles and 90 travelling particles even on long glyph strings; at least every second particle is skipped for short sentences. `REVEALED` resident shimmer uses every 8th instead of every 4th particle. Photon core/trail appearance and motion/click origin unchanged.
- **Important:** Did NOT increase the raster sampling `stride` or truncate `this.ps`, because those samples are used to reconstruct target letter outlines. `this.glyphs`, progressive character timing, `prepare()` rasterization and `crisp()` are unchanged. The existing internally sampled `OrbMicrocrystalGather`, sphere WebGL optical compression, 1.8s PROCESSING → 0.3s compression → emission → materialization, and the no-blur photon style of V5.10 are preserved. User-restored STATIC original V4 microphone lines remain static, no V5.6–V5.9 experiment added.
- `src/lib/medeus/glyph-fog.test.ts` commit `4b5bb916bb43e9f8bc6775e11f901ed062a94034`: regression covers cap math for sample counts 1..2000, actual Canvas2D photon draw counts across EMITTING/MATERIALIZING/REVEALED and unchanged glyph targets. No fake test success by deleting source particles.
- `.github/workflows/medeus-liquid-orb-qa.yml` commit `ca02da3f39f780b1025d08204da24d0f73c70cef`: enforces exact caps and protection of glyph sample set, crystal gather and previous invariants.
- GitHub Actions `38714702666` on exact HEAD COMPLETED SUCCESS: shader GLSL ES100 compile PASS, Vite/Bun production site build PASS, **80/80 unit tests in 12 suites PASS**. https://github.com/MrPenser/medeus-master-asset/actions/runs/38714702666
- Lovable `76dd8168-469d-4edb-88f6-f313be1c1de8` `ready`, `agentFinished=true`, exact `latest_commit_sha=ca02da3f39f780b1025d08204da24d0f73c70cef`. Preview: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/ . `is_published=false`.
- Approved V4 image `src/assets/MEDEUS_MASTER_VISUAL_V4_APPROVED.png` SHA256 `773f67be7fea7fb8b3dd63b88f58dd55d01e82b0724ed3098db317a8d4f8d5b6` remains unchanged. Original static waveform, separate mic response, V5.5 coronal motion, and physical hover preserved.

## Acceptance status
`SOURCE_QA=PASS`; `GLSL_ES100=PASS`; `BUILD=PASS`; `UNIT_TESTS=80_80_PASS`; `LOVABLE_SYNC=PASS`. `USER_VISUAL_SIGNOFF=PENDING`, `REAL_BROWSER_VISUAL_QA=PENDING`, `STAGE_COMPLETE=FALSE`. The reduced visible particle count is guaranteed by code and unit tests but subjective aesthetic preference needs user observation. Do not automatically further reduce brightness or particle sizes.
