# MEDEUS — Desktop visual corrections / acceptance gate v2
**2026-10-12 · `OPEN / USER_REJECTED_CURRENT_VISUALS` · Current Lovable commit:** `a06fd137bded5eb167ef2701f63e8e3ee0d9b7ab`.

## Reported visual defects (HUMAN observed)
1. Black/visually empty side strips remain: website composition still appears as a narrow bounded picture; full desktop viewport is not occupied by the cosmic scene.
2. Materialized letters arrive too abruptly, reading as falling/spilling characters rather than gradual smoke-to-text condensation.
3. The ten states are not sufficiently perceptually distinct; current reviewer can recognize **fewer than five**. Defining ten `enum` values and code paths does **not** satisfy this criterion.

**Disposition:** `DESKTOP_VISUAL_GATE=FAIL` (observational, not independently instrumented), `SOURCE_MASTER_LOCKED`, `MOBILE=DEFERRED`; do not relabel as PASS based on code generator's report.

## Source-derived diagnosis (read of actual Lovable source; not speculative)
- `MedeusStage.tsx` uses `<img className="... object-contain ...">` for authoritative central master; its letterbox in wide viewport is an inevitable ratio mismatch. `medeus-gutter` blur/cover was added, but lacks feathered compositing/edge matching and did not satisfy user viewing.
- `glyph-fog.ts`: `EMIT_MS=2400`, `MATERIALIZE_MS=3400`, a single global `crisp` alpha ramp `clamp01((t-2.3)/0.9)` draws ALL lines together in under 1s. Particles converge before an instant text reveal. This violates **progressive letter → word → sentence**.
- `orb-field.ts` contains 10 shader branches, but effects share texture displacement and do not produce demonstrably distinct observable fields under target desktop viewing conditions. Core motion code exists but user visual acceptance is FAIL.
- Speech recognition/display status is not sufficient evidence of microphone functioning; show `LISTENING` only after actual recognition start.
- The master asset is approved: `MEDEUS_MASTER_VISUAL_V1_LOCKED.png` SHA256 `52244e15720d0dd40faa04914a44f8051a6466c166973b2609ea5d58f0e1de88`. **Do not redraw or change source pixels.**

## Proposed repair contract — no new aesthetic master
### A. Full-bleed desktop, composition preserved
- Keep canonical foreground master aspect-preserving and unaltered.
- Extend outside its native aspect using a *single* darkened, softly blurred version of the **same master** scaled to cover entire viewport.
- Feather the foreground's LEFT and RIGHT outer edges over ~6–10% of the foreground width, such that no hard rectangular border appears. Avoid duplicating recognizable objects in the side gutters; edge-color sampled/mirrored bands are also allowed if measured from SAME master.
- No empty solid-black side bar at viewport widths `1227×699`, `1366×768`, `1440×900`, `1920×1080`. Evaluate desktop aspect and full-scene retention simultaneously.
- If user instead demands original pixels spanning the whole width with NO extension, this mathematically requires vertical cropping (`cover`) or distortion; **ask separately** before altering composition. Do not distort.

### B. Slow fog-to-glyph materialization, not letter rain
- Emission from the user's recorded pointer coordinate `(clientX,clientY)`, preserved through state transition.
- Starting stage should be broad/smoky and sparse, never a burst of crisp dots/letters at contact.
- Use staggered **character** reveal schedule: spectral clusters condense to glyph contours, stroke point density rises, and word visibility follows their completed letters. Only then the next word and eventually whole sentence; never `fillText(allLines)` with one late global opacity ramp.
- Make timing content-dependent: short phrase ~5–7 s; longer phrase dynamically 7–12 s; do not hard-code global final fade at 2.3s. If reduced motion: show stable text accessibly without photic intensity.
- Per-particle velocity must ease-in/ease-out; particle sprite size and blur shrink continuously **as distance to glyph target decreases**, not simply by elapsed time; soft haze first, final crisp glyph after ≥80% path. Gradual intensity increase near arrival.
- Suggested first calibration: emission ~3–4 s, materialization 5–8 s, particle cap 400–750 on ordinary desktop; adjust to real fps, do not equate these starting values with canon.

### C. Ten visibly distinct core motions
- Keep shader/canvas tied to master pixels. No universal rotating vortex.
- `DORMANT`: low-amplitude breathing, no continuous global spin.
- `AWARE`: localized shock wave anchored to contact point, not a generic halo.
- `LISTENING`: clearly inward rippling field; react to measured audio amplitude only if available.
- `RECEIVING_TEXT`: directional filament focus/structured gathering.
- `PROCESSING`: intense non-rotational asymmetric contraction/compression, then release.
- `EMITTING`: asymmetric outward pressure/flow FROM contact, continuous fog transfer.
- `MATERIALIZING`: field synchronizes with evolving text, luminous concentration migrates toward letters.
- `REVEALED`: distinct stable resonance/settling, not same as DORMANT.
- `DEEPENING`: layered outward disclosure, slow nested expansion.
- `ERROR_SILENCE`: irreversible-looking but recoverable attenuation/quiet.
- Render 10 actual short browser videos with **NO overlaid state names**. Hold each state 3–5 seconds; side-by-side comparison must allow reviewer to distinguish **all ten**. If fewer than 10 are clear, `MOTION_ACCEPTANCE=FAIL`.
- Test ordinary path + debug state forcing separately. Demonstrating the ordinary happy-path alone cannot exercise optional error/deepening states.

## Gate checklist
- [ ] 1227x699 full-viewport composition, no black hard-edge columns; 1440x900 and 1920x1080 too.
- [ ] Frozen master PNG hash verified; no generative substitution.
- [ ] Gentle mist at EXACT click point, ≥3s pre-glyph, no instantaneous letter rain.
- [ ] Each word appears through its own glyphs, no all-lines opacity snap.
- [ ] RU & EN both materialize legibly, mixed scripts do not break layout.
- [ ] State-by-state real desktop recording (10 × ~3–5s), 10/10 behavior human signoff.
- [ ] Separate unlabelled 2s A/B clips for `DORMANT`, `LISTENING`, `PROCESSING`, `REVEALED`; no spinner.
- [ ] Real browser performance and error console; reduced-motion path.
- [ ] Changes confirmed in Lovable built website (not just GitHub docs); user signoff.

## External blocker / workaround
At this checkpoint, `Lovable.send_message` rejected additional edits/QA with `WORKSPACE_OUT_OF_CREDITS`. GitHub docs may still be updated, **but changing a document does not patch Lovable site**. Possible user-authorized routes: restore Lovable credits, or connect/export Lovable source to GitHub and edit through ordinary version control. Never misrepresent either as already accomplished.
