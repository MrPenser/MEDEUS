# MEDEUS — Input/Output Modality Contract & Long Forecast Notice v1
**Date:** 2026-10-12 · **Authority:** direct user instruction
**Status:** POLICY_LOCKED / DEMO_VOICE_ROUTING_CODE_CONNECTED / REAL_LONG_FORECAST_ENGINE_NOT_IMPLEMENTED

## User-approved channel contract
- Question via actual microphone + successful speech recognition -> **short response by audible core speech**, without showing the same short answer as regular reply text (unless native speech is unavailable, where readable text is the accessibility fallback). This is a rule about source channel, not mere browser voice API availability.
- Question typed via keyboard / frameless field -> **answer visually in writing**, no routine spoken answer. The first-session *welcome* is separate and exempt.
- **Long detailed forecast** -> **written response regardless of input channel**. The text must be fully readable, scrollable, sourced and downloadable when a real artifact exists; never truncate it to tiny canvas glyphs.
- When a long forecast follows an actual **voice** question, core must first **say briefly** in user's language that the forecast is detailed and is being provided as written text for careful reading; never read thousands of words aloud. If user asks “why only writing?”/doesn't understand, voice should repeat/explain the same rule on the voice channel. A text asker can see that explanation in text, without unsolicited speech.
- Typed questions do not switch to voice merely because microphone hardware is available; requests entered by microphone do not become text just because speech recognition generated a transcript.
- For accessibility, screen readers, captions and a clearly signaled fallback for audio-blocked browsers are allowed; cannot promise successful TTS until actual browser test.

## Real implementation boundary
- Site source: `src/lib/medeus/response-channel.ts` — `QuestionChannel = voice|text`; `AnswerKind = short|long_forecast`; `answerChannel(...)`; localized `longForecastVoiceNotice(...)`; native speech reply helper.
- Site source: `src/components/medeus/MedeusStage.tsx` — records source modality on submission; renders short demo text ONLY for text questions; for voice question speaks demo answer with browser native speech and falls back to text if unavailable; long forecast switch is defined but **there is not yet a real backend to produce long forecasts**.
- The current assistant response text is still DEMO copy. Native browser voices are **NOT** River C3; River C3 is only a fixed recorded timbre preview. No ASTRADELIA integration connected.
- Original master PNG and ten existing orb motion states remain unchanged. No altered visual or new druid face is approved.

## QA/acceptance
1. Text keyboard -> text reply (and no new non-welcome speech), including Android native IME, Cyrillic and Enter.
2. Microphone -> native speech recognition result -> audible short reply; no double-spoken transcript; cancel speech before next mic capture to prevent feedback.
3. If speech blocked/unsupported, fallback to visible answer; never silently pretend voice was delivered.
4. With a **verified** response typed `kind=long_forecast`, both input modalities display accessible, scrollable text; only voice-origin cases get one brief *spoken* mode-change explanation; user confusion prompts another concise explanation, not long speech.
5. Do not implement “long forecast detection” by treating long wording as proof of a real forecast. Backend must explicitly supply result kind.
6. User tests normal website on desktop and phone; independent readback needed after GitHub/Lovable source sync.

## Later visual exploration — NOT AN APPROVAL OR CHANGE
User suggested a **very large druid face** with eyes closed at entry, opening when a conversation begins. It is an exploratory concept, NOT user authorization to overwrite the SHA-locked sphere master. Proposed comparison: (A) existing sphere, (B) cosmic ageless androgynous face emerging WITHIN sphere at awareness, (C) full-face replacement with new separately approved production master. No changes to original PNG, 10 states, logo or current scene until explicit choice and visual approval.
