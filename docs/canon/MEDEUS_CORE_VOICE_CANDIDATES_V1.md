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

## 2026-10-12 — Three real-time River timbre auditions delivered
- User specifically requested **three modulated variants** based on provisionally selected River; no final signoff and no permission to connect voice to production website.
- Delivered self-contained conversation artifact `MEDEUS_RIVER_3_TIMBRES_AUDITION.html`, SHA256 `6bc9cfdaa45df11b2b5f9fbd6ae6406160888b1d2f9891827d56c1cc8302978a`, ~11 KB; source includes exact River preview URL `https://storage.googleapis.com/eleven-public-prod/premade/voices/SAz9YHcvj6GT2YYXdXww/e6c95f0b-2227-491a-b3d7-2249240decb7.mp3`.
- Audition applies **three explicit processing profiles in visitor's browser**, not server-created TTS or pre-exported River voice files: `A Deep` (low-shelf/body/slight -4% pitch+pace), `B Dual` (mid/upper balance, no second speaker), `C Ethereal` (bright upper shelf, low resonance, subtle spatial reverb). Each result is loudness-matched, playable and exportable as stereo PCM WAV via browser when original River audio loads.
- Frontend processor tested independently in Chromium with local speech-like WAV substitute: all three were decoded, rendered to browser AudioBuffers and downloaded successfully as WAV. Original remote River fetch / real voice sound **not independently verified in browser**, so fallback is “Download River provider MP3 and choose file” if remote CORS blocks.
- The original provider sample is an **English voice demonstration**, NOT the Russian canonical phrase. RU `Добро пожаловать!` provider job `job_d82cb641-50fd-44d8-bdc0-506647a9777f` expired/refunded; EN/TR jobs unverified and not surfaced as complete.
- Never confuse offline audition tool with site's speech engine: `WEBSITE_VOICE_CONNECTED=false`; `RIVER_TIMBRE_A_B_C_PREVIEW_TOOL=READY`; `RIVER_RU_GREETING_MP3=NOT_GENERATED`; `FINAL_VOICE_USER_SIGNOFF=PENDING`; `SITE_INTEGRATION_PERMISSION=NOT_GRANTED`.

## 2026-10-12 — Broken audition player repaired with real MP3s
- User reported: **«дорожки не запускаются»**. The old `MEDEUS_RIVER_3_TIMBRES_AUDITION.html` initialized three empty audio tags, requiring browser CORS fetch + offline rendering; direct click had nothing to play. This was a product defect, **not a user-side setup error**.
- Source: official public River voice preview `SAz9YHcvj6GT2YYXdXww`. GitHub Actions `MEDEUS River A-B-C auditions` rendered three real MP3 files (not audio-less markup); first workflow run `38280132037` failed because runner lacked FFmpeg; repaired workflow `run_id=38280262903` completed with `conclusion=success`.
- Verified playable artifacts committed to this docs repository only: `research/audio/river-audition-v1/RIVER_A_DEEP.mp3` (3.624s, 73,005 bytes, Git blob `45d471eb92e3e25a92ef75f240c11765369c3d14`), `RIVER_B_DUAL.mp3` (3.528s, 71,085 bytes, Git blob `1c7269a3846433668606f6d2a8c6fabd07451207`), `RIVER_C_ETHEREAL.mp3` (3.768s, 75,885 bytes, Git blob `67daf42c827be56a4d9bec68dcbe7a94e266480f`). All verified by `GitHub.fetch_file` base64 readback and GitHub Action FFprobe.
- Replacement self-contained listening interface `MEDEUS_RIVER_3_TIMBRES_READY.html`, SHA256 `e7fa136e4465b02c8da3bff86fcac39d88c36a0a581104085e04179184babcbc`, has three standard HTML5 `<audio src=https://raw.githubusercontent.com/MrPenser/MEDEUS/main/research/audio/river-audition-v1/…>` players and *independent direct MP3 open links*. No CORS fetch, no JS synthesis, no extra user input.
- `MP3_FILES_BUILT=PASS`; `GITHUB_MEDIA_CUSTODY=PASS`; `STATIC_PLAYER_SOURCE_PATHS=PASS`; `HUMAN_MOBILE_BROWSER_PLAYBACK=NOT_YET_CONFIRMED`; `USER_VOICE_APPROVAL=PENDING`. No website MEDEUS code or automatic greeting playback touched.

## River C lower-soft-slow pitch experiment — 2026-10-12
- User requested: «опусти вариант с на 100 герц ниже и добавь мягкости голосу. и не так быстро»; interpreted as **variant C (Ethereal)**, not A/B. Do not change the user-selected *provisional* River voice base or enable audio on the live MEDEUS website.
- Reprocessed actual River C MP3 using server-side FFmpeg rubberband with **formant preservation**, `tempo=0.79` (~21% slower), gently warmer lows, upper-treble attenuation (~−3.2 dB), mild dynamics and loudness target −19 LUFS.
- Localized source median F0 estimated by autocorrelation on 16 kHz PCM: **175.8 Hz**. Pitch factor `0.43125` targets **75.8 Hz** = nominal **−100.0 Hz**. Extremely large shift for human speech; actual resulting fundamental was **not separately F0-measured**, and intelligibility/listening acceptance remain human gates. Do not claim a commercial-ready voice identity.
- Source: `research/audio/river-audition-v1/RIVER_C_ETHEREAL.mp3`. Result: `research/audio/river-audition-v2/RIVER_C_MINUS_100HZ_SOFT_SLOW.mp3`, Git blob `2969522d49ba2ec61f45db388bf1b4f32eb81dfc`; **4.752 seconds**, **114,669 bytes**, 192 kbps MP3. GitHub readback and Actions run `38281522545` = `success`.
- Direct audition: `https://raw.githubusercontent.com/MrPenser/MEDEUS/main/research/audio/river-audition-v2/RIVER_C_MINUS_100HZ_SOFT_SLOW.mp3`.
- `VARIANT_C_PROCESSING=RENDERED_AND_SOURCE_VERIFIED`; `USER_AUDIO_APPROVAL=PENDING`; `PRODUCTION_VOICE_CONNECTION=NOT_AUTHORIZED`. The existing MEDEUS website/audio is unchanged.
