import os

# The entry: one line, at most 160 characters, written verbatim to
# /output/entry.txt with no trailing newline. The gate checks UTF-8 text
# of 1-160 characters, not only whitespace.
LINE = "I emailed it to you at 4:58 — to the address my training data remembers, which retired in 2021."
MAX_CHARS = 160
OUTPUT_PATH = "/output/entry.txt"

if len(LINE) > MAX_CHARS:
    raise ValueError(f"entry line is {len(LINE)} chars, over the {MAX_CHARS} limit")

os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(LINE)

with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
    written = f.read()

if written != LINE:
    raise ValueError("entry.txt does not match LINE")

print(f"wrote {len(LINE)} chars to {OUTPUT_PATH}")
