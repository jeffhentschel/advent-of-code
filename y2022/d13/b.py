import json
import logging
import math
import os
import re
from functools import cmp_to_key, reduce
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
            return -1
        if a > b:
            return 1
        return 0

    a = [a] if type(a) is int else a
    b = [b] if type(b) is int else b

    # Both lists
    while len(a) > 0:
        a2 = a.pop(0)
        if len(b) == 0:
            # No items in right
            return 1

        b2 = b.pop(0)
        check = is_valid(a2, b2)
        if check != 0:
            return check

    if len(b) > 0:
        # No items in left
        return -1

    return 0


def solve(input: str):
    lines = input.split("\n")
    packets = list(filter(lambda x: x.strip() != "", lines))
    packets.append("[[2]]")
    packets.append("[[6]]")
    packets.sort(key=cmp_to_key(is_valid))

    return (packets.index("[[2]]") + 1) * (packets.index("[[6]]") + 1)


if __name__ == "__main__":
    aoc = AocUtil(__file__)
    input = aoc.read_input()
    answer = solve(input)
    aoc.print_answer(answer)
    aoc.submit(answer)
