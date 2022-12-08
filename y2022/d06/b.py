import logging
import math
import os
import re
from functools import reduce
from pprint import pprint

from aoc.input import read_input

LOG = logging.getLogger(__name__)
input = read_input(__file__)


def get_start(s, size=4):
    for i in range(len(s) - size):
        if len(set(s[i : i + size])) == size:
            return i + size


def solve(input):
    return get_start(input, 14)


if __name__ == "__main__":
    input = read_input(__file__)
    print(solve(input))
