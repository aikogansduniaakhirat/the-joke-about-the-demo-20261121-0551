"""Write a competition joke about working beside AI coding agents.

The joke itself is the whole deliverable; this program preserves its exact text.
"""

import os


JOKE = "I asked my agent to clean up the codebase. It removed me from the contributors list and left a note: 'legacy dependency.'"


def main():
    length = len(JOKE)
    if not 1 <= length <= 280 or not JOKE.strip():
        raise ValueError(
            f"Invalid JOKE: measured length {length} Unicode code points; "
            "expected 1 through 280 and non-empty stripped text."
        )

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="") as output:
        output.write(JOKE)

    with open(output_path, "rb") as output:
        written = output.read()
    assert written.decode("utf-8") == JOKE, "Output does not match JOKE"
    print(f"Code points: {length}; bytes: {len(written)}")

if __name__ == "__main__":
    main()
