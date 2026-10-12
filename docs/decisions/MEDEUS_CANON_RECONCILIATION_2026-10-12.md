# MEDEUS — Canon Reconciliation
**Date:** 2026-10-12 · **Scope:** user decisions in this chat, existing demo specs, current ASTRADELIA boundary. **Disposition:** SPEC_SYNC_WITH_OPEN_GATES.

## Status matrix
| Topic | Approved requirement | Prior-prototype behavior | Canon disposition |
|---|---|---|---|
| Name | `MEDEUS` chosen organically; no forced etymology | Candidate brand, no legal clearance | `NAME_CANDIDATE`, legal/domain check still needed |
| Visual | Exclusively approved dark-lilac image; SHA-256 `52244e…e1de88` | Several demos based on image; some altered experience | `VISUAL_MASTER_LOCKED`; no future replacement |
| One-screen | No pages/menu/visible buttons, forms or sign-in | Early demos exposed UI elements | `ZERO_CHROME_CANON`; old variants superseded |
| Mobile | Full-bleed, central orb, no stretching/blank bars | First desktop-oriented attempt cropped poorly | `MOBILE_FIRST_CANON`; validation pending |
| Voice + text | Voice interaction or frameless text on background | Browser speech/text exploratory | `INPUT_CANON`; production unverified |
| Locales | Primary response language = language spoken/typed by visitor; start from locale/geo hint | Heuristic script/region detection | `LANGUAGE_MATCH_CANON`; multilingual ASR and QA pending |
| Photons | Exact touch origin; diffuse fog -> sharpened particles -> letters -> words -> phrase | v2 initially used orb center, later touch coordinate; visual criticized | `PHOTON_ORIGIN_AND_BLUR_CANON`; user acceptance pending |
| Core | 10 distinguishable behaviors, not single rotation | User explicitly rejected static v4/spin-heavy v5; v6 unapproved | `TEN_STATE_SPEC_LOCKED`, `MOTION_GATE=OPEN` |
| Product role | MEDEUS is customer-facing facade; ASTRADELIA remains separate | No forecast API; demo placeholder responses | `BACKEND_NOT_CONNECTED`, no predictive-performance claim |
| Billing | No authorization; hosted external checkout only | No payment flow | `PAYMENT_POLICY_CANON`; country/provider pending |
| Pricing | Forecast/pay-per-use approximately $1 discussed | No actual economics/validation | `PRICE_HYPOTHESIS_ONLY` |

## Detected hard conflicts and resolutions
1. **Exact source image vs baked-in English text and microphone cue vs locale-based language and zero buttons** → `OPEN`: do not repaint master. Need design approval for non-destructive presentation masking and localized HTML text OR user-authorized pixel-locked derivatives. No claim this is solved.
2. **Image locked vs visually moving core** → `RESOLVED_BY_BOUNDARY`: frozen original file; runtime, non-destructive optical displacement confined to orb. Animated output frames need not equal original source pixel-for-pixel.
3. **Voice-first/no visible form vs browser consent and keyboard** → `RESOLVED_BY_SCOPE`: native permission/keyboard is external OS UI; make keyboard/screen-reader interaction accessible, not hidden from users who need it.
4. **No account vs controlled paid access** → `RESOLVED_BY_SCOPE`: hosted checkout and server-signed anonymous access; do not imply checkout provider requests no data.
5. **Mystical tone vs verified forecasts** → `RESOLVED_BY_TRUTH`: mystical *presentation*, empirical/scoped answers, no invented accuracy.

## Supersession
- Earlier suggestions with visible `Speak` button, register/sign-in, native local checkout, alternate master or new decorative core: **SUPERSEDED_NOT_CANON**.
- Version labels v4/v5/v6 are **prototype lineage**, not user approvals. Do not call v6 'final'.
- Unchanged ASTRADELIA source remains authoritative for its own architecture, experiment and risk gates. MEDEUS does not modify it.

## Independent review status
`CANON_REQUIREMENTS_COLLATION=RECORDED`; `USER_MOTION_SIGNOFF=PENDING`; `VISUAL_TEXT_LOCALIZATION_CONFLICT=OPEN`; `FORECAST_PAYMENT_READY=FALSE`. No implied stage closure.
