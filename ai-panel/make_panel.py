#!/usr/bin/env python3
"""Generate a multi-person AI talking-head panel video from face images + audio.

Examples:
  python make_panel.py --config script.json --layout panel --out final.mp4
  python make_panel.py --config script.json --layout active-speaker --out final.mp4
  python make_panel.py --config script.json --backend static --out smoke.mp4   # no-ML smoke test
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from panelkit.backends import BACKENDS, BackendError  # noqa: E402
from panelkit.config import ConfigError  # noqa: E402
from panelkit.media import MediaError  # noqa: E402
from panelkit.pipeline import LAYOUTS, build  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", required=True, type=Path,
                    help="script.json (see README for the schema)")
    ap.add_argument("--layout", choices=LAYOUTS, default="panel",
                    help="panel: everyone on screen, active speaker highlighted; "
                         "active-speaker: hard cut to whoever is talking "
                         "(default: panel)")
    ap.add_argument("--out", required=True, type=Path,
                    help="final output mp4 path")
    ap.add_argument("--backend", choices=sorted(BACKENDS), default="musetalk",
                    help="talking-head model (default: musetalk; 'static' is an "
                         "ffmpeg-only no-lip-sync smoke test)")
    ap.add_argument("--idle-mode", choices=("silence", "loop", "still"),
                    default="silence",
                    help="non-speaking tiles in panel layout: 'silence' "
                         "generates a real not-talking clip per speaker from "
                         "near-silent audio (neutral mouth + natural head "
                         "motion; default), 'loop' boomerangs the speaker's "
                         "talking clip (mouths move while others speak), "
                         "'still' is a subtle breathing zoom on a frozen frame")
    ap.add_argument("--workdir", type=Path, default=Path("outputs"),
                    help="working directory; intermediates go to "
                         "<workdir>/intermediate/ (default: ./outputs)")
    ap.add_argument("--force", action="store_true",
                    help="regenerate talking-head clips even if cached")
    args = ap.parse_args()

    try:
        build(config_path=args.config, layout=args.layout, out_path=args.out,
              workdir=args.workdir, backend_name=args.backend,
              idle_mode=args.idle_mode, force=args.force)
    except (ConfigError, MediaError, BackendError) as e:
        print(f"\nerror: {e}", file=sys.stderr)
        return 2
    except KeyboardInterrupt:
        print("\ninterrupted", file=sys.stderr)
        return 130
    return 0


if __name__ == "__main__":
    sys.exit(main())
