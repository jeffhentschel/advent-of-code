import logging
import math
import os
from pprint import pprint

from aoc.input import read_input

LOG = logging.getLogger(__name__)
input = read_input(__file__)


def priority(c):
    if c == c.lower():
        return ord(c) - 96
    return ord(c) - 38


total = 0
for line in input.split("\n"):
    half = int(len(line) / 2)
    left = set(line[:half])
    right = set(line[half:])

    match = left.intersection(right).pop()
    score = priority(match)
    # print(f"Matched {match} == {score}")
    total += priority(left.intersection(right).pop())

print(total)
