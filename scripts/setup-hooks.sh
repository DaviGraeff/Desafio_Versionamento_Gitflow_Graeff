#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$REPO_ROOT"

if [[ ! -d ".githooks" ]]; then
  echo "Pasta .githooks não encontrada."
  exit 1
fi

chmod +x .githooks/pre-commit

git config core.hooksPath .githooks

echo "Hooks configurados com sucesso."
echo "core.hooksPath=$(git config --get core.hooksPath)"
