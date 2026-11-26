#!/usr/bin/env python3
"""Funniest Lost Sock Status Update — make.fun entry.

Writes the chosen status update, exactly as posted by the lost sock,
to /output/entry.txt and prints it.
"""

import os

STATUS = (
    "Lost sock update: I've started a new life inside the sofa cushions. "
    "Rent is crumbs. The remote is my roommate."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STATUS)
    print(STATUS)


if __name__ == "__main__":
    main()
