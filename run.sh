#!/usr/bin/env bash

YEAR="${2:-$(date +%Y)}"
DAY="${3:-$(date +%d)}"

python -m pytest y$YEAR/d$DAY/test_$1.py

if [ $? -eq 0 ]; then
    echo ""
    python -m y$YEAR.d$DAY.$1
else
    echo "Tests failed"
fi
