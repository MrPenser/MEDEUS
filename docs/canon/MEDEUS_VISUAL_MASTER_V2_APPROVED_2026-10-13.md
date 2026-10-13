# MEDEUS — Visual Master V2 (USER-APPROVED)
Date: 2026-10-13
Status: APPROVED ARTWORK / WEBSITE IMPLEMENTED / CODE QA PASS / FULL RESPONSIVE VISUAL SIGNOFF PENDING

## Visual authority and custody
The user explicitly approved the image `космическое_ядро_medeus.png` after rejecting visible orbit scaffolds, ill-defined microphone planet and partially visible left planet in V1. The user then ordered direct substitution into the existing MEDEUS website, and authorized repository access.

Canonical source (EXACT bytes):
- Original locally: `/mnt/data/космическое_ядро_medeus.png`
- Versioned GitHub source asset: `MrPenser/medeus-master-asset/src/assets/MEDEUS_MASTER_VISUAL_V2_APPROVED.png`.
- Pixel format: RGB PNG, 1672×941, source file size 2,408,121 bytes.
- SHA256: `0dd41f6c5f1381136920480e23a3c9389604834a331e6b8bcfd4e22480f5b2ba`.
- GitHub binary blob SHA1: `71d82ce9c6c396d948921a31bb4b105a36db1222`.
- Asset introduction commit: `22907e60735ab79d58655fac795c084f8b31eaa5`.
- Full master switch commit: `ddf90cc6263c6bbcee9c3432891234c1d4ec5074`.
- Source bytes never altered or regenerated, only served as a static Vite-imported image with runtime SHA256 verification.
- V1 original preserved as backup metadata and original Lovable hosted immutable asset: `MEDEUS_MASTER_VISUAL_V1_LOCKED.png`, SHA256 `52244e15720d0dd40faa04914a44f8051a6466c166973b2609ea5d58f0e1de88`. V1 is now HISTORICAL/NOT DISPLAYED, not deleted.

## Website binding
- `src/lib/medeus/asset.ts`: `MASTER_ASSET.version=V2`; `url=masterV2Url` (Vite asset import); `expectedSha256` matches above, source width=1672, height=941; orb geometry cx=836, cy=403, r=224.
- `src/lib/medeus/presentation.ts`: **identity scene** from verified PNG, no old V1 image-specific inpainting/removal/overlays. Coordinates: answerY=657, orbScale=1.0, microphone (836,810), micHitRadius=60. These are V2 source pixels. No artificial microphone stamp/planet redraw, no old crop/image blending.
- `src/lib/medeus/cosmic-field.ts`: adjusted edge band to avoid stretching the planets in desktop responsive extension; vertical stretch for 16:10 tall desktops remains a known visual review item.
- `src/components/medeus/MedeusStage.tsx`: references common `MASTER_ASSET.width/height/orb` and PRESENTATION coordinates, maps pointer/microphone/text interactions into source-space geometry. No change to 10-state FSM, breathable fluid, no stars, no crystal strokes.
- `src/lib/medeus/master-v2.test.ts`: 5 direct custody/geometry/image identity tests; immutable asset fingerprint and image dimensions enforced.
- `.github/workflows/medeus-liquid-orb-qa.yml`: verify V2 image import, dimensions and raw SHA256, prohibit V1-only presentation destructive filters.

## QA provenance
- Site GitHub Actions run `38359117816`, source SHA `ddf90cc6263c6bbcee9c3432891234c1d4ec5074`: `GLSL_ES100=PASS`, `BUN_VITE_PRODUCTION_BUILD=PASS`, `UNIT_TESTS=29/29_PASS`.
- Lovable project `76dd8168-469d-4edb-88f6-f313be1c1de8`, status ready, latest synced SHA matches.
- Lovable agent tested 1280×800 and 1440×1000 desktop with orb clicking, typing 'hello' and Enter: response appeared in new V2 band and microphone/side planets were visible on tested desktops. This is agent-reported browser QA, not independent human signoff.
- KNOWN limitations: very tall 1440×1000 previews may show faint streaks from vertical background extension; **mobile currently uses orb-centered zoom, so side planets may be cropped from the phone viewport**. Do not claim full-scene mobile visual acceptance yet. Voice input, breathing, hover and GPU smoothness not browser-regression-confirmed in this asset change.
- `VISUAL_V2_ARTWORK_APPROVED=TRUE`; `V2_SOURCE_INTEGRATION=PASS`; `V2_FULL_RESPONSIVE_VISUAL_ACCEPTANCE=PENDING`; `CONVERSATION_BACKEND_NOT_IMPLEMENTED` remains true.
- Preview: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/ .

## Mandatory inheritance
V2 replaces V1 as visual source of truth for current site. Do not resurrect old orbit-cleanup masks, old microphone crop/stamp or x723/y427 coordinates. Do not attempt generative redraw. Keep the 10 canonical state structure and never treat demos as a production forecasting backend. Visuals on mobile must be reviewed separately without weakening source checksum and current desktop layout.
