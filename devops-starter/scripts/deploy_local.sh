#!/usr/bin/env bash
set -euo pipefail

IMAGE_NAME="devops-starter:local"

pushd "$(dirname "$0")/.." >/dev/null

docker build -f docker/Dockerfile -t "${IMAGE_NAME}" .
docker rm -f devops-starter-local >/dev/null 2>&1 || true
docker run -d --name devops-starter-local -p 8000:8000 "${IMAGE_NAME}"

popd >/dev/null

echo "Local deployment complete. Check: http://localhost:8000/health"
