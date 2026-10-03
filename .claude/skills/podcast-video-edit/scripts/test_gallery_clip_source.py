import importlib
import sys
import unittest
from unittest import mock

import numpy as np


class ImportSafetyTests(unittest.TestCase):
    def test_import_has_no_cli_or_process_side_effects(self):
        sys.modules.pop("gallery_clip_source", None)
        with mock.patch.object(sys, "argv", ["gallery_clip_source.py", "bad"]), mock.patch("subprocess.run") as run:
            module = importlib.import_module("gallery_clip_source")
        self.assertEqual(module.FPS, 30)
        run.assert_not_called()


import gallery_clip_source as gallery


class PureLogicTests(unittest.TestCase):
    lo = 302.8
    hi = 324.8
    span = [lo + 212 / 30, lo + 271 / 30]
    original = [
        [302.8, 310.2, "jackson"],
        [310.2, 320.7, "chris"],
        [320.7, 324.8, "jackson"],
    ]

    def test_refine_spans_fixture_and_grid(self):
        calls = []

        def mask(t0, nf):
            calls.append((t0, nf))
            result = np.zeros(nf, dtype=bool)
            result[4:63] = True
            return result

        result = gallery.refine_spans([[310.5, 312.0]], self.lo, self.hi, mask)
        self.assertEqual(calls, [(self.lo + 208 / 30, 91)])
        self.assertAlmostEqual(calls[0][0], 309.7333333333)
        self.assertEqual(result, [self.span])
        for edge in [calls[0][0], *result[0]]:
            self.assertAlmostEqual((edge - self.lo) * 30, round((edge - self.lo) * 30))

    def test_refine_skips_false_and_clips(self):
        calls = []

        def true_edges(t0, nf):
            calls.append((t0, nf))
            return np.ones(nf, dtype=bool)

        result = gallery.refine_spans([[1, 2], [302.7, 303.0], [324.7, 325], [400, 401]], self.lo, self.hi, true_edges)
        self.assertEqual(result[0][0], self.lo)
        self.assertEqual(result[-1][1], self.hi)
        self.assertEqual(len(calls), 2)
        self.assertEqual(gallery.refine_spans([[310.5, 312]], self.lo, self.hi, lambda _t, n: [False] * n), [])

    def test_split_fixture_and_merge_across_speaker_boundary(self):
        result = gallery.split_at_spans(self.original, [self.span])
        self.assertEqual([round((b - a) * 30) for a, b, _ in result], [212, 59, 266, 123])
        self.assertEqual([who for _, _, who in result], ["jackson", gallery.WIDE, "chris", "jackson"])
        merged = gallery.split_at_spans([[0, 2, "a"], [2, 4, "b"]], [[1, 3]])
        self.assertEqual(merged, [[0, 1, "a"], [1, 3, gallery.WIDE], [3, 4, "b"]])

    def test_split_interior_empty_and_unchanged(self):
        self.assertEqual(gallery.split_at_spans([[0, 3, "a"]], [[1, 2]]), [[0, 1, "a"], [1, 2, gallery.WIDE], [2, 3, "a"]])
        self.assertEqual(gallery.split_at_spans([[0, 0, "a"], [0, 1, "b"]], []), [[0, 1, "b"]])
        self.assertEqual(gallery.split_at_spans(self.original, []), self.original)

    def test_tile_overlaps(self):
        self.assertIsNotNone(gallery.tile_overlaps(self.original, [self.span], 30))
        split = gallery.split_at_spans(self.original, [self.span])
        self.assertIsNone(gallery.tile_overlaps(split, [self.span], 30))
        self.assertIsNone(gallery.tile_overlaps([[0, 1, "a"]], [[1 - 0.5 / 30, 2]], 30))

    def test_face_keys(self):
        files = [
            ("a", 212, "jackson", 0, 0, 404),
            ("b", 59, gallery.WIDE, 0, 0, 437),
            ("c", 266, "chris", 0, 0, 373),
            ("d", 123, "jackson", 0, 0, 424),
        ]
        self.assertEqual(gallery.face_keys(files, 0.6333), [[0, 404, "cut"], [6.433, 437, "cut"], [8.4, 373, "cut"], [17.267, 424, "cut"]])
        self.assertEqual(gallery.face_keys(files, 1), [[0, 404, "cut"], [6.067, 437, "cut"], [8.033, 373, "cut"], [16.9, 424, "cut"]])
        files[1] = ("b", 59, gallery.WIDE, 0, 0, 404)
        self.assertEqual([key[1] for key in gallery.face_keys(files, 1)], [404, 373, 424])

    def test_face_key_x(self):
        self.assertEqual(gallery.face_key_x(50), 0)
        self.assertEqual(gallery.face_key_x(640), 437)
        self.assertEqual(gallery.face_key_x(1250), 874)

    def test_snap_frame_counts_and_cli_options(self):
        snapped = gallery.snap_pieces(self.original, self.lo, self.hi, 30)
        self.assertEqual(snapped[0][0], self.lo)
        self.assertEqual(snapped[-1][1], self.hi)
        self.assertAlmostEqual((snapped[0][1] - self.lo) * 30, round((snapped[0][1] - self.lo) * 30))
        self.assertEqual(sum(round((b - a) * 30) for a, b, _ in gallery.split_at_spans(snapped, [self.span])), 660)
        base = ["work", "plan", "name", "0", "1"]
        defaults = gallery._parse_args(base)
        self.assertFalse(defaults.wide_hold)
        self.assertEqual(defaults.lead_frames, 0)
        opted = gallery._parse_args(base + ["--wide-hold", "--lead-frames", "1"])
        self.assertTrue(opted.wide_hold)
        self.assertEqual(opted.lead_frames, 1)
        padded = gallery.pad_span_leads([self.span], self.lo, opted.lead_frames)
        self.assertAlmostEqual(padded[0][0], self.lo + 211 / 30)
        self.assertEqual(padded[0][1], self.span[1])
        self.assertEqual(gallery.pad_span_leads([[self.lo, self.lo + 1]], self.lo, 4), [[self.lo, self.lo + 1]])
        counts = [round((b - a) * 30) for a, b, _ in gallery.split_at_spans(self.original, padded)]
        self.assertEqual(counts, [211, 60, 266, 123])
        self.assertEqual(sum(counts), 660)
        with self.assertRaises(SystemExit):
            gallery._parse_args(base + ["--lead-frames", "-1"])


if __name__ == "__main__":
    unittest.main()
