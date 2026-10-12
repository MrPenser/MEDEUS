# MEDEUS — TEN DISTINCT CORE STATES v1
**Date:** 2026-10-12 · **Status:** BEHAVIORAL_SPEC_LOCKED / MOTION_ACCEPTANCE_PENDING

**Baseline:** The master bitmap is frozen. The *orb region* gains intrinsic optical flow, refraction, local field deformation, breathing and emission. Purely spinning the center, varying rotational speed, or adding faint rings only is **FAIL**. State-specific perceptual differences must be independently testable on an actual phone.

| State | Entry / real trigger | Distinct orb behavior | Exit / gate |
|---|---|---|---|
| `DORMANT` | Initial load, no action | Very low-amplitude irregular breathing and slow non-rotating internal circulation | Pointer/voice-ready interaction |
| `AWARE` | Contact/hover, with exact coordinates | Non-global point-anchored ripple; brief local focusing at the contact coordinate | Input gesture |
| `LISTENING` | Permission granted & recognition active | Field flows inward, modulation by actual voice energy **when measurable**; otherwise neutral listen motion without simulated audio-reactivity | Recognition result/timeout |
| `RECEIVING_TEXT` | Text entry mode | Directed converging filaments; tiny local pulses from remembered contact; native keyboard but no visible input box | Submit/cancel |
| `PROCESSING` | Real request dispatched / local demo processing disclosed | Uneven radial contraction, denser internal complexity, no obligatory spin | Response/error |
| `EMITTING` | Response available & transmission begins | Soft diffuse lilac smoke originates from the *last actual orb contact point*; grows/moves toward text target | Glyph formation |
| `MATERIALIZING` | Photonic field reaches lettering zone | Diffuse cloud sharpens nonlinearly into separate photon clusters -> glyph strokes -> letters -> words -> full sentence; blur progressively decreases as target proximity increases | Final word settled |
| `REVEALED` | Answer completed | Slow stable breathing and subtle non-rotating optical resonance between orb/text | Fresh gesture/session end |
| `DEEPENING` | User requests expanded analysis; optional paid path | Nested slow luminous layers progressively unfold, without CTA button overlays or deception about completed payment | Confirm/defer/checkout |
| `ERROR_SILENCE` | Denied microphone, network failure, empty/unknown input | Light contracts then fades, recoverable silent pause; accessible localized explanation | Retry/text fallback |

### Canonical flow
`DORMANT → AWARE → LISTENING|RECEIVING_TEXT → PROCESSING → EMITTING → MATERIALIZING → REVEALED`; optional `DEEPENING` after an explicit request; any transient may go to `ERROR_SILENCE → DORMANT|RECEIVING_TEXT`.

### Touch coordinate contract
- `touch_source = (clientX, clientY, viewport size, timestamp)`, registered only after valid interaction on the core.
- Transform accurately across portrait/landscape/reflow. A later animation always uses the origin associated with the **current interaction**, not a stale tap from a previous query.
- For non-touch accessibility flows use a clearly documented fallback anchor; never fabricate a person's touch.
- Origin must be testable by touches at least at 4 separated orb quadrants with recorded trajectories.

### Motion acceptance
1. Independent short video for **each** state from real browser execution; no label-only proof.
2. Blind reviewer distinguishes `DORMANT/LISTENING/PROCESSING/REVEALED` better than chance and all 10 states show the declared behavior.
3. Physical touch position changes photon-emission origin correspondingly; no center-spawn except legitimate fallback.
4. Fog starts diffuse (large/soft), sharpens **near letters**; individual letters precede finished words, finished words precede the complete sentence; supported non-Latin scripts tested.
5. Portrait 360x800 and 390x844, landscape 844x390, low-memory Android, measured frame timings, proper pause/resume and reduced-motion behavior.
6. Browser/voice/platform errors do not accidentally transition into `REVEALED` with a fake forecast.

### Evidence disposition
Historical demos v1–v6 are **candidate experiments**, not approved behavior or production. The user explicitly rejected v4 and v5 as effectively static/rotating. v6 was demonstrated but **not user-approved**. `MOTION_GATE=OPEN`, `CORE_BEHAVIOR_VERIFIED=FALSE`.
