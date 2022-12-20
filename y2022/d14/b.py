import logging
import math
import os
import re
from functools import reduce
from pprint import pprint

from advent_of_code_ocr import convert_6

from aoc.aoc_util import AocUtil

LOG = logging.getLogger(__name__)


class Cave:
    def __init__(self, rock_paths):
        self.blocks = {}
        self.mins = [None, 0]
        self.maxs = [None, None]
        self.sands = 0
        for path in rock_paths:
            self._add_rocks(path)

        self.maxs[1] += 2

    def _update_bounds(self, a):
        # print(f"updating bounds {a} (mins = {self.mins}")
        if self.mins[0] is None or self.mins[0] > a[0]:
            self.mins[0] = a[0]
        if self.mins[1] is None or self.mins[1] > a[1]:
            self.mins[1] = a[1]

        if self.maxs[0] is None or self.maxs[0] < a[0]:
            self.maxs[0] = a[0]
        if self.maxs[1] is None or self.maxs[1] < a[1]:
            self.maxs[1] = a[1]

    def _add_rocks(self, path):
        stops = path.split(" -> ")
        for i in range(len(stops) - 1):
            a = tuple(map(lambda x: int(x), stops[i].split(",")))
            b = tuple(map(lambda x: int(x), stops[i + 1].split(",")))
            self._update_bounds(a)
            self._update_bounds(b)

            min_y = min(a[1], b[1])
            max_y = max(a[1], b[1])
            min_x = min(a[0], b[0])
            max_x = max(a[0], b[0])
            for x in range(min_x, max_x + 1):
                for y in range(min_y, max_y + 1):
                    self.blocks[(x, y)] = "#"

    def add_sand(self, start):
        if start in self.blocks:
            return self.sands

        self._update_bounds(start)

        down_y = start[1] + 1
        down = (start[0], down_y)
        dl = (start[0] - 1, down_y)
        dr = (start[0] + 1, down_y)

        if down_y == self.maxs[1]:
            self.blocks[down] = "#"
            self.blocks[dl] = "#"
            self.blocks[dr] = "#"

        if down not in self.blocks:
            return self.add_sand(down)

        if dl not in self.blocks:
            return self.add_sand(dl)

        if dr not in self.blocks:
            return self.add_sand(dr)

        self.blocks[start] = "o"
        self.sands += 1
        return self.sands

    def print(self):
        print("")
        cave_rows = []
        for row in range(self.mins[1], self.maxs[1] + 1):
            r_str = f"{row: 3} "
            for col in range(self.mins[0], self.maxs[0] + 1):
                r_str += self.blocks.get((col, row), ".")
            cave_rows.append(r_str)
        cave_str = "\n".join(cave_rows)
        print(cave_str)


def solve(input: str):
    lines = input.splitlines()
    cave = Cave(lines)
    print(f"Cave mins = {cave.mins}")
    print(f"Cave maxs = {cave.maxs}")

    start = (500, 0)
    sands = cave.add_sand(start)
    for i in range(92_500):
        new_sands = cave.add_sand(start)
        if i % 10000 == 0:
            print(f"Sand {i:,} ({new_sands:,})")
        if new_sands == sands:
            break
        sands = new_sands

    return sands


if __name__ == "__main__":
    aoc = AocUtil(__file__)
    input = aoc.read_input()
    answer = solve(input)
    aoc.print_answer(answer)

    if int(answer) <= 10001:
        print("WRONG ANSWER TOO LOW")
    elif int(answer) >= 92390:
        print("WRONG ANSWER TOO HIGH")
    else:
        aoc.submit(answer)
