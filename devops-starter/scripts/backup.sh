#!/usr/bin/env bash
set -euo pipefail

SRC_DIR="${1:-./python-app}"
BACKUP_DIR="${2:-./backups}"
TIMESTAMP="$(date +%Y%m%d_%H%M%S)"
ARCHIVE_PATH="${BACKUP_DIR}/project_${TIMESTAMP}.tar.gz"

mkdir -p "${BACKUP_DIR}"
tar -czf "${ARCHIVE_PATH}" "${SRC_DIR}"

echo "Backup created at: ${ARCHIVE_PATH}"
