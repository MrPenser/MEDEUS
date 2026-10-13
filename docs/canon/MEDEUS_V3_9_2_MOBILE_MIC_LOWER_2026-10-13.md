# MEDEUS V3.9.2 — lower mobile microphone without phantom duplicate

Date: 2026-10-13
User directive: "Микрофон опусти ниже" then "Сама".
Disposition: EXTEND mobile-only V3.9.1 stage, no replacement of approved scene, shader, 10 FSM, microphone motion, body size, original title, or desktop.
Status: SOURCE_QA=PASS / CI=PASS / LOVABLE_SYNC=PENDING_VERIFICATION / USER_MOBILE_VISUAL_SIGNOFF=PENDING / STAGE_COMPLETE=FALSE.

## Recall and observed interaction hazards
- Last verified site HEAD `b041a253cdee783fab57be0da562879ba074f657`, Lovable mirror same at recall.
- Mobile render `src/lib/medeus/mobile-layout.ts` originally used source y position `y + (PRESENTATION.micY - orb.cy) * s` with no additional offset. Simply moving its canvas would have left React pointer-down/hover tests in the original position and a **baked microphone illustration** behind in the unmodified V3 source backdrop.
- Therefore a correct mobile-only movement must modify geometry, pointer/hover coordinates and the displayed original-image backdrop together, while leaving source master and desktop unchanged.

## Committed website changes (`MrPenser/medeus-master-asset`)
1. `src/lib/medeus/mobile-layout.ts` commit `56fbae966578857945ff8cc01b5769fa51425b1c`: reserve `roomBelow` and lower mobile mic by `min(40px portrait / 20px landscape, max(0, roomBelow-4px))`. On compact screens the displacement is reduced to avoid clipping below `safeBottom`. Orb center/radius unchanged. Response gap recomputed from moved mic.
2. `src/components/medeus/MedeusStage.tsx` commits `b8d4bda804dea0a0b78463a1fdb629f85b9bc1fb`, `df61b950f3cacbced8de27c6aef570a5e90c3378`: add mic coordinates to shared `geo` reference so the live mic canvas, pointer-down hit testing, mic-only click ripple, mobile touch and desktop mouse/pen hover share the **same final center**. Pass microphone displacement to mobile panorama painter. Desktop coordinates retain the exact previous `fx + PRESENTATION.micX * s` and `fy + PRESENTATION.micY * s`.
3. `src/lib/medeus/mobile-field.ts` commit `d0325091690f1fc7fccbf0e7fb76396d45b79dfd`: when the mic is moved, erase only the original baked mic from the aligned mobile source layer with a soft `destination-out` radial feather, exposing the already verified lateral cosmic backdrop. The independently rendered live mic remains visible at the new lower location. This is runtime mobile sampling/compositing, no mutation of original V3 PNG or a new generated art asset.
4. `src/lib/medeus/mobile-layout.test.ts` commit `8a2b383d3c3731e0a81fb9b03e86aed7da69ee85`: 10-screen mobile geometry, tall-screen expected 40px shift, compact screen nonoverflow, mic pointer/click coordinate alignment, feather-mask suppression of ghost mic, preservation of original title/globe layout.
5. `.github/workflows/medeus-liquid-orb-qa.yml` commit `673174c86bc9abec964a936ee599ca6318deeb59`: gates the lower mic, pointer alignment, baked mic suppression and all existing source custody, shaders and FSM invariants.

## Verifications
- Website HEAD `673174c86bc9abec964a936ee599ca6318deeb59`.
- GitHub Actions run `38405058510`: orb+mic GLSL ES100 compile PASS, Bun/Vite build PASS, **58/58 unit tests PASS across 10 suites**.
- Original approved PNG `src/assets/MEDEUS_MASTER_VISUAL_V3_NO_CAPTIONS.png`, SHA256 `9aac52baeac03d61a35ea9809d3580128952de1ae14d77f43c97a5fb7585c50d`, not modified. Volume-only V3.9 internal pearl light, gentle breath, hover/click, desktop UI, microphone microphone shader and voice/text channels remain unchanged.
- Lovable project `76dd8168-469d-4edb-88f6-f313be1c1de8`; preview https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/. Confirm Lovable SHA separately: source CI success does not prove immediate mirror sync.

## Strict stage status
`SOURCE_QA=PASS`, `BUILD=PASS`, `GLSL=PASS`, `UNIT_TESTS=58/58_PASS`.
`LOVABLE_MIRROR=CHECK_PENDING`, `USER_REAL_ANDROID_VISUAL_ACCEPTANCE=PENDING`, `IOS_QA=PENDING`, `STAGE_COMPLETE=FALSE`.
The user's former screenshot showed additional website-wide heading/cosmos artwork issues; these are a separate visual-layout problem and not part of the scoped microphone relocation request.
