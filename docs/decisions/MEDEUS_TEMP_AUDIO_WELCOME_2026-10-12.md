# MEDEUS — Temporary Greeting and Provisional Voice Integration (2026-10-12)

**User authorization:** «ладно подключи его но это временно . и заодно звуковое приветствие».

## Implemented scope — GitHub website source
- Code authority: `MrPenser/medeus-master-asset`.
- `src/lib/medeus/temporary-greeting.ts`, commit `4fae2800c10afb69d5060ba25f42cc893f20443b`:
  - On the first browser-permitted *user gesture*, play the existing provisional ASCENT V2 instrumental `/audio/medeus_ascent_deep_v2.wav` at gentle volume 0.15.
  - Say «Добро пожаловать!» or natural supported translation using the **browser's native** Web Speech TTS, at reduced speed (rate 0.82) and pitch 0.95 (a normalized *relative* control, **not** a literal 9-Hz shift).
  - Explicit translation dictionary for 37+ language/locale bases; some locales have no installed TTS, and unsupported locales fall back to English. **Universal TTS for every language is NOT implemented**. Never claim language coverage or timbral parity outside validation.
  - Music/TTS never autoplay on page load; they are reserved for a user gesture. SessionStorage attempts to deduplicate welcome after actual speech starts. Audio can be suppressed by browser permissions/voice availability; user-visible mobile-browser PASS is not established.
  - During user microphone recognition the welcome is deferred until recognition is finished/unavailable, avoiding self-capture and feedback.
- `src/components/medeus/MedeusStage.tsx` commit `ece2a8e3ddb31eb45b978b1c990620751ef09260`: wires temporary audio to source-verified single-scene core's contact/voice/text states, and adds original **River C3 sound sample** as a listen-only element to already-existing `?soundDemo=1` diagnostic panel. DOES NOT add conventional UI to normal site or modify the master asset / shader / ten core states.

## Crucial production truth
**River C3 is a short, pre-recorded English timbre audition, NOT a general-purpose Russian/Turkish/multilingual TTS engine.** A generic browser voice can be slowed and lowered in pitch but does NOT become ElevenLabs River; **the actual spoken greeting implemented now uses native browser speech**. The River C3 MP3 is connected only as an optional reference preview, not as the runtime speech engine. No misleading River identity claim is permitted. Real River production TTS requires a supported and licensed API and authenticated server proxy; do not embed API secrets in browser.

The provider did produce a true English River “Welcome!” via vidIQ job `job_8be22026-5f56-4d2a-9c0b-bf76c4bb6bc7`, but it is delivered as a signed/expiring URL, **not a stable site asset**. Russian and Turkish attempts remained pending or failed; no approved multilingual River media was deployed. Lovable agent edits cannot currently be requested: workspace reports out of credits, but GitHub source commits do not require Lovable editing credits.

## Preliminary gates
- `PROVISIONAL_ASCENT_V2_SITE_GREETING_SOURCE_CONNECTED=true` (existing 7.4-second WAV).
- `TEMP_NATIVE_TTS_GREETING_CODE_CONNECTED=true`, `BROWSER_SPEECH_AUDIO_QA=PENDING`.
- `RIVER_C3_AUDITION_PREVIEW_CONNECTED=true`, `RIVER_RUNTIME_MULTILINGUAL_TTS_CONNECTED=false`.
- `WEBSITE_SOURCE_COMMITTED=true`; `LOVABLE_READBACK=PENDING_OR_TO_BE_VERIFIED`.
- `FINAL_SOUND_APPROVAL=false`; `FINAL_VOICE_APPROVAL=false`; `EXPLICIT_USER_PERMISSION=TEMPORARY_ONLY`.
- `BACKEND_ASTRADELIA_CONNECTED=false`. All existing visual locks and user-confirmed mobile soft-keyboard behavior must remain stable.

## Remaining work
1. Obtain user-observed phone and desktop first-interaction audio check (including mic+keyboard) and confirm volume/cue overlap.
2. Obtain properly licensed / provider-routed River TTS for RU/EN/TR first, then open-ended locale support; record authorized voice IDs, API cost and latency.
3. Verify same first-phrase precedence, one-per-session semantics, microphone no-feedback, tab visibility and mute/volume preferences.
4. Let user approve or reject current temporary version independently from final voice/sound design.
