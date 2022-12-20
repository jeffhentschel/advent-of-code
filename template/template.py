from __future__ import annotations
import sys
import logging
import math
import os
import re
from functools import reduce
from pprint import pprint
from advent_of_code_ocr import convert_6

from aoc.aoc_util import AocUtil

LOG = logging.getLogger(__name__)


def solve(input: str):
    lines = input.splitlines()
    answer = ""

    return answer


if __name__ == "__main__":
    aoc = AocUtil(__file__)
    filename = sys.argv[1]
    print(f"Reading file {filename}")
    input = aoc.read_input(filename=filename)
    answer = solve(input)
    aoc.print_answer(answer)

    if filename == "input.txt":
        aoc.submit(answer)
