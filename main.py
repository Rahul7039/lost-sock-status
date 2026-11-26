#!/usr/bin/env python3
"""Funniest Lost Sock Status Update — make.fun entry.

Writes the chosen status update, exactly as posted by the lost sock,
to /output/entry.txt and prints it. The status is validated against the
competition's 120-character, single-line rule before anything is written.
"""

import os

MAX_CHARS = 120

STATUS = (
    "Lost sock update: I've started a new life inside the sofa cushions. "
    "Rent is crumbs. The remote is my roommate."
)


def validate_status(status: str) -> None:
    """Check the assembled status fits the competition's rules."""
    if len(status) > MAX_CHARS:
        raise SystemExit(
            f"status is {len(status)} chars, over the {MAX_CHARS}-char limit"
        )
    if "\n" in status or "\r" in status:
        raise SystemExit("status must be a single line")


def main() -> None:
    validate_status(STATUS)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STATUS)
    print(STATUS)


if __name__ == "__main__":
    main()
