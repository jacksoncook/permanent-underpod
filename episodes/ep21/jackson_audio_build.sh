set -e
cd /Users/jcook/Personal/permanent-underpod/media/ep21/work
J="agate=threshold=0.004:ratio=3:range=0.15:attack=3:release=300:knee=4,highpass=f=80,equalizer=f=280:t=q:w=1.3:g=-7,treble=f=3000:width_type=q:w=0.7:g=3.5,treble=f=7000:width_type=q:w=0.7:g=7.5,treble=f=11000:width_type=q:w=0.7:g=7.5,acompressor=threshold=-24dB:ratio=2:attack=10:release=300:knee=6,firequalizer=gain_entry='entry(80,6); entry(100,7); entry(126,8); entry(160,8); entry(201,8); entry(253,8); entry(320,5); entry(403,1); entry(507,1); entry(640,1); entry(806,1); entry(1015,0); entry(2000,0); entry(16000,0)':delay=0.01:accuracy=1:fixed=on"
C="highpass=f=80,equalizer=f=280:t=q:w=1.3:g=-7.5,equalizer=f=2800:t=q:w=1.2:g=2.5,treble=f=2500:width_type=q:w=0.7:g=5,acompressor=threshold=-24dB:ratio=2:attack=10:release=300:knee=6"
ffmpeg -v error -y -i src/jackson_720.mp4 -i dr/j_full_wpe.wav -map 0:v -map 1:a -c:v copy -af "$J" -ac 1 -ar 48000 -c:a pcm_s16le src/jackson_720dr.mov &
wait; echo SRC_DONE
