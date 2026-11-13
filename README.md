# Strawberry Snail

Entry for make.fun **cutest-picture-01**.

A cream-coloured snail carries a giant ripe strawberry on its back — the shell
sits in a saddle of flesh with a front lip wrapping the base, so it reads as
carried rather than pasted on. The picture was drawn offline by
`../concept_e3.py` (pure Python standard library).

## Layout

- `entry.png` — the artwork, 768x768, well under 1 MiB
- `main.py` — writes the image to `/output/entry.png` (falls back to `./output`
  when `/output` does not exist)

## Run

```sh
python main.py            # writes /output/entry.png
python main.py --check    # prints the sha256 of the bytes it would write
```

The program is deterministic: it copies fixed bytes, so two runs write the same
file.
