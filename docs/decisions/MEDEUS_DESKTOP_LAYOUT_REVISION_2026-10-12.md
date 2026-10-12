# MEDEUS desktop layout revision — accepted requirements / website implementation
**Date:** 2026-10-12 · **Decision authority:** latest explicit user instructions.
**Status:** `SOURCE_IMPLEMENTED`, `LOVABLE_SYNC_VERIFIED`, `VISUAL_USER_SIGNOFF=PENDING`.

## Six-point execution specification
1. **Delete left marginal footnote** `PROBABILISTIC INTELLIGENCE INTERFACE` from displayed scene, not the original locked PNG.
2. **Delete right marginal footnote** `PATTERN PROBABILITY INSIGHT` from displayed scene, likewise preserve original PNG.
3. **Move the original microphone** below the generated answer. Do not redesign the icon: use its exact cropped pixels from the approved visual with a presentation-only radial mask. Reposition its center to original-source coordinates `(723, 973)`.
4. **Answer above microphone:** dynamic response and frameless typed question centered at original-source `y=823`; microphone below at `y=973`. The old baked-in `SPEAK / THE CORE IS LISTENING` text and waveform are presentation-only suppressed, not altered in source PNG. Mic area must remain clickable as an alternate input surface.
5. **Faster but still photographic materialization:** reduce particle emission from `3500ms` to `1400ms` and materialization from `8700ms` to `3900ms`. Retain progressive diffuse fog → contours → letters → words; do not revert to instant falling characters.
6. **Do not change** the accepted-for-now ten state shader modes, the exact master image SHA-256, the sharp full-bleed cosmic-field topology, no-registration constraint, or desktop-browser-first delivery.

## Media / source authority
- **Immutable original:** `MEDEUS_MASTER_VISUAL_V1_LOCKED.png` with SHA256 `52244e15720d0dd40faa04914a44f8051a6466c166973b2609ea5d58f0e1de88`.
- Since the requested text and original mic are baked into the bitmap, **source pixel immutability and changed presentation** require a separate in-memory derived composition of the original pixels. This user-authorized presentation derivative does not change the original master binary. It only suppresses requested regions / moves original copied microphone pixels. No AI redraw or unrelated design changes.
- **Implementation files** in private working code repo `MrPenser/medeus-master-asset`: `src/lib/medeus/presentation.ts`, `src/lib/medeus/cosmic-field.ts`, `src/components/medeus/MedeusStage.tsx`, `src/lib/medeus/glyph-fog.ts`.
- Latest implementation commmits: `4c0c1db4e85ee1e6773c1c49c10d09b43eaca3aa` → `a147e1c7c3b2162037eba7b0270451b89310ec62` → `9ca2201f84898239076370a48d0aaee402bc0bfa` → `ae74548496919c3276d5ceca39ef6f5549ee4c79` → `6897b6beab181803089ea0f741d66f60b9cdba83` → `235fed4190b9558f43eeab302a7de492e421517e`.
- Last Lovable project readback `latest_commit_sha=235fed4190b9558f43eeab302a7de492e421517e`, `ready=true`, `agentFinished=true`; verifies **GitHub-to-Lovable source synchronization**, not user's visual acceptance.
- **Unchanged core-state shader:** `src/lib/medeus/orb-field.ts` blob `04fbf8a4432d55cdb964096b42949bb24a248643`. Frozen under provisional visual approval.

## Testing boundary
- A local source-image presentation approximation was visually examined to ensure labels disappeared and the microphone is below the answer zone; this is NOT an independently acquired screenshot of a live browser.
- `BUILD_READY_PROVIDER=REPORTED`; `BROWSER_INTERACTION_QA=NOT_INDEPENDENTLY_RUN`; `HUMAN_VISUAL_ACCEPTANCE=PENDING`.
- Next action: user refreshes Lovable preview on desktop and checks (a) both side labels gone, (b) microphone below text, (c) no hard masking seams, (d) text appears significantly faster while retaining mist-to-glyph effect. Fix any observed failures only; no unsolicited core state redesign.
