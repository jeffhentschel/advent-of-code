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

    sprite = [0, 1, 2]
    cycle = 0
    rows = ["." * 40, "." * 40, "." * 40, "." * 40, "." * 40, "." * 40]
    row = 0

    def print_crt():
        print(f"Cycle {cycle}")
        for r in rows:
            print(r)
        print("")

    def update_crt():
        if cycle in sprite:
            tmp = list(rows[row])
            tmp[cycle] = "#"
            rows[row] = "".join(tmp)
            print_crt()

    def tick():
        nonlocal cycle
        nonlocal row
        update_crt()
        cycle += 1
        if cycle == 40:
            cycle = 0
            row += 1

    for line in lines:
        parts = line.split(" ")
        tick()
        if parts[0] == "addx":
            tick()
            sprite = list(map(lambda x: x + int(parts[1]), sprite))

    return "\n".join(rows)


if __name__ == "__main__":
    aoc = AocUtil(__file__)
    input = aoc.read_input()
    answer = solve(input)
    converted = convert_6(answer)
    aoc.print_answer(converted)
    aoc.submit(converted)
