import logging
import math
import os
import re
import subprocess
from functools import reduce
from pprint import pprint

from aoc.aoc_util import AocUtil

LOG = logging.getLogger(__name__)


def create_rope(knots: int):
    rope = [[0, 0]]
    for i in range(knots):
        rope.append([0, 0])
    return rope


def follow(knot, prev):
    x_delta = prev[0] - knot[0]
    y_delta = prev[1] - knot[1]

    if abs(x_delta) > 1:
        knot[0] += int(math.copysign(1, x_delta))
        if abs(y_delta) == 1:
            knot[1] += y_delta

    if abs(y_delta) > 1:
        knot[1] += int(math.copysign(1, y_delta))
        if abs(x_delta) == 1:
            knot[0] += x_delta


def solve(input: str):
    bridge = set((0, 0))
    rope = create_rope(9)

    moves = {
        "R": (0, 1),
        "L": (0, -1),
        "U": (1, 1),
        "D": (1, -1),
    }

    for line in input.split("\n"):
        d, c = line.split(" ")
        print("")
        print(f"Head at {rope[0]}, moving {d} {c}")
        for i in range(int(c)):
            move = moves[d]
            rope[0][moves[d][0]] += moves[d][1]
            # print(f"Head at {knots[0]}, move is {d} {c}")

            for i in range(1, len(rope)):
                follow(rope[i], rope[i - 1])

            bridge.add(tuple(rope[-1]))

    print(rope)
    return len(bridge) - 1


if __name__ == "__main__":
    aoc = AocUtil(__file__)
    input = aoc.read_input()
    answer = solve(input)
    aoc.print_answer(answer)
    aoc.submit(answer)
