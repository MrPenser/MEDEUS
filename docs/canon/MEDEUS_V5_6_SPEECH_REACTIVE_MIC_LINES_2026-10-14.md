# MEDEUS V5.6 — Speech-responsive original microphone lines
Date: 2026-10-14
Owner instruction: "ок теперь сделай сама чтобы при произношении или голосовом ответе линии возле микрофона реагировали в такт речи".
Decision: EXTEND current approved V5.5, not a new image. Scope: only the TWO EXISTING thin audio lines on both sides of the mic at (706,830) in verified V4 PNG. Original geometry, mic liquid optical surface, star, FSM, provenance untouched.

## Implemented
Production-source repo `MrPenser/medeus-master-asset`, main HEAD `5fb18bd6af890507af58db195c75ada404c4583b`.
- New `src/lib/medeus/mic-voice-lines.ts` commit `e38f90c9bd3557544384807465368f344067f439`: `createMicVoiceActivity()` obtains a Web Audio MediaStream analyser **only after native speech recognition has started** (permitted microphone gesture). Calculates real input time-domain RMS, applies noise threshold and fast-attack/slow-decay envelope, stops/cleans all microphone tracks and AudioContext on completion, cancellation, new input or unmount. If a separate analyser is denied or unsupported, native SpeechRecognition `onspeechstart/onspeechend` supplies coarse active-voice gating; silence and no-permission result in no motion. The microphone analyser never connects to speakers and does not store/upload audio.
- Output native browser SpeechSynthesis exposes no PCM. `ttsBoundaryLevel` is a clearly labeled **approximation**, driven by onstart/onboundary/onend word timing, with a deliberately subdued "speaking" fallback for engines that omit word-boundary events. Never call this true output amplitude synchronization.
- `paintMicrophoneVoiceLines` uses the existing V4 baked line baseline around `micY + 6*s`, draws fine varying-height strokes over the line strips ONLY left and right of the existing approved microphone (from 1.22 to ~4.48 mic radii), using RMS/boundary envelopes rather than independently animated decorative effects. No new orbit, ring, equalizer HUD or permanently glowing background. In complete silence it draws NOTHING; reduced-motion preference attenuates motion.
- `src/lib/medeus/speech.ts` commit `16efe00287b0eed39be5b6b8d9a4b27212bae656` surfaces real recognition speech-start/end callbacks.
- `src/lib/medeus/response-channel.ts` commit `b3982234c8c33bf7ca9fbe046e5dcb3a3be9b705` adds optional TTS start, word-boundary and finish timing callbacks (and cancellation cleanup) without changing answer routing or speech voice choices.
- `src/lib/medeus/temporary-greeting.ts` commit `c41292007b9ce314c20f359c0bad4b2aeae033dd` similarly animates the once-per-session spoken greeting; it still never plays before user action and defers until speech recognition ends.
- `src/components/medeus/MedeusStage.tsx` commit `3f3280fc094144086d72eeaad5ca06d846ecba2d`: connects real input activity and voice output events to the same mic-line controller; paints on existing fog/overlay canvas using exact responsive mic geometry. Stop/cleanup on aborted listening, reply cancellation, speech end and component unmount. No FSM or separate mic hover/click changes.
- Source V4 bitmap exactly SHA256 `773f67be7fea7fb8b3dd63b88f58dd55d01e82b0724ed3098db317a8d4f8d5b6`. Previous V3 backup remains.

## Evidence
- New `src/lib/medeus/mic-voice-lines.test.ts`, commits `8c8e46df7cf83a74a39350233f2cf324ffaa3a24` / `84b91db165191baa6084d3631134d6832b5b4578`: real RMS threshold/clipping, attack/decay, true silence, separate left/right visual strips not overpainting the mic, output boundary timing and canceled voice cleanup.
- GitHub CI workflow `.github/workflows/medeus-liquid-orb-qa.yml` commit `5fb18bd6af890507af58db195c75ada404c4583b`: includes all new voice files in push triggers and new source custody, cleanup and microphone line-only behavior gates.
- GitHub Actions `38624077560` on exact website HEAD: completed **SUCCESS**, orb/mic GLSL ES100 PASS, production site build PASS, **76/76 unit tests PASS across 11 suites**. https://github.com/MrPenser/medeus-master-asset/actions/runs/38624077560 .
- Lovable project `76dd8168-469d-4edb-88f6-f313be1c1de8` status ready, agentFinished true, latest_commit_sha `5fb18bd6af890507af58db195c75ada404c4583b` exactly matches GitHub. Preview https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/ . `is_published=false`, not a public deployment.

## Acceptance
`SOURCE_QA=PASS`, `GLSL_ES100=PASS`, `BUILD=PASS`, `UNIT_76_76=PASS`, `LOVABLE_SYNC=PASS`.
`USER_VISUAL_SIGNOFF=PENDING`, `REAL_BROWSER_MIC_PERMISSION_AUDIO_QA=PENDING`, `REAL_BROWSER_NATIVE_TTS_BOUNDARY_QA=PENDING`, `STAGE_COMPLETE=FALSE`.
Test steps: speak 2–3 seconds into the mic with permission granted, check waveform strip peaks and settles to baseline when quiet; finish recognition, hear the short spoken demo answer, check left/right strips articulate with TTS words and stop at onend. Also check initial once-per-session greeting and denial/cancellation. Browsers without native speech recognition or TTS may provide no speech and thus no matching line animation. PCM amplitude of native browser TTS is inaccessible, so word timing remains approximate.
