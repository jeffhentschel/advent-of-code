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
    lines = input.split("\n")
    answer = ""

    return answer


if __name__ == "__main__":
    aoc = AocUtil(__file__)
    input = aoc.read_input()
    answer = solve(input)
    aoc.print_answer(answer)
    aoc.submit(answer)
