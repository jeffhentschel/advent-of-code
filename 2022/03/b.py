import logging
import math
import os
from pprint import pprint

LOG = logging.getLogger(__name__)

input_file = "2022/03/input.txt"
LOG.info(f"Loading file {input_file}")
with open(input_file) as f:
    input = f.read()


def priority(c):
    if c == c.lower():
        return ord(c) - 96
    return ord(c) - 38


total = 0
lines = input.split("\n")[:-1]
for i in range(0, len(lines), 3):
    match = (
        set(lines[i]).intersection(set(lines[i + 1])).intersection(lines[i + 2]).pop()
    )
    total += priority(match)

print(total)
