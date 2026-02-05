"""Simple health checker for the running API."""

import argparse
import sys
import requests


def run_health_check(url: str, timeout: int) -> int:
    try:
        response = requests.get(url, timeout=timeout)
        if response.status_code == 200:
            print(f"HEALTHY: {url}")
            return 0
        print(f"UNHEALTHY: {url} (status={response.status_code})")
        return 1
    except requests.RequestException as exc:
        print(f"ERROR: health check failed for {url}: {exc}")
        return 2


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Health check script")
    parser.add_argument("--url", default="http://localhost:8000/health")
    parser.add_argument("--timeout", type=int, default=5)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    code = run_health_check(args.url, args.timeout)
    sys.exit(code)
