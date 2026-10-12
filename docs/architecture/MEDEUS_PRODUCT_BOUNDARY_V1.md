# MEDEUS — PRODUCT / ASTRADELIA BOUNDARY v1
**Date:** 2026-10-12 · **Status:** INTEGRATION_SPEC_ONLY / NOT_CONNECTED

## Distinct systems
- **MEDEUS**: presentation scene, user speech/text capture, inferred language/locale, anonymous paid-access orchestration, visible results, privacy and consumer disclosures.
- **ASTRADELIA**: *separate* source-of-evidence/forecast engine when its declared domain and validation gates permit. Never change its existing `8 outer functional nodes + NOW/S_t center` topology; EVERION is Layer 0/state-space dynamics, not a MEDEUS UI component.
- MEDEUS may route through authorized **read-only scoped forecast API** (future), not obtain GUARDAR/TURRIS powers or bypass safety/verification.
- **Authority**: ASTRADELIA's current [ROADMAP](https://github.com/MrPenser/genius-ai/blob/main/docs/roadmap/ROADMAP.md) and canonical verification artifacts govern the engine. This document **does not** make experimental ASTRADELIA systems production-ready.

## Real answer contract (future)
Every market/real-world forecast needs: `question`, `target`, `scope`, `forecast_horizon`, `as_of_cutoff`, `issued_at`, `probability` when justified, `uncertainty`, `evidence_snapshot_id/hash`, `forecast_system_snapshot_id/hash`, `search_ledger_id/hash`, `trial_family`, `evaluation_window`, `adaptation_policy`, `provenance_refs`, `verification_status`, `limitations`, `locale`. Unknown fields must be marked unknown/not verified, never fabricated.
- Forward-looking accuracy, calibration, leakage, dependence, baselines and outcome readback are separate gates; `BACKTEST_EDGE != FORWARD_EDGE`.
- `BEST_OF_MANY_WITHOUT_SEARCH_LEDGER != VERIFIED_EDGE`; `MODEL_PRICE != VERIFIED_TASK_COST`; `PREDICTION != EXECUTION_AUTHORITY`.
- Material forecast model/feature/router change during a scored evaluation window => a new version/segment, not silent continuation.
- `QUERY_VET = VERIFIED_ECONOMIC_VALUE - VERIFIED_TASK_COST` is an economic test metric, not guaranteed profit or permission to charge.
- When no validated forecast is available: return an honest scope-limited answer or decline prediction. A mystical visual never authorizes certainty/fabricated probability.

## Payments / no accounts
- Optional `~USD 1 per forecast` pricing is a **hypothesis**; verify economics and country/merchant eligibility before taking payments.
- Hosted checkout only, from legitimate third-party provider (e.g. Stripe Checkout or equivalent available to merchant jurisdiction), initiated with a deliberate informed action, **not** by passive touching/voice recognition.
- No own card forms, no account creation. **Anonymous ≠ unauthenticated access to entitlements**: create unguessable short-lived order/session token; verify on server via signed provider webhook and replay protection; never trust redirect success alone.
- Refund, tax, pricing, jurisdiction, age, terms and data processing disclosures must be accessible without conventional navigation chrome where legally possible. Avoid promise of returns or financial advice.
- No card details in MEDEUS logs; speech permissions and transcript retention explicit and minimal. Accessible text-only fallback and safe provider privacy boundary.

## Architecture / release gates
`DEMO_UI` → `VOICE_AND_TEXT_REAL` → `FORECAST_API_SHADOW` → `VERIFIED_FORECASTS_WITH_PROVENANCE` → `HOSTED_PAYMENT_TEST` → `PILOT` → `PUBLIC`; each requires independent acceptance and recorded evidence. No production claims from animation screenshots.
