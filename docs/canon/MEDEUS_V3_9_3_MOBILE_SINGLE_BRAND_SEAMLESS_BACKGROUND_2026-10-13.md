# MEDEUS V3.9.3 — Mobile single brand and seamless cosmic background

Date: 2026-10-13
User screenshot: Android Chrome, source issue at current V3.9.2 mobile preview: duplicated "ASK WHAT MATTERS" and large MEDEUS overlaid in the background, plus straight horizontal nebula seams. The user confirmed lowered mic remains correctly positioned. Latest directive: "Микрофон на месте. Текст дубль с наложением".
Disposition: EXTEND mobile only; SUPERSEDE mobile V3.9.2 dual-pass background composition. Preserve mic position and all sphere/voice interactions.
Source QA: PASS; CI 58/58 PASS; Lovable sync verified; live on-device visual approval pending.

## Verified root cause
1. `src/lib/medeus/mobile-field.ts` painted a lateral nebula cover, then overlaid **the complete aligned V3 bitmap minus only the top 7.5%**. The original master still contains the MEDEUS logo and accompanying ASK WHAT MATTERS lower than that cutoff. Thus the mobile HTML headline and baked title both remained onscreen. Overlaid pixel layers also had mismatched composition at the top/bottom of the aligned frame, creating visible horizontal seams.
2. `src/components/medeus/MedeusStage.tsx` drew a separate mobile header containing only `ASK WHAT MATTERS`. The user correctly identified double title.
3. Mic position was previously fixed. DO NOT move it again or regress hit testing, touch, independent voice behavior or fallback.

## Source repair
Private site repo `MrPenser/medeus-master-asset`, branch `main`:
- `src/lib/medeus/mobile-field.ts`, commit `e25b390fdb60bac872a5900e5c6848c3c5e5352b`: mobile background is **exactly one continuous full-viewport drawImage**, using a left-lateral nebula subsection of the immutable V3 master: x [0.075, 0.325] of 1672px, y [0.095, 1] of 941px. The crop is outside the old central orb and baked logo; no second aligned full-image content pass, no title strip draw, no source mic ghost, no destination-out mask, no horizontal content-plane seam. Keep original image immutable; do not invent or generate background art. `MobileFrame` argument is maintained for caller compatibility but does not affect drawing.
- `src/components/medeus/MedeusStage.tsx`, commits `4984dffdc0b6ebf2368fe59194f483d92776eac3` and `de5e8f6ca87bfaafbf06f5e0318fb2dd9d2d5b6f`: mobile-only HTML title is now a single semantic branding stack with large `MEDEUS` and one subordinate `ASK WHAT MATTERS` line, instead of standalone ASK repeated over baked words. CSS absolute top safe area, original typography family, no overlay image. Desktop JSX remains unchanged.
- `src/lib/medeus/mobile-layout.test.ts`: commit `4fa2a0b26e46de4e0bc96c377605edb706ef0ad7`; malformed test regex later fixed `bb2aac6c2ac2c1c30e58b8417f475c61d88131c1`. Static check: one mobile `drawImage` call, no aligned overdraw, crop strictly beyond orb boundary, exactly one tagline literal in Stage, mic touch and its existing safe move preserved, original geometry unchanged.
- `.github/workflows/medeus-liquid-orb-qa.yml`: commits `b9b33131730a0c137ecfed4fec6182f9abf4a1ae` and `bda4b4935451ea6b520fd889b01c8e9165ca3472` update mobile single-pass/title gates and add mobile-layout/test files to workflow trigger paths.
- **Final website HEAD: `bda4b4935451ea6b520fd889b01c8e9165ca3472`**.
- GitHub Actions `38411074573`: SUCCESS, both GLSL ES100 orb/mic shaders and Bun/Vite site build PASS; **58/58 unit tests PASS across 10 suites**. An intermediate run at `b9b33131` failed solely because of a malformed regular expression in the new test (not a product shader failure); the final run passed.
- Lovable project ID `76dd8168-469d-4edb-88f6-f313be1c1de8`, READY with latest_commit_sha exactly `bda4b4935451ea6b520fd889b01c8e9165ca3472`, independently verified.
- Preview https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/

## Preservation / verification policy
- V3 authoritative bitmap `src/assets/MEDEUS_MASTER_VISUAL_V3_NO_CAPTIONS.png`, SHA256 `9aac52baeac03d61a35ea9809d3580128952de1ae14d77f43c97a5fb7585c50d`, unchanged. Runtime mobile crop uses only original pixels; desktop full-scene draw unchanged.
- Independent microphone field is at the already accepted lower mobile position; touch/hover, speech, text, keyboard and full 10 FSM unaffected. V3.9 inner pearl sphere, single click wave, gentle breathing, no rotation all preserved. Keep source rollback toggles.
- `SOURCE_QA=PASS`, `CI=PASS`, `LOVABLE_SYNC=VERIFIED`; `ANDROID_ACTUAL_NO_DUPLICATION_VISUAL_SIGNOFF=PENDING`, `IOS_VISUAL_QA=PENDING`, `STAGE_COMPLETE=FALSE`. The source and structural tests do not prove the exact mobile screenshot post-change; request owner to refresh preview and inspect on phone before locking this visual stage.
