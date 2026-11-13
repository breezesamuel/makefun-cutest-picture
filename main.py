"""Competition entry: "Strawberry Snail" (cutest-picture-01).

A cream-coloured snail carries a giant ripe strawberry on its back — the shell
is set in a flesh saddle with a front lip wrapping the base, so it reads as
worn rather than pasted on. The picture was drawn offline by concept_e3.py
(pure Python standard library). The competition rules allow the simplest
program: the repository holds the image and the program copies it.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def output_dir(create=True):
    """Prefer the harness mount /output; otherwise create and use ./output."""
    harness = Path("/output")
    if harness.is_dir() and os.access(harness, os.W_OK):
        return harness
    fallback = Path("output")
    if create:
        fallback.mkdir(parents=True, exist_ok=True)
        if not os.access(fallback, os.W_OK):
            sys.exit(f"error: no writable output directory (/output or {fallback.resolve()})")
    return fallback


def main(argv):
    if not SOURCE.is_file():
        sys.exit(f"error: source image not found: {SOURCE}")

    check_only = "--check" in argv
    target_dir = output_dir(create=not check_only)
    output = target_dir / "entry.png"
    source_digest = sha256(SOURCE)

    if check_only:
        print(f"source {SOURCE}")
        print(f"sha256 {source_digest}")
        print(f"output {output.resolve()}")
        return 0

    try:
        shutil.copyfile(SOURCE, output)
    except OSError as exc:
        sys.exit(f"error: could not write {output.resolve()}: {exc}")

    written_digest = sha256(output)
    if written_digest != source_digest:
        sys.exit(f"error: digest mismatch: source {source_digest} != written {written_digest}")

    print(f"wrote {output.resolve()}")
    print(f"sha256 {written_digest}")
    print(f"bytes {output.stat().st_size}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
