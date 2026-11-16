# ai-excited-01 entry (Python 3.13, standard library only).
# The image is the entry.png beside this file; the program copies it to
# /output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png outside the grader).
# The copy is byte for byte, so both runs write identical bytes.

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUT_DIR.mkdir(parents=True, exist_ok=True)

shutil.copyfile(HERE / "entry.png", OUT_DIR / "entry.png")

# The copy must be byte for byte, so both runs write identical bytes.
assert (OUT_DIR / "entry.png").stat().st_size == (HERE / "entry.png").stat().st_size
