#!/usr/bin/env python3
"""ai-excited-01 entry: write the glass-whale image to the output directory.

The image (entry.png) is the submission itself; this program only places an
exact copy at $MAKEFUN_OUTPUT_DIR/entry.png (or /output/entry.png) and
verifies the copy is byte-for-byte identical to the source.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
TARGET_SHA256 = "4c1abb7719290651a64f6fa7f015e8f72b06becffc9f4e1689141fd75758357b"


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    got = sha256_of(dst)
    assert got == TARGET_SHA256, "entry.png sha256 mismatch: %s" % got
    print("wrote %s (%d bytes, sha256 %s)" % (dst, os.path.getsize(dst), got))
    return 0


if __name__ == "__main__":
    sys.exit(main())
