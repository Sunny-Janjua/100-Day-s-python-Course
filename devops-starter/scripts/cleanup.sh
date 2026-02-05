#!/usr/bin/env bash
set -euo pipefail

TARGET_DIR="${1:-./backups}"
DAYS="${2:-7}"

if [[ ! -d "${TARGET_DIR}" ]]; then
  echo "Target directory does not exist: ${TARGET_DIR}"
  exit 0
fi

find "${TARGET_DIR}" -type f -name '*.tar.gz' -mtime +"${DAYS}" -print -delete
echo "Cleanup completed for files older than ${DAYS} days in ${TARGET_DIR}"
