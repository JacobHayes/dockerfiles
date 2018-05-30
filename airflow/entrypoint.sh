#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

# Install additional runtime packages
if [[ -f apt-requirements.txt ]]; then
    apt-get update
    xargs apt-get install -y < apt-requirements.txt
fi
if [[ -n "${APT_REQUIREMENTS:-}" ]]; then
    apt-get update
    apt-get install -y ${APT_REQUIREMENTS}
fi
if [[ -f requirements.txt ]]; then
    pip3 install --no-cache-dir -r requirements.txt
fi
if [[ -n "${REQUIREMENTS:-}" ]]; then
    pip3 install --no-cache-dir ${REQUIREMENTS}
fi

exec airflow "$@"
