#!/usr/bin/env bash

YEAR="${2:-$(date +%Y)}"
DAY="${3:-$(date +%d)}"

python -m pytest y$YEAR/d$DAY/test_$1.py

echo ""
python -m y$YEAR.d$DAY.$1
