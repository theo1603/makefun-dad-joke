#!/usr/bin/env python3
"""Write one dad joke to /output/entry.txt.

Revision (v2): dropped "single" (tighter) and added a second beat —
"Even the new ones arrive old" — which extends the "dated" pun
instead of just repeating it. The joke is now a two-step groan:
the calendar always has a date, its jokes are dated, and even its
new ones show up old. Punchline still lands at the end.
"""

from pathlib import Path

TEXT = (
    "I told my kids the calendar is my favourite comedian: "
    "it always has a date, and every joke it tells is dated. "
    "Even the new ones arrive old."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
