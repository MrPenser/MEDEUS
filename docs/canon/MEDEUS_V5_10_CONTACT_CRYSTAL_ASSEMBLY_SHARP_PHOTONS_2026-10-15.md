# MEDEUS V5.10 — Contact microcrystal assembly → clean photons → sharp letters

Date: 2026-10-15
Owner request: "при появлении текста раньше сама сфера какбы собиралась микрокристалами внуть точки касания и сяпала фотонами. теперь только фатоны. мне не равится что фотоны мутные и нереалистичнве. и что нет того раннего эффекта сферы"; direct consent: "делай сама".

Decision: REUSE/EXTEND legacy inward PROCESSING mote/convergence concept and the approved ten-state model. Restore the missing visible *contact-focused contraction of the sphere itself* and replace over-blurred photon rendering. Do NOT reinstate permanently visible rare crystal dashes, ambient small star speckles, geometrical axes, rotating globe, whiteout, V5.6–V5.9 rejected microphone visualizer, or any new pixel master.

## Evidence and diagnosis

- The historic `src/lib/medeus/motion-engine.ts` still includes a PROCESSING mote gather toward last contact (pure 2D historical code), but the current site uses `MedeusStage` + `orb-field` + `GlyphFog` and does NOT call that legacy renderer.
- The V5.5 `orb-field.ts` computed state-dependent `sampleOrganicState`, but the active approved V4/V5 star path replaced that material with the original V4 sampled texture and `v5StellarInterior`, so the PROCESSING gathering optical dynamics were invisible in the sphere itself.
- The live `glyph-fog.ts` produced EMITTING and MATERIALIZING via a 64x64 radial-gradient sprite with alpha haze, emitter scale ~38–142px and particle sprite scale ~14px, giving the owner-rejected dull blurry photons.
- Prior user timing intent: processing/then emitting/then materialization. State model preserved: PROCESSING 1800ms, EMITTING 1400ms, MATERIALIZING 3900ms, ten FSM states unchanged.

## Implemented site source — tested

Site repo `MrPenser/medeus-master-asset`, `main` final SHA `b5a60abf9a023abbf36872a4ae3d376d1dfc331c`.
1. New `src/lib/medeus/crystal-gather.ts`, commit `8232c89b68dda7e68bc20167277dab0566a49f0a`: native V4 RGB-pixel 4x4 facets are sampled from verified orb texture (source orb center from `MASTER_ASSET.orb`) and temporarily painted as tiny clipped, depth-varying diamond microcrystals *strictly inside the actual orb*. They deterministically converge toward the last actual valid orb touch coordinate (or the existing safe orb fallback). 132 default fragments, 152 normal rendering and 72 reduced-motion. Processing gets 1.8s for compression; first 300ms of emitting completes it; temporary shards fully fade by 500ms. No change to V4 PNG, orbit, mic, settled states, source text, or idle visuals.
2. `src/lib/medeus/orb-field.ts`, commit `3bc2a1015731070db1a8425f44733b888138b929`: the V5 star's own original V4 source UV *locally* compresses optically toward `uClick` during state indices 4 PROCESSING and 5 early EMITTING only. An inverse optical material transport plus tiny unsynchronized crystalline noise makes verified source filaments visibly draw inward together with shards. Bounded `sourceP` sampling (max normalized radius .985), no radial hole, default-state contamination, rotation, stripes, new sample donor, or drawn axes. Other V5.5 star behavior untouched.
3. `src/lib/medeus/glyph-fog.ts`, commit `4e3fb4ebf4715bd2ad5a93797c49d64198c03f62`: removes the old blurred 64px `getSprite()` radial-gradient sprite entirely. Photon launch has a 300ms hold for crystal convergence, then fine white-hot <=1.5px cores and tiny violet 0.45–1.1px strokes/trails (not haze). During MATERIALIZING photons travel from the actual touch, then arrive at glyph target points; per-character reveal has <=0.9px temporary blur and 1.8px shadow blur, becoming sharp. REVEALED/DEEPENING glyph formation and timings retained.
4. `src/components/medeus/MedeusStage.tsx`, commit `de048b0b68943513736ab6a17baa83ca12ff6ba1`: renders the crystal gathering on the existing overlay from PROCESSING and early EMITTING, with true original touch origin and responsive desktop/mobile center/radius. Canvas clipping ensures interior-only fragments; no changes to mic or voice routing, user click FSM, source master, permanent imagery or renderer defaults.

## Verification

- `src/lib/medeus/crystal-gather.test.ts`, commit `d0fb542cc9057221c045ef9ea92e91fb76982ce5`: numerically confirms distance-to-contact shrinks from PROCESSING start through end then vanishes by +300ms EMITTING, tests clipping, source-pixel sampling and finite lifecycle, reduced-motion geometry preservation.
- `src/lib/medeus/glyph-fog.test.ts`, commits `87577c491a4a2f85561a3b29d60a989275c93346` and `cdd5e6fd4e57095491cc23f5c0c3af43d8fa6302`: ensures photon release only after .3s and uses real crisp small primitives without sprite haze, honors FSM timing and static mic.
- `src/lib/medeus/core-flow.test.ts` commit `f94e71d56ec4681b2db2cf634992ab0f141dc27f`: confirms 2 transient source-optic compression states and untouched material outside phases.
- CI workflow `.github/workflows/medeus-liquid-orb-qa.yml` final `b5a60abf9a023abbf36872a4ae3d376d1dfc331c` includes new tests and verifies actual GLSL ES100 orb/mic shaders.
- GitHub Actions run `38712529123` at exact final source SHA: **completed SUCCESS**, Bun/Vite site production build PASS, real orb/mic GLSL ES100 compile PASS, **79/79 tests PASS across 12 suites**. Initial failures at intermediate commits were static substring expectations for `const e = ease` corrected to exact source spacing; final gate passed.
- Lovable project `76dd8168-469d-4edb-88f6-f313be1c1de8`, `ready`, `agentFinished=true`, latest_commit_sha exact `b5a60abf9a023abbf36872a4ae3d376d1dfc331c`. Preview https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/ . No public production publication.
- V4 master `src/assets/MEDEUS_MASTER_VISUAL_V4_APPROVED.png` remains SHA256 `773f67be7fea7fb8b3dd63b88f58dd55d01e82b0724ed3098db317a8d4f8d5b6` byte-identical. The V5.5 restored STATIC MIC WAVEFORM remains authoritative; never reintroduce rejected reactive audio bar layers unless explicitly asked.

## Open visual signoff

`SOURCE_QA=PASS`, `CI=PASS`, `LOVABLE_SYNC=PASS`, `USER_VISUAL_SIGNOFF=PENDING`, `REAL_BROWSER_GPU_QA=PENDING`, `STAGE_COMPLETE=FALSE`.
The tests verify code/physics/math and source custody, not actual optical aesthetics in the user browser. User must compare at actual response generation: source texture + crystals converge to contact (PROCESSING), pause/compress (first .3s EMITTING), short bright sharp streaks emit, text assembles (MATERIALIZING). Rejected V5.6–V5.9 microphone-wave visual work remains rolled back.
