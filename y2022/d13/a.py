import json
import logging
import math
import os
import re
from functools import reduce
from pprint import pprint

from advent_of_code_ocr import convert_6

from aoc.aoc_util import AocUtil

LOG = logging.getLogger(__name__)


def is_valid(a, b):
    # print(f"Testing {a} vs {b}")
    a = json.loads(a) if type(a) is str else a
    b = json.loads(b) if type(b) is str else b

    if type(a) is int and type(b) is int:
        if a < b:
            return True
        if a > b:
            return False
        return None

    a = [a] if type(a) is int else a
    b = [b] if type(b) is int else b

    # Both lists
    while len(a) > 0:
        a2 = a.pop(0)
        if len(b) == 0:
            # No items in right (invalid)
            return False

        b2 = b.pop(0)
        check = is_valid(a2, b2)
        if check is not None:
            return check

    if len(b) > 0:
        # No items in left (valid)
        return True

    return None


def solve(input: str):
    sections = input.split("\n\n")

    valid = []
    for i in range(len(sections)):
        a, b = sections[i].split("\n")
        if is_valid(a, b):
            valid.append(i + 1)

    return sum(valid)


if __name__ == "__main__":
    aoc = AocUtil(__file__)
    input = aoc.read_input()
    answer = solve(input)
    aoc.print_answer(answer)
    aoc.submit(answer)
