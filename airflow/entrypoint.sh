#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

# Install additional runtime packages
if [[ -f apt-requirements.txt ]]; then
    apt-get update
    xargs apt-get install -y < apt-requirements.txt
fi
if [[ -f requirements.txt ]]; then
    pip3 install -r requirements.txt --no-cache-dir
fi

exec airflow "$@"
