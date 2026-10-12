# MEDEUS — Orb-only photon emission + safe enlargement
**Date:** 2026-10-12 · **Decision source:** explicit user instruction.

## Locked changes
1. **Mic is an input trigger, not an emission origin.** Click/tap on sphere: `ORB_CLICK` records actual contact point and emits from it. Click mic: use last real valid orb contact if any; otherwise an orb-internal anchor `(cx, cy+0.18*visualRadius)`. Never microphone coordinates. Both WebGL contact field and photon fog receive the same orb-local coordinate.
2. **Remove visible exterior orbit guides**, preserve original cosmic field and locked original raster. Implementation: one-time source-pixel-neighbor suppression in `src/lib/medeus/orbit-cleanup.ts` on browser-only derived `HTMLCanvasElement`. No image generation, new backdrop, or file rewrite. Do not erase central stellar texture.
3. **Enlarge the active living orb** to `visualRadius = master.orb.r * fitScale * 1.23` (about +23% radius, about +51% area). The WebGL state shader continues sampling the same original source texture; only output canvas size, state hit testing, and normalized interaction coordinates are scaled. Preserve center and all ten motion definitions.
4. **No overlap**: measured on source-coordinate fit at 1278×638, 1440×900, 1920×1080. Space between displayed enlarged orb and tagline remains about 11px, 16px, 19px respectively; gap above answer remains ≥72px on tested desktop reference sizes. Browser QA and human approval required.
5. **Immutable source:** original `MEDEUS_MASTER_VISUAL_V1_LOCKED.png` SHA256 `52244e15720d0dd40faa04914a44f8051a6466c166973b2609ea5d58f0e1de88`. No source binary changes. Previously approved-for-now ten state shader code/blob `04fbf8a4432d55cdb964096b42949bb24a248643` remains unchanged.

## Runtime source changes
Working Lovable-synced source repo: `MrPenser/medeus-master-asset`.
- `src/lib/medeus/orbit-cleanup.ts` commit `e5e65996c4a4aadc3ae1a70ef141d24825de6742`.
- `src/lib/medeus/presentation.ts` commit `b1a7afbc44f38a605e89d83bb079ab8e671987db`.
- `src/components/medeus/MedeusStage.tsx` commit `6c92b87ca0dd69e8a1697e3e5e339871921b9f20`.
- Lovable `get_project` readback: `latest_commit_sha=6c92b87ca0dd69e8a1697e3e5e339871921b9f20`, project `ready`, agentFinished=true. Lovable source readback independently confirms connected orbit cleanup, 1.23 factor, mic origin separation.

## Outstanding acceptance
`CODE_SOURCE_SYNC=PASS`, `MIC_PHOTON_COORDINATES_CODE_PATH=PASS`, `TEN_STATE_SHADER_UNCHANGED=PASS`, `HUMAN_ORBIT_REMOVAL_VISUAL_VERDICT=PENDING`, `HUMAN_MAX_SAFE_ORB_SCALE_VERDICT=PENDING`, `END_TO_END_BROWSER_TEST=NOT_RUN`. Content-aware line interpolation may leave residual fine orbital traces; do not falsely declare all orbit artifacts eliminated without current browser screenshot/approval.

Website: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app
