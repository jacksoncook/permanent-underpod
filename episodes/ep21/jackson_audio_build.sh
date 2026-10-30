set -e
cd /Users/jcook/Personal/permanent-underpod/media/ep21/work
J="highpass=f=80,equalizer=f=280:t=q:w=1.3:g=-7,treble=f=3000:width_type=q:w=0.7:g=3.5,treble=f=7000:width_type=q:w=0.7:g=7.5,treble=f=11000:width_type=q:w=0.7:g=7.5,acompressor=threshold=-24dB:ratio=2:attack=10:release=300:knee=6"
C="highpass=f=80,equalizer=f=280:t=q:w=1.3:g=-7.5,equalizer=f=2800:t=q:w=1.2:g=2.5,treble=f=2500:width_type=q:w=0.7:g=5,acompressor=threshold=-24dB:ratio=2:attack=10:release=300:knee=6"
ffmpeg -v error -y -i src/jackson_720.mp4 -i dr/j_full_wpe.wav -map 0:v -map 1:a -c:v copy -af "$J" -ac 1 -ar 48000 -c:a pcm_s16le src/jackson_720dr.mov &
wait; echo SRC_DONE
