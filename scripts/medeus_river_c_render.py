"""MEDEUS River C voice audition only. No site code or automated greeting."""
import subprocess
import wave
from pathlib import Path
import numpy as np

source = Path("research/audio/river-audition-v1/RIVER_C_ETHEREAL.mp3")
target = Path("research/audio/river-audition-v2/RIVER_C_MINUS_9HZ_SOFT_SLOW.mp3")
target.parent.mkdir(parents=True, exist_ok=True)

def run(*args):
    subprocess.run(list(args), check=True)

mono = "/tmp/medeus_river_c_16k.wav"
run("ffmpeg","-nostdin","-v","error","-y","-i",str(source),"-ar","16000","-ac","1","-c:a","pcm_s16le",mono)
with wave.open(mono,"rb") as w:
    y = np.frombuffer(w.readframes(w.getnframes()), dtype="<i2").astype(np.float64) / 32768.

# Normalized autocorrelation on voiced 128-ms windows. Reject weak/unstable frames.
f0_values=[]
win=2048
for start in range(0, max(0,len(y)-win),320):
    segment=y[start:start+win]
    rms=float(np.sqrt(np.mean(segment**2)))
    if rms<0.018:
        continue
    segment=(segment-np.mean(segment))*np.hanning(win)
    corr=np.fft.irfft(abs(np.fft.rfft(segment,n=8192))**2,n=8192)[:win]
    lo,hi=40,245  # 65 Hz .. 400 Hz
    norm=corr[lo:hi] / (corr[0]+1e-12)
    p=int(np.argmax(norm))+lo
    if norm[p-lo]>0.57:
        f0_values.append(16000./p)
if len(f0_values)<8:
    raise RuntimeError(f"Not enough voiced samples: {len(f0_values)}")
f0=float(np.median(f0_values))
# Small, natural voice-lowering from the original River C. Preserve vocal identity.
new_f0=max(55.,f0-9.)
ratio=new_f0/f0
print(f"VOICE_C_SOURCE_MEDIAN_F0_HZ={f0:.1f}",flush=True)
print(f"VOICE_C_REQUESTED_DOWN_HZ=9",flush=True)
print(f"VOICE_C_EST_TARGET_MEDIAN_F0_HZ={new_f0:.1f}",flush=True)
print(f"VOICE_C_APPLIED_F0_SHIFT_HZ={f0-new_f0:.1f}",flush=True)
print(f"VOICE_C_PITCH_FACTOR={ratio:.5f}",flush=True)
filter_chain=(
    f"rubberband=pitch={ratio:.6f}:tempo=0.80:formant=preserved:transients=smooth:detector=soft,"
    "highpass=f=54,bass=g=2.5:f=170,"
    "equalizer=f=1150:t=q:w=1.0:g=0.8,"
    "treble=g=-3.2:f=4300,lowpass=f=7700,"
    "acompressor=threshold=0.18:ratio=1.4:attack=20:release=280,"
    "loudnorm=I=-19:TP=-2:LRA=7"
)
run("ffmpeg","-nostdin","-v","error","-y","-i",str(source),
    "-af",filter_chain,"-codec:a","libmp3lame","-b:a","192k",str(target))
run("ffprobe","-v","error","-show_entries","format=duration,size","-of","default=noprint_wrappers=1",str(target))
print(f"RESULT_FILE={target}",flush=True)
