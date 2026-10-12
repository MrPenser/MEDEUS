# MEDEUS

**MEDEUS** is a mobile-first, voice-first, single-screen experimental interface for evidence-grounded probabilistic answers. The user-approved **visual master is immutable**. MEDEUS is a separate product/interface, not an ASTRADELIA core node.

> **Current status (2026-10-12): CANON_DOCS_IN_PROGRESS / PROTOTYPE_NOT_ACCEPTED / PRODUCTION_NOT_AUTHORIZED.** A demo is not a validated forecast service.

## Project authority
- [ROADMAP.md](ROADMAP.md) — stages, dependencies, acceptance gates.
- [Canonical product specification](docs/canon/MEDEUS_CANONICAL_SPEC_V1.md) — product UX and hard constraints.
- [Visual master lock](docs/canon/MEDEUS_VISUAL_MASTER_LOCK_V1.md) — exact raster identity and localization/mobile conflict.
- [Ten-state core model](docs/canon/MEDEUS_CORE_STATE_MODEL_V1.md) — distinct state machine.
- [ASTRADELIA integration boundary](docs/architecture/MEDEUS_PRODUCT_BOUNDARY_V1.md) — forecast evidence, safety and hosted payment.
- [Canon reconciliation](docs/decisions/MEDEUS_CANON_RECONCILIATION_2026-10-12.md) — locked/pending/conflict.
- [HANDOFF_STATE.md](HANDOFF_STATE.md) — continuation and readback status.

## Canonical visual identity

`MEDEUS_MASTER_VISUAL_V1_LOCKED.png` (approved original, currently held outside this repository pending binary custody upload).
**SHA-256**: `52244e15720d0dd40faa04914a44f8051a6466c166973b2609ea5d58f0e1de88`.

Do not redraw, replace, recolor, or alter the master asset. Runtime animation is a separate non-destructive layer; animated frames are not expected to equal the static PNG. No reinterpretation of the visual is authorized.

**Source and production:** This repository currently documents the product. Production forecasting, payment integration, verified forecasting performance, real geolocation resolution, and user approval of v6 motion are **not asserted**.

**Upstream system authority:** [ASTRADELIA roadmap](https://github.com/MrPenser/genius-ai/blob/main/docs/roadmap/ROADMAP.md). MEDEUS inherits applicable safety/verification gates but cannot promote ASTRADELIA capabilities, modify the 8 + NOW core, or bypass evidence requirements.
