# MEDEUS — Original static microphone image restored (2026-10-15)

## Decision and user authority
On 2026-10-15, the owner rejected the attempted microphone voice-wave animations: "ерундаверни статичнуюкартинку". Disposition: **SUPERSEDE / ROLLBACK V5.6–V5.9 microphone-waveform visual experiments**, restore the earlier owner-approved V5.5 static original microphone lines. Do not confuse this with reverting the living star: existing V5.5 stellar surface motion, 8-sector short eruptive corona, physical nonluminous orb hover, separate mic hover/click, all ten FSM states and demo voice/text responses remain supported exactly as in V5.5.

## Exact executable website rollback (verified)
Private site repo: `MrPenser/medeus-master-asset`, `main`.
- New **forward-only** revert commit `f6eb5308e74bf0074cb3acf2e5e6e4ab0f6088b0`; parent remains previous `f4b81b3bbf9d7d4abc7c58cbfacb610d16c05b44`, **no history rewritten or force-pushed**, connected Lovable sync preserved.
- Exact returned **Git tree SHA256/ID** `aa1aa5263edbc8810ffd522bd195af3c034e1c9e` matches **bit-for-bit Git tree of pre-audio V5.5 baseline commit** `1b5c8f0f56c819bb49199352dab29f1b7cbdec15`. All repository files equal the former tested V5.5 source, not only a visual approximation.
- The following five paths restored to their exact historical V5.5 Git blobs: `src/components/medeus/MedeusStage.tsx`, `src/lib/medeus/speech.ts`, `src/lib/medeus/response-channel.ts`, `src/lib/medeus/temporary-greeting.ts`, `.github/workflows/medeus-liquid-orb-qa.yml`.
- Four V5.6–V5.9 audio-visual modules/tests deleted from HEAD (history retained): `src/lib/medeus/mic-voice-lines.ts`, `src/lib/medeus/mic-voice-lines.test.ts`, `src/lib/medeus/mic-waveform-material.ts`, `src/lib/medeus/mic-waveform-material.test.ts`.
- All obsolete speech-meter AudioContext/getUserMedia duplication, source-image waveform segmentation, per-column pixel transformation, synthetic painted audio lines and `?waveProbe=1` diagnostic removed.
- Approved source bitmap `src/assets/MEDEUS_MASTER_VISUAL_V4_APPROVED.png` remains original byte-identical image (SHA256 `773f67be7fea7fb8b3dd63b88f58dd55d01e82b0724ed3098db317a8d4f8d5b6`); the **existing artwork of the microphone waveform is now stationary**, with no overlay or damaged field rectangles.
- Verified Lovable project `76dd8168-469d-4edb-88f6-f313be1c1de8` `ready`, `agentFinished=true`, `latest_commit_sha=f6eb5308e74bf0074cb3acf2e5e6e4ab0f6088b0`; preview https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/ . Not publicly deployed (`is_published=false`).

## Validation and acceptance
- Git tree identity is unambiguous: `V5_5_TREE_RESTORED=PASS`; `LOVABLE_SYNC=PASS`.
- Followup GitHub Actions run `38707866999` on rollback commit to confirm GLSL ES100 and production build, using exact V5.5 workflow. Read completion before asserting CI pass.
- Owner request is **restore** to static image; do NOT resurrect any voice-reactive waveform animation unless explicitly requested anew.
- No new final visual signoff is required to assert source rollback identity; real browser rendering remains unverified until observed.
