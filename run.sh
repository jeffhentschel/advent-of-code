#!/usr/bin/env bash

YEAR=$(date +%Y)
DAY=$(date +%d)

python -m pytest y$YEAR/d$DAY/test_$1.py

echo ""
echo "-- ANSWER --"
ANSWER=$(python -m y$YEAR.d$DAY.$1)
echo $ANSWER
echo -n $ANSWER | pbcopy
echo ""
