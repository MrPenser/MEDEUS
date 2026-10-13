# MEDEUS V3.6 — NO rotation; native V3 depth, softer breathing and featureless-center repair
Date: 2026-10-13
Disposition: EXTEND V3.5 (new user visual instruction supersedes earlier approval of V3.4 rotation)
Status: SOURCE_QA=PASS / LOVABLE_MIRROR=PENDING_AT_RECORDING / USER_VISUAL_SIGNOFF=PENDING / STAGE_COMPLETE=FALSE

## Authority and observed defect
- User provided direct visual screenshot of V3.5 and reported visible horizontal/diagonal UV stripes during rotation.
- User command: "видны такие полосы при вращении. давай уберем вращение оставим просто реалистичную глубину и дыхание менее интенсивное"; user explicitly approved direct source edit: "меняй сама разрешаю".
- The previous approved V3.4 spin is NOW revoked. Latest owner direction wins.
- Prior canonical checkpoint: `docs/canon/MEDEUS_V3_5_NATIVE_DEPTH_NO_WET_SHADING.md`.
- Source recall: `MrPenser/medeus-master-asset@d1859f5284bad8eadc7c8b533d5bb0584bc2cbe9`, mirrored by Lovable at start; no unrelated file changes requested.

## Exact implemented changes (website source)
- `src/lib/medeus/orb-field.ts`, commit `69e5c8b519032e9999d58d96a12e6e6b44f8b009`:
  - Deleted entire `oceanAxisTurn`, `oceanSphereRotation` and `oceanVolumeCurrent` rotation pipeline plus its call from the active render pass. There is **no 3-D hemisphere projection, no warped spinning source UV or static orbital geometry**. V3 pixels sample in native source image coordinates, barring breathing and local user-input optical displacement.
  - Retained native original V3 detail `vec3 originalV3=tex(pBelow).rgb` and subordinate cognitive-state material modulation, no artificial wet specular in default mode.
  - Reduced default hover/refraction factors from `0.012 -> 0.006` and `0.022 -> 0.014`. Historic `?volume=off` fallback remains at `0.056` / `0.104` and its classic wet appearance.
  - Retained V3 source donor pixels from `oceanLayerA/B/C` inside max radius `0.86`; color-only overexposed repair `whitePlateau`, and added **neutral near-black flat-pixel** `darkPlateau` repair with 0.68 maximum opacity. No circular center-radius mask, no new drawing or edited image. Blue/violet shadows are preserved by chroma gating.
  - Breathing GPU clamp reduced from ±2.7% to ±1.2%.
- `src/lib/medeus/breathing.ts`, commit `f8fcf606b7e5c19c895f25b53f97baf41912f36d`: phase speed lowered from 0.86 to 0.69; strength 0.006–0.011 radius fraction (formerly 0.014–0.026) and micro noise <= 0.00035; reduced-motion multiplier 0.3 retained.
- `src/lib/medeus/breathing.test.ts` commit `89bb226a139a59326f713e6cc1c0c5d950d4726d`: softer amplitude/variability assertions.
- `src/lib/medeus/core-flow.test.ts`: no-active-spin, exact native depth, center repair, gentle breath and micro preservation tests. Last commit `9d3a8330be36b6169f733d09ea487b48d97fe99d` fixes harness selector (vertex shader's earlier `void main` incorrectly selected over fragment shader). The harness selector failure was **test code**, not a demonstrated product rendering failure.
- `.github/workflows/medeus-liquid-orb-qa.yml`: commit `815b04554ee4206e62e718a31ddf54620eff1864` enforces no spinning UV rotation, native V3 material depth, no default wet sheen, gentle breathing, immutable master and mic/fallback invariants.
- Full website CI HEAD `9d3a8330be36b6169f733d09ea487b48d97fe99d`, GitHub Actions `38375660791`: GLSL ES100 WebGL orbital/microphone compilation PASS, Bun/Vite build PASS, **39/39 tests PASS, 9 suites**.

## Preserved invariants
- Approved V3 master `src/assets/MEDEUS_MASTER_VISUAL_V3_NO_CAPTIONS.png` unchanged; SHA256 `9aac52baeac03d61a35ea9809d3580128952de1ae14d77f43c97a5fb7585c50d`; no image generation and no modification to screenshot.
- Original desktop/mobile scene, planets, text, interactive layout, all 10 cognitive FSM states, voice/text paths, independent microphone hover/press, large sphere click wave and hover, non-identical resting breath.
- Default `uVolumeFlow` flag now means sharp unrotated native master + repair (historic variable name only, not global fluid motion).
- `?breath=off` disables breathing; `?volume=off` / `?core=off` retain prior fallback; `?surface=classic` remains classic rendering.

## Hard acceptance boundary
- `SOURCE_QA=PASS` / `AUTOMATED_TESTS=39_39_PASS` / `SHADER_GLSL_ES100=PASS`; no claim of live browser visual acceptance.
- Latest visual evidence is **pre-fix** screenshot from user, documenting striping before removal; it does NOT establish that post-fix has no visible holes.
- `NO_STRIPES_VISUAL_PASS=PENDING`, `NO_HOLE_VISUAL_PASS=PENDING`, `SOFT_BREATH_USER_ACCEPTANCE=PENDING`, `DESKTOP_MOBILE_REAL_BROWSER_QA=PENDING`, `STAGE_COMPLETE=FALSE`.
- Post-fix visual inspection on desktop and mobile, idle/hover/press 20–40s required before promoting/locking.
- GitHub source: https://github.com/MrPenser/medeus-master-asset
- Preview: https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/
