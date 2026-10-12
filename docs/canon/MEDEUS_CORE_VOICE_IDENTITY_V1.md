# MEDEUS — Core Voice Identity v1
**Date:** 2026-10-12
**Authority:** latest direct user instruction: «голос ядра д.б. гермафродитным»
**Status:** CANON_DESIGN_REQUIREMENT / NO_SYNTHESIZED_VOICE_APPROVED / NOT_CONNECTED_TO_SITE

## Definition
The speaking **voice of the MEDEUS core** must be **androgynous, dual-natured** — combining both traditionally masculine and feminine timbral qualities in **one coherent person-like voice**, without presenting as clearly male or clearly female. The user's term «гермафродитным» here describes the creative auditory effect, not an assertion of biological sex or a need to impersonate a real person.

The voice should feel as if it belongs to the living core itself: **deep but luminous, intimate but non-humanly neutral**, controlled, calm, mature, sophisticated. It is a unique MEDEUS sonic identity, not a generic assistant voice, an alien horror effect, a synthetic choir or an exaggerated whisper.

## Acoustic/production targets — design starting point, not approved technical constants
- **One audible identity:** do not simply hard-pan a male and a female TTS recording or blend two full voices with obvious double articulation/comb filtering. Any dual layering must converge into **one intelligible lead** with consistent formants and coherent breath/consonants.
- **Pitch/register:** intermediate speaking tessitura, approximate starting experiment median F0 ≈150–200 Hz when the language/voice supports it; optimize by listening rather than choosing gender by pitch alone. Both low chest warmth and higher light head resonance are present, never growly male bass or extremely high feminine soprano.
- **Spectral character:** low-mid resonant foundation; clear upper formants and delicate airy brightness; modest subharmonic support if needed; avoid muddiness and harsh sibilance. Brightness does not mean pitch-shift distortion.
- **Cadence:** measured, deliberate, unhurried but natural; subtle internal motion, intelligible pauses, good phrase endings, no melodramatic breathiness or robotic monotone.
- **Emotional stance:** poised, mysterious, welcoming, emotionally capable without affectation; the human should perceive one deep intelligence, not two competing speakers.
- **Language parity:** audible identity survives Russian, English and Turkish pronunciation/prosody; multilingual support must be actually tested rather than claimed, with consistent name pronunciation.
- **Mixing:** crystal-clear speech consonants, comfortable perceived loudness across phone and headphones, adequate headroom; optional subtle stereo space/reverb behind mono-compatible center voice, no reverb tail that masks words. Underlying welcome motif must duck beneath speech.
- **Consent/rights:** use a newly synthesized or correctly licensed voice with explicit commercial-speech/voice-clone permissions. Do not replicate any identifiable person's voice without authorization.
- **Interaction boundary:** browser speech recognition of the **user** is a separate input service. This canon specifies the **outgoing audible response** of the core; STT/voice input does not imply TTS is implemented.

## Production/testing workflow
1. Create **at least three 8–15 s candidate voice sketches** with identical neutral wording in Russian, plus comparison phrases in EN/TR where possible:
   - A — darker low-mid anchored, luminous upper overtones;
   - B — nearly balanced male/female formant impression;
   - C — ethereal, brighter yet grounded.
2. A/B/C compare at **matched loudness**, on smartphone speakers + headphones, without music at first; reject unintelligible, gender-stereotyped, chorus-like, vocoder-like or muffled voices.
3. Place winning dry voice above future **ASCENT** welcome sonic cue; duck motif under speech. The current ASCENT V2 greeting is provisional, NOT final.
4. Obtain **user listening signoff**, then add controlled outbound speech synthesis/playback behind explicit consent/browser audio policy, cancellation/interruption and user mute choices.
5. Verify pronunciation, latency/streaming speech with long answers, accessibility, script-localization, and that speech and on-screen response correspond to exactly the same evidence-grounded text.

## Acceptance/status
- `CORE_VOICE_GENDER_IDENTITY=ANDROGYNOUS_DUAL_NATURED_SINGLE_VOICE`: user-directed requirement.
- `CORE_VOICE_FINAL_PRESET=NOT_SELECTED`
- `VOICE_DEMO_RENDERED=FALSE`; `VOICE_USER_LISTENING_SIGNOFF=PENDING`
- `TTS_ENGINE_CONNECTED=FALSE`; `SITE_OUTGOING_SPEECH=NOT_IMPLEMENTED`
- `GREETING_ASCENT_V2=PROVISIONAL_ONLY`; site welcome sound is NOT auto-enabled by this decision.
- `TEN_ORB_STATES_UNCHANGED`; `LOCKED_MASTER_PNG_UNCHANGED`; `ASTRADELIA_BACKEND_NOT_CONNECTED`.

