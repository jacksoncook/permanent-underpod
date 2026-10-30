# Ep 21 — Jackson bathroom-mic treatment bench

Two passages, same episode chain on every file (highpass, afftdn, de-ess, comp, air, loudnorm −16), so only the
source treatment differs. Loudness matched. Play A_* back to back, then B_*.

- **A** = master 2132–2160, "I do think we should do our due diligence… 138 pieces of work" (plain talk, numbers)
- **B** = master 1801–1826, "Good on them for finding their own path… let's hope things turn around" (soft tails, laugh)

| # | File | Treatment |
|---|---|---|
| 1 | `*_1_raw` | nothing (StreamYard as recorded) |
| 2 | `*_2_wpe_only` | WPE dereverb only |
| 3 | `*_3_wpe_eq_v3` | v3: WPE → highpass → 280 Hz −7 → +3.5 @3k, +7.5 @7k, +7.5 @11k → gentle comp |
| 4 | `*_4_wpe_eq_gate_v2` | v3 + the expander that shipped in v2 (chops word tails; here for reference) |
| 5 | `*_5_wpe_lighteq` | WPE → half-strength EQ (280 −4, +2 @3k, +4 @7k/11k) → comp |
| 6 | `*_6_eq_no_wpe` | the v3 EQ with no dereverb |
| 7 | `*_7_wpe_eq_denoise` | v3 + heavier afftdn (nr 24) before the EQ |
| 8 | `*_8_wpe_eq_softgate_v4` | **what v4 ships**: 4's chain with the gate opened up (threshold −48 dB, range −16 dB, release 300 ms): same clean silence between words, 0 of 1,965 word tails attenuated (4 chopped 14%) |

Tell me the number; I rebuild `src/jackson_720dr.mov` with it and re-render (~25 min).
Rebuild the bench: `bash build.sh`.
