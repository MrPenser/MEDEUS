# MEDEUS — Greeting Sound Design v1
**Date:** 2026-10-12 · **Status:** AUDIO_FILES_RENDERED / USER_SOUND_SIGNOFF_PENDING / WEBSITE_BINARY_ASSET_NOT_IMPORTED

## Source authority
User supplied `20261012_171725.amr`, AMR-NB 8 kHz, mono, approximately 10.16 s decoded duration. This is an explicitly requested sound-design source for a website greeting. The final cue uses gently processed original material and synthetic resynthesis of its tonal outline; it is not a claim to reconstruct missing AMR high frequencies.

## Tonal, timbral and pacing design
- Main acoustic resonances in the source roughly outline `B♭–D–F`. Proposed tempered tonal center **B♭ major**, A=440 Hz; pitch-note architecture is reconstructed rather than blindly global-pitch-shifted.
- Sound identity: ethereal / celestial; soft glass bell/chimes, diffused warm choir-like pad (instrumental, not synthesized speech), delicate stereo reverberation and natural gentle fades. No drum beat or intrusive click.
- Source cleaning: stationary broadband noise reduction, narrowband cleanup and moderated transients, original-pitched source blended under additive tones, synthesized harmonics to provide high-end presence lost in AMR telephone-band recording.
- Cue A **SHORT**: `MEDEUS_GREETING_SHORT_4s`, approximately 4.5 s. Primary website greeting.
- Cue B **EXTENDED**: `MEDEUS_GREETING_MASTER_7s`, approximately 7.4 s. Optional opening sequence or user-approved ambient intro (do not play simultaneously with Cue A).
- Both created at 48 kHz, 24-bit stereo PCM mastering, MP3 128 kb/s fallback and WebM/Opus 64 kb/s browser variant. Measured integrated loudness approx `−16.9 LUFS` (short), `−16.5 LUFS` (extended), with gentle attenuation already applied. This is a short one-shot cue, NOT a continuously looping background track.
- The site ideally plays the short cue exactly **once** after the first user touch/click on the orb or mic. Standard mobile autoplay policies frequently block audio before a user gesture; do not silently keep retrying or automatically start on page load.
- When delivered on site: maintain correct source identity, moderate default playback volume, respect OS mute/accessibility and page visibility, no restarts on every question or state transition. Leave existing ten orb states and visual master unchanged.

## Generated media custody (conversation export — NOT IN WEBSITE REPO YET)
- Short Opus WebM SHA256: `ab50052ba88a18a757d443d16f4b9808d0b2f26ad3fe09635e1958e397964bec`; ~44 KB.
- Short MP3 SHA256: `3720912c28efc3252088836b6d41d9df04e0ee99e07e7c15953584f93671b624`; ~73 KB.
- Extended Opus WebM SHA256: `b89ab93cea916dce9b162aa877fff5239dc07adef91fb0fedbd8c5206d5c6801`; ~70 KB.
- Conversation artifact: `MEDEUS_GREETING_SOUND_PACK_V1.zip`, includes both variants in MP3/WebM/WAV plus readme.
- **Do not claim binary GitHub/site asset uploaded from conversation sandbox.** The site must have audio files in `public/audio/` or another authenticated/static hosting location for playback. There is no working site greeting until that happens and client audio playback is implemented and tested.

## Acceptance gates
1. User listens to the short and extended MP3 previews, approves harmonic/motif identity and desired loudness.
2. Upload approved Opus + MP3 files to actual Lovable-synced website source or static media storage with independent checksum readback.
3. Implement one-time, first-user-gesture playback with format fallback, graceful `NotAllowedError` handling, no autoplay claim.
4. QA real Android Chrome, iOS Safari, desktop Chrome/Safari, silent mode, slow network and navigation reloads, voice/keyboard coexistence.
5. **Do not** introduce new menu/button/sign-in or alter original visual master, ten-state rendering/shader, photon origination behavior.
`AUDIO_SOURCE_PROCESSED=true`; `AUDIO_USER_SIGNOFF=PENDING`; `WEBSITE_SOUND_ENABLED=false`.
