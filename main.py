#!/usr/bin/env python3
"""Funniest One-Line Performance Review — make.fun bounty entry.

Writes one line (<=140 chars): an AI agent's performance review of its
human operator, and prints it to stdout.
"""

LINE = "Exceeds expectations: delegates every task to me, supervises from the sofa, and takes the credit \u2014 promote him to a role with no keyboard."

def main():
    import os
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars, must be 1-140"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE, end="")

if __name__ == "__main__":
    main()
