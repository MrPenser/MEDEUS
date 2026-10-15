# MEDEUS V5.8 — No rectangular artifacts beside voice-reactive original microphone lines
Date: 2026-10-15
User evidence: uploaded screenshot `Screenshot_4.png` showing hard-edged dark rectangular block/field artifacts near the left microphone waveform. User reports "есть артефакты полей действия звуковых полос".
Disposition: FIX/EXTEND V5.7. Do not change locked V4 image or restore V5.6 extra synthetic bars.

## Verified root cause
In `src/lib/medeus/mic-waveform-material.ts`, V5.7's `separateApprovedMicWaveform()` cleaned each WHOLE 282x104 rectangular region by interpolating source pixels linearly from the top and bottom of the strip. This produced visibly different cosmic-nebula pixels in large bounded rectangular panels near the actual waveform; a source/CI test existed but missed the resulting visible rendering damage.

## Implemented
- Live site `MrPenser/medeus-master-asset`: shader/art unchanged, mic waveform source extraction changed in commit `8c99c8e85cb605852ca7dd113db20879a0f0af64`.
- Instead of cleaning a full rectangle, `separateApprovedMicWaveform()` now conservatively detects individual bright local-contrast waveform pixels. A same-column, near-neighbor sky estimator takes the dimmest two of eight nearby y samples; spatial feathering confines modifications to the true audio band (source y=860 with a smooth ~27–45px footprint) and to interior strip x with 17px edge feather. Per-pixel removal requires both measured positive contrast >~0.095 and source luminance >~0.34, with gradual soft thresholding. Source pixels outside the detected audio material are bitwise unchanged (no painted rectangle), and extracted RGB residual is additive so static rest restores native colors. This is pixel-local in a RAM-only presentation copy; immutable source PNG is untouched.
- Genuine V4 waveform material remains the only animated line effect via `drawImage` source-pixel transport. No `stroke`, `lineTo`, extra equalizer bars or orb changes. Existing mic RMS, TTS word-boundary timing, original mic hover/click, V5.5 star, FSM remain.
- Exact approved master bitmap `src/assets/MEDEUS_MASTER_VISUAL_V4_APPROVED.png`, SHA256 `773f67be7fea7fb8b3dd63b88f58dd55d01e82b0724ed3098db317a8d4f8d5b6`, not modified.
- Regression test commit `9c60ae9058b88dc4394865b15ffc51dabb6430c5` adds synthetic strong bright *broad* nebula, smooth cloudy texture and narrow true audio line. Asserts all pixels outside the center band and bright non-audio nebula inside remain exactly original, audio source isolated, and additive residual reconstructs source RGB in silence. Workflow HEAD commit `1ce0789e6d8edf15953103bd703ddf0478303c07` forbids wholesale rectangle interpolation.
- GitHub Actions run `38682640674` at exact code HEAD completed SUCCESS, GLSL ES100 orb/mic compilation PASS, Bun/Vite production build PASS, **81/81 unit tests PASS across 12 suites**.
- Lovable project `76dd8168-469d-4edb-88f6-f313be1c1de8` code-bearing commit `8c99c8e85cb605852ca7dd113db20879a0f0af64` verified mirrored and `status=ready`. Later GitHub commits are tests/workflow only. Preview https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/ . No public production publish.

## QA boundaries
`SOURCE_QA=PASS`, `CI=PASS`, `USER_VISUAL_SIGNOFF=PENDING`, `REAL_BROWSER_GPU_AUDIT=PENDING`, `STAGE_COMPLETE=FALSE`. Do not call the screenshot artifact definitively gone until actual user visual check. If residual blocks remain, next step is compare real saved browser frames while speaking/quiet, not stronger shader gain.
