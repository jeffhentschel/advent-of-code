#!/usr/bin/env bash

YEAR=$(date +%Y)
DAY=$(date +%d)

python -m $YEAR.$DAY.$1
