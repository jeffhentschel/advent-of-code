#!/usr/bin/env bash

YEAR=$(date +%Y)
DAY=$(date +%d)
DIR=$YEAR/$DAY

if [ "$1" != "-o" ] && [ -d $DIR ]; then
  echo "$DIR already setup. Use -o to overwrite."
  exit 1
fi

SESSION_COOKIE=$(cat .session)

echo "----- $YEAR Day $DAY -----"
echo "📂 Creating directory $DIR"
mkdir -p $DIR

echo "🐍 Initializing template"
cp template.py $DIR/a.py
cp template.py $DIR/b.py
touch $DIR/__init__.py

echo "🗒️  Fetching input file"
curl --silent \
  --output $DIR/input.txt \
  --cookie "$SESSION_COOKIE" \
  https://adventofcode.com/$YEAR/day/$(date +%-d)/input
