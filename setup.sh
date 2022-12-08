#!/usr/bin/env bash

YEAR="${1:-$(date +%Y)}"
DAY="${2:-$(date +%d)}"
DIR=y$YEAR/d$DAY

if [ "$3" != "-o" ] && [ -d $DIR ]; then
  echo "$DIR already setup. Use -o to overwrite."
  exit 1
fi

SESSION_COOKIE=$(cat .session)

echo "----- $YEAR Day $DAY -----"
echo "📂 Creating directory $DIR"
mkdir -p $DIR

echo "🐍 Initializing template"
TEMPLATE_DIR=template
cp $TEMPLATE_DIR/template.py $DIR/a.py
cp $TEMPLATE_DIR/template.py $DIR/b.py
cp $TEMPLATE_DIR/test_a_template.py $DIR/test_a.py
cp $TEMPLATE_DIR/test_b_template.py $DIR/test_b.py
touch $DIR/__init__.py

echo "🗒️  Fetching input file"
curl --silent \
  --output $DIR/input.txt \
  --cookie "$SESSION_COOKIE" \
  https://adventofcode.com/$YEAR/day/$DAY/input
