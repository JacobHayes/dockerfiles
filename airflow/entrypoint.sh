#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

# Install additional runtime packages
if [[ -n "${APT_REQUIREMENTS:-}" ]]; then
    apt-get update
    apt-get install -y ${APT_REQUIREMENTS}
fi
if [[ -n "${REQUIREMENTS:-}" ]]; then
    pip3 install --no-cache-dir ${REQUIREMENTS}
fi

exec airflow "$@"
