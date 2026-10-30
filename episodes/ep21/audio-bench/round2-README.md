# Ep 21 — Jackson bathroom-mic bench, round 2

Same two passages as round 1 (A = master 2132 s, 28 s · B = 1801 s, 25 s), all through the episode
render chain, loudness-matched to about −16.5 LUFS. Number 8 is what shipped in v6.

- **8_current_v6** — WPE dereverb → soft gate → 280 Hz −7, +3.5 at 3 k, +7.5 shelves at 7 k / 11 k → comp.
- **9_v6_plus_body** — 8, plus the low end put back (+6 to +8 dB from 80 to 320 Hz). The laptop mic has
  ~11 dB less body than Jackson's Ep 20 mic below 300 Hz; this restores most of it without touching the mids.
- **10_v6_match_ep20** — 8, plus a full spectral match to Jackson's Ep 20 mic (1/3-octave, capped ±12 dB).

Matching curve derived from the long-term speech spectrum of `work/dr/ep20_raw.wav` vs the v6 chain output
(`work/enh/matcheq_cur.txt`, applied with `firequalizer`).

Round 2b — Resemble Enhance (neural denoise + enhance, `work/enh/`, MPS, nfe 64, lambd 0.9, tau 0.5), then the
render chain only (no bathroom EQ, no gate):

- **11_resemble_raw** — Resemble on the raw laptop track.
- **12_resemble_wpe** — Resemble on the WPE-dereverbed track.

Install notes: current torch (no 2.1.1 pin), `--no-deps resemble-enhance`, stub `deepspeed`, `torchcodec`,
`weights_only=False` on the three `torch.load` calls, `fsolve(...)[0]` in `lcfm/cfm.py`, and the HF model repo
needs `git lfs pull` (the clone ships LFS pointers). ~5 s per 30 s passage.
