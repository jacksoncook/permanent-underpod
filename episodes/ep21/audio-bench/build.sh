set -e
cd /Users/jcook/Personal/permanent-underpod/media/ep21/work
OUT=../audio-samples
EQ="equalizer=f=280:t=q:w=1.3:g=-7,treble=f=3000:width_type=q:w=0.7:g=3.5,treble=f=7000:width_type=q:w=0.7:g=7.5,treble=f=11000:width_type=q:w=0.7:g=7.5"
EQL="equalizer=f=280:t=q:w=1.3:g=-4,treble=f=3000:width_type=q:w=0.7:g=2,treble=f=7000:width_type=q:w=0.7:g=4,treble=f=11000:width_type=q:w=0.7:g=4"
COMP="acompressor=threshold=-24dB:ratio=2:attack=10:release=300:knee=6"
GATE="agate=threshold=0.02:ratio=2.5:range=0.15:attack=5:release=100:knee=4"
CHAIN="highpass=f=80,afftdn=nr=14:nf=-50:tn=1,volume=6dB,adynamicequalizer=dfrequency=6800:dqfactor=2.5:tfrequency=6800:tqfactor=2.5:mode=cutabove:threshold=0.01:ratio=4:range=8:attack=2:release=40,acompressor=threshold=-20dB:ratio=3:attack=15:release=250:knee=6,treble=f=9500:width_type=q:w=0.8:g=1.5,loudnorm=I=-16:TP=-1.5:LRA=7"
render() { # name src filter
  name=$1; src=$2; flt=$3
  for span in "A 2132 28" "B 1801 25"; do set -- $span
    ffmpeg -loglevel error -y -ss $2 -t $3 -i "$src" -af "$flt,$CHAIN" -ar 48000 -c:a aac -b:a 192k "$OUT/${1}_${name}.m4a"
  done
}
render 1_raw            dr/j_raw48.wav    "anull"
render 2_wpe_only       dr/j_full_wpe.wav "anull"
render 3_wpe_eq_v3      dr/j_full_wpe.wav "highpass=f=80,$EQ,$COMP"
render 4_wpe_eq_gate_v2 dr/j_full_wpe.wav "$GATE,highpass=f=80,$EQ,$COMP"
render 5_wpe_lighteq    dr/j_full_wpe.wav "highpass=f=80,$EQL,$COMP"
render 6_eq_no_wpe      dr/j_raw48.wav    "highpass=f=80,$EQ,$COMP"
render 7_wpe_eq_denoise dr/j_full_wpe.wav "highpass=f=80,afftdn=nr=24:nf=-45:tn=1,$EQ,$COMP"
echo built