## FIRST SPOKEN PHRASE — globally localized welcome
- **Mandatory first intelligible spoken phrase addressed to a new visitor:** the equivalent of **«Добро пожаловать!»** in that visitor's language. This is not a generic AI assistant self-introduction, nor a question or sales pitch. The welcome has priority before any other synthesized utterance (including a model-generated answer).
- Examples are illustrative only: `ru: «Добро пожаловать!»`, `en: “Welcome!”`, `tr: “Hoş geldiniz!”`. For other languages, use a grammatically and culturally natural verified translation; do not limit product support to these examples.
- Resolve language from an explicit visitor selection or known conversation preference where available; otherwise from browser locale preference (`navigator.languages`, BCP-47). **Do not infer spoken language solely from IP/geolocation.** If TTS for a language is unavailable, transparently fall back to supported speech plus appropriately localized visible text; do not misrepresent a fallback as that user's language.
- The phrase is spoken **with the one coherent androgynous voice of the core**, not with the nonverbal ASCENT motif. Match pronunciation, warmth, depth, deliberate pace and timbre across languages; do not switch male/female speakers by language.
- Browser autoplay rules: greeting may be visually displayed immediately if desired, but speech must begin only after the first allowed user interaction / explicit audio permission. Reserve greeting as the first sentence of speech even if that interaction is the user's initial question; do not block the question from being received.
- **Once per new visit/session**, not before every question or every new page state. Avoid surprising the user with duplicate greetings during an active conversation. Allow mute or skip. Distinguish `GREETING_SPOKEN` (actual audio playback confirmed) from `GREETING_SCHEDULED` (pending gesture) and `GREETING_UNAVAILABLE`.
- `FIRST_SPOKEN_PHRASE_CANON=LOCALIZED_WELCOME`; `ALL_LANGUAGES_IMPLEMENTED=FALSE`; `TTS_GREETING_RUNTIME=NOT_IMPLEMENTED`; `USER_VOICE_PRESET_APPROVAL=PENDING`.

## River selected as provisional timbral foundation — 2026-10-12
- Latest explicit user decision: **“Для MEDEUS наиболее близок голос River. Используй его как основу для дальнейших проб. Финального утверждения и разрешения на подключение к сайту пока нет.”**
- **Selection is directional, NOT a final voice approval**. Preferred source identity `ElevenLabs River`, exact provider voice ID `SAz9YHcvj6GT2YYXdXww`. Do not treat provider's plain voice as automatically satisfying MEDEUS's unique single-voice, androgynous, deep and luminous design.
- Prepare matched audition for first spoken welcome in RU `Добро пожаловать!`, EN `Welcome!`, TR `Hoş geldiniz!`; evaluate phonetic naturalness, pronunciation, low-mid body, top-end shimmer, pace, consonant clarity and *consistent identifiable voice across locales*.
- Provider sample synthesis jobs: RU `job_d82cb641-50fd-44d8-bdc0-506647a9777f`, EN `job_8be22026-5f56-4d2a-9c0b-bf76c4bb6bc7`, TR `job_6a35e8c0-49c4-4c86-9c55-67ada412ab39`. At last check RU was still `inprogress`; EN and TR newly submitted. A job ID is NOT an audio file; record real MP3 URLs only once jobs complete.
- Refine *subtly*: controlled formants/spectral envelope to increase depth without low-end mud, soft upper resonance, stable pitch and breath/consonants; no dual-speaker overlays, no heavy chorus, no full-track pitch shift that makes language unintelligible. All variants loudness-matched and checked on mobile and headphones.
- No GitHub website repository code, deploy, startup voice or autoplay change authorized by this provisional choice. Listening first, explicit final approval second, integration only after further distinct permission.
- `VOICE_BASE=RIVER_PROVISIONAL`; `MULTILINGUAL_VOICE_SAMPLES=PENDING`; `VOICE_TIMBRE_FINAL_APPROVAL=false`; `WEBSITE_VOICE_CONNECT_AUTHORIZED=false`; `SITE_AUDIO_UNCHANGED=true`.
