# Strawberry Snail

Entry for make.fun **cutest-picture-01**.

A cream-coloured snail carries a giant ripe strawberry on its back — the shell
is set in a saddle of flesh with a front lip wrapping the base, so it reads as
carried rather than pasted on. Drawn offline by `../concept_e3.py` (pure Python
stdlib). The rules allow the simplest program: the repo holds the image and
the program copies it.

## Layout

- `entry.png` — 768x768 PNG, well under 1 MiB
- `main.py` — writes `/output/entry.png` (falls back to `./output`)

## Run

```sh
python main.py
python main.py --check
```

Deterministic: two runs produce identical bytes.
