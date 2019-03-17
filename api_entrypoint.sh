#!/usr/bin/env bash

set -e

if [[ "$@" == *--api* ]]; then
    cd /src
    uwsgi --socket 0.0.0.0:${API_PORT} --yaml /src/uwsgi.yaml
fi
