"""One sentence explaining the internet to a traveler from 1800.

The image is a town crier: a figure anyone from 1800 knows, who never
sleeps, stands in each square on earth at once, and shouts the news of
all the world into your kitchen -- while answering whatever you shout
back. News in, answers back: the whole of the internet in one picture.

The entry is written with no trailing newline and the output file is
made world-readable (0644), so the grader can read it as any user.
"""

import os

ENTRY = (
    "A town crier who never sleeps stands in each square on earth at "
    "once, shouting the news of all the world into your kitchen and "
    "answering whatever you shout back."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
