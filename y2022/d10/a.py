import logging
import math
import os
import re
from functools import reduce
from pprint import pprint

from aoc.aoc_util import AocUtil

LOG = logging.getLogger(__name__)


def solve(input: str):
    lines = input.split("\n")

    x = 1
    cycle = 0
    answer = 0

    def tick():
        nonlocal cycle
        nonlocal answer
        cycle += 1
        if (cycle - 20) % 40 == 0:
            answer += x * cycle

    for line in lines:
        parts = line.split(" ")
        tick()
        if parts[0] == "addx":
            tick()
            x += int(parts[1])

    return answer


if __name__ == "__main__":
    aoc = AocUtil(__file__)
    input = aoc.read_input()
    answer = solve(input)
    aoc.print_answer(answer)
    aoc.submit(answer)
