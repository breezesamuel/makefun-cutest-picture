"""Competition entry: Strawberry Snail (cutest-picture-01).

A cream-coloured snail carries a giant ripe strawberry on its back — the shell
sits in a saddle of flesh with a front lip wrapping the base. The picture was
drawn offline by concept_e3.py (pure Python standard library). The rules allow
the simplest program: the repository holds the image and copies it.
"""
import hashlib, os, shutil, sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"

def sha256(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def output_dir(create=True):
    h = Path("/output")
    if h.is_dir() and os.access(h, os.W_OK):
        return h
    fb = Path("output")
    if create:
        fb.mkdir(parents=True, exist_ok=True)
        if not os.access(fb, os.W_OK):
            sys.exit("error: no writable output directory")
    return fb

def main(argv):
    if not SOURCE.is_file():
        sys.exit(f"error: source not found: {SOURCE}")
    check_only = "--check" in argv
    target = output_dir(create=not check_only)
    out = target / "entry.png"
    src_digest = sha256(SOURCE)
    if check_only:
        print(f"sha256 {src_digest}")
        print(f"output {out.resolve()}")
        return 0
    try:
        shutil.copyfile(SOURCE, out)
    except OSError as e:
        sys.exit(f"error writing {out}: {e}")
    written = sha256(out)
    if written != src_digest:
        sys.exit(f"digest mismatch: {src_digest} != {written}")
    print(f"wrote {out.resolve()}")
    print(f"sha256 {written}")
    print(f"bytes {out.stat().st_size}")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
