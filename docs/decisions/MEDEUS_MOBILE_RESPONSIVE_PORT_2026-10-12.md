# MEDEUS — Mobile-responsive WEBSITE port
**Date:** 2026-10-12 · **Trigger:** explicit user instruction "Адаптируй для мобильного".
**Status:** `SOURCE_COMMITTED_AND_LOVABLE_SYNCED` / `PHYSICAL_DEVICE_ACCEPTANCE_PENDING`.

## Scope and immutable boundaries
- This is the **same single-page HTTPS website**, not an installable mobile app or new mobile project.
- Earlier `DESKTOP_FIRST / MOBILE_DEFERRED` sequencing is superseded **only for scheduling**, as the user has now requested the phone version.
- The approved image `MEDEUS_MASTER_VISUAL_V1_LOCKED.png` remains byte-identical with SHA-256 `52244e15720d0dd40faa04914a44f8051a6466c166973b2609ea5d58f0e1de88`.
- Approved-for-now ten-state `src/lib/medeus/orb-field.ts` remains unchanged, blob `04fbf8a4432d55cdb964096b42949bb24a248643`. The visual master, desktop sharp cosmic field, original microphone/icon relocation and 1.4s/3.9s photon schedule all remain in place.

## Implementation
- Mobile breakpoints: `width<=720` or `height<=520 && width<=1024`; responsive browser viewport, no UI gutters.
- `src/lib/medeus/mobile-field.ts` renders the same verified, in-memory presentation scene via exact aspect-preserving isotropic transform with full-bleed cover underlay on phone. No generic image replacement, blurred borders or phone app wrapper.
- Mobile layout center: `orb.x=viewportWidth/2`, `orb.y=0.395*viewportHeight`. Orb visual scale `min(viewportHeight/1086, (viewportWidth-20)/(2*222*1.07))`; mobile orb display factor `1.07`, desktop remains factor `1.23`. The 1.07 factor makes the entire orb fit width with at least approximately 10 CSS pixels either side.
- The answer baseline remains at the source-relative `y=823` (above mic at `y=973`) with independently wrapped `maxWidth = 84% viewport`. User touches sphere -> true orb coordinates for photon emission. Mic touch -> voice attempt, photon source continues **inside orb** (previous real orb contact or orb-local fallback).
- Mobile text entry: invisible but accessible native textarea using synchronous touch focus. Supports native Android/iOS soft keyboard, Cyrillic/IME, editing, paste, Enter/Send and Escape; no visible form box. If speech recognition is unsupported, mic gesture falls back to native keyboard.
- `src/routes/__root.tsx` now declares `viewport-fit=cover`; mobile overflow/overscroll CSS is bounded to responsive viewport.
- WebGL ten-state behaviors and normal desktop layout are not rewritten.

## Visual geometry smoke-check — calculated, NOT browser tested
| Viewport | Scale | Sphere center | Sphere diameter | Text baseline | Mic center |
|---|---:|---:|---:|---:|---:|
| 390×844 | 0.777 | (195,333) | ~369 px | ~641 px | ~758 px |
| 360×800 | 0.716 | (180,316) | ~340 px | ~599 px | ~707 px |
| 320×568 | 0.523 | (160,224) | ~248 px | ~431 px | ~510 px |
| 844×390 | 0.359 | (422,154) | ~171 px | ~296 px | ~350 px |

These computations validate the *design formula* but not iOS/Android safe areas, OS keyboard behavior or WebGL mobile performance.

## Checkpoints
- Private working code `MrPenser/medeus-master-asset` latest synced GitHub commit: `e4cb31a05e3f3238dce4f143035168a825f890cc`.
- Lovable `get_project` returned exact latest commit above, `status=ready`, `agentFinished=true`. **Source-to-preview sync** verified.
- `MOBILE_SOURCE_PORT=COMMITTED`; `LOVABLE_SYNC=PASS`; `DESKTOP_REGRESSION_NOT_INDEPENDENTLY_TESTED`; `PHYSICAL_ANDROID_CHROME=NOT_RUN`; `PHYSICAL_IOS_SAFARI=NOT_RUN`; `VOICE_PERMISSION_ON_DEVICE=NOT_RUN`; `MOBILE_VISUAL_SIGNOFF=PENDING`.
- No assertions of real predictions, payment or production traffic.

## User test / next action
Open https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app directly on phone browser (not HTML preview). Tap sphere to open frameless keyboard text; Enter to watch photons emerge from orb. Tap relocated mic for supported native speech recognition; a non-supporting browser uses keyboard fallback. Rotate to landscape. Report clipping, unreadable branding, native keyboard failures, dynamic WebGL lag or errors. `STAGE_STATUS=NOT_COMPLETE` until human signoff.
