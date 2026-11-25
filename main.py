"""One-Line Office Jokes — make.fun entry 204.

Pure Python standard library, no dependencies, fully deterministic.
Writes a single one-line office joke to /output/entry.txt.

The joke is built from one concrete office detail — the reply-all
chain nobody can escape — and lands on the sharpest turn: asking to
leave the thread is exactly what makes you its manager.
"""

import os

JOKE = (
    "I replied-all 'please remove me from this thread' and got promoted "
    "to thread manager by 47 strangers who also replied-all."
)


def main() -> None:
    text = JOKE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 199, "entry must be 1-199 characters"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(text)
    print(f"wrote {len(text)} characters to {path}")


if __name__ == "__main__":
    main()
