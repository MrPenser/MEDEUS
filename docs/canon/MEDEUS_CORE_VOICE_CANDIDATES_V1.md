# MEDEUS Core Voice — Audition Candidates V1
**Date:** 2026-10-12 · **Status:** SHORTLIST_PREPARED / RUSSIAN_TTS_JOBS_SUBMITTED / USER_VOICE_APPROVAL_REQUIRED / SITE_VOICE_NOT_CONNECTED

## User instruction
Find an appropriate, rich and deep androgynous/dual-timbre single voice for the MEDEUS core, but **present candidates for approval before website integration**. Required first utterance for every visitor: localized natural translation of «Добро пожаловать!». No change to ten-state orb animation, master image or provisional ASCENT V2 sound.

## Real candidate voices returned by provider-connected vidIQ catalogue
All candidate IDs below correspond to ElevenLabs premade voices surfaced by the provider, not an invented voice design:
- **River** — voiceId `SAz9YHcvj6GT2YYXdXww`; description “Relaxed, Neutral, Informative”; neutral timbral baseline, primary audition candidate. Provider demo `https://storage.googleapis.com/eleven-public-prod/premade/voices/SAz9YHcvj6GT2YYXdXww/e6c95f0b-2227-491a-b3d7-2249240decb7.mp3`.
- **Matilda** — voiceId `XrExE9yKIg1WjnnlVkGX`; professional, alto-pitched female; alternate for lower/human mid-range while preserving airiness. Provider demo `https://storage.googleapis.com/eleven-public-prod/premade/voices/XrExE9yKIg1WjnnlVkGX/b930e18d-6b4d-466e-bab2-0ae97c6d8535.mp3`.
- **Eric** — voiceId `cjVigY5qzO86Huf0OWal`; smooth tenor, conversational, lower register alternative. Provider demo `https://storage.googleapis.com/eleven-public-prod/premade/voices/cjVigY5qzO86Huf0OWal/d098fda0-6456-4030-b3d8-63aa048c9070.mp3`.

These are **provider sample clips, not evidence that any candidate has the full androgynous identity, multilingual accent parity, commercial rights or technical viability**. Required validation: same spoken script and matched loudness across candidate voices, RU/EN/TR, smartphone speaker/headphones, qualitative impression and commercial license/cost checks.

## Sample synthesis requests
Three provider-connected vidIQ voiceover generation jobs were submitted with identical script `Добро пожаловать!` (Russian) on 2026-10-12:
- River `job_d82cb641-50fd-44d8-bdc0-506647a9777f`
- Matilda `job_82cfb7fb-5d7a-4d25-bac0-91dc22cc70fa`
- Eric `job_9344bfb9-ede8-492f-9405-5b262567a6a1`
Latest status seen before documenting: **inprogress**, do not treat them as generated assets without polling completion and confirming hosted MP3 URL.

## Production gates
1. User must listen to actual resulting greeting samples and choose/reject.
2. Chosen candidate requires commercial usage license verification, provider availability, data/privacy review, and actual RU/EN/TR output tests.
3. Implement TTS or licensed pre-rendered greetings **only after user approval**. Browser audio policy requires first user gesture; mute/skip and once-per-session handling.
4. Existing `MEDEUS_ASCENT_V2` instrumental greeting is provisional, not a replacement for this voice.

`VOICE_CANDIDATES_IDENTIFIED=true`; `USER_VOICE_SELECTION=PENDING`; `TTS_WEBSITE_DEPLOYMENT=NOT_AUTHORIZED`; `SAMPLE_GENERATION_STATUS=IN_PROGRESS_AT_LAST_POLL`.

## River selected as provisional timbral foundation — 2026-10-12
- Latest explicit user decision: **“Для MEDEUS наиболее близок голос River. Используй его как основу для дальнейших проб. Финального утверждения и разрешения на подключение к сайту пока нет.”**
- **Selection is directional, NOT a final voice approval**. Preferred source identity `ElevenLabs River`, exact provider voice ID `SAz9YHcvj6GT2YYXdXww`. Do not treat provider's plain voice as automatically satisfying MEDEUS's unique single-voice, androgynous, deep and luminous design.
- Prepare matched audition for first spoken welcome in RU `Добро пожаловать!`, EN `Welcome!`, TR `Hoş geldiniz!`; evaluate phonetic naturalness, pronunciation, low-mid body, top-end shimmer, pace, consonant clarity and *consistent identifiable voice across locales*.
- Provider sample synthesis jobs: RU `job_d82cb641-50fd-44d8-bdc0-506647a9777f`, EN `job_8be22026-5f56-4d2a-9c0b-bf76c4bb6bc7`, TR `job_6a35e8c0-49c4-4c86-9c55-67ada412ab39`. At last check RU was still `inprogress`; EN and TR newly submitted. A job ID is NOT an audio file; record real MP3 URLs only once jobs complete.
- Refine *subtly*: controlled formants/spectral envelope to increase depth without low-end mud, soft upper resonance, stable pitch and breath/consonants; no dual-speaker overlays, no heavy chorus, no full-track pitch shift that makes language unintelligible. All variants loudness-matched and checked on mobile and headphones.
- No GitHub website repository code, deploy, startup voice or autoplay change authorized by this provisional choice. Listening first, explicit final approval second, integration only after further distinct permission.
- `VOICE_BASE=RIVER_PROVISIONAL`; `MULTILINGUAL_VOICE_SAMPLES=PENDING`; `VOICE_TIMBRE_FINAL_APPROVAL=false`; `WEBSITE_VOICE_CONNECT_AUTHORIZED=false`; `SITE_AUDIO_UNCHANGED=true`.
