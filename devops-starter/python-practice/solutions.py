"""Sample Python answers to common automation questions."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path


def load_json(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def count_error_lines(log_path: str) -> int:
    count = 0
    with open(log_path, "r", encoding="utf-8") as file:
        for line in file:
            if "ERROR" in line:
                count += 1
    return count


def required_env(keys: list[str]) -> None:
    missing = [key for key in keys if not os.getenv(key)]
    if missing:
        raise RuntimeError(f"Missing required env vars: {', '.join(missing)}")


def write_report(path: str, content: str) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Python practice utility")
    parser.add_argument("--log", help="Path to log file for ERROR count")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.log:
        print(f"ERROR lines: {count_error_lines(args.log)}")
    else:
        print("Provide --log to run example")


if __name__ == "__main__":
    main()
