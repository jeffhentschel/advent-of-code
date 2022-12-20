import heapq
import logging
import math
import os
import re
from copy import deepcopy
from functools import reduce
from pprint import pprint
from queue import PriorityQueue

from advent_of_code_ocr import convert_6

from aoc.aoc_util import AocUtil

LOG = logging.getLogger(__name__)


def locate(c, map):
    for row in range(len(map)):
        for col in range(len(map[row])):
            if map[row][col] == c:
                return row, col


class Atlas:
    def __init__(self, atlas):
        self.atlas = atlas
        self.edge = (len(self.atlas), len(self.atlas[0]))
        self.neighbors = {}
        for i in range(self.edge[0]):
            for j in range(self.edge[1]):
                dirs = [
                    (i - 1, j + 0),
                    (i + 1, j + 0),
                    (i + 0, j - 1),
                    (i + 0, j + 1),
                ]
                self.neighbors[(i, j)] = list(
                    filter(lambda d: self.valid_step((i, j), d), dirs)
                )

    def val_at(self, c):
        val = self.atlas[c[0]][c[1]]
        val = "a" if val == "S" else val
        val = "z" if val == "E" else val
        return ord(val)

    def valid_step(self, a, b):
        if b[0] < 0 or b[1] < 0:
            return False
        if b[0] >= self.edge[0] or b[1] >= self.edge[1]:
            return False

        if self.val_at(b) > self.val_at(a) + 1:
            return False
        return True

    def find_path(self, start):
        distances = {}
        unknown = PriorityQueue()
        for r in range(self.edge[0]):
            for c in range(self.edge[1]):
                distances[(r, c)] = float("inf")
                unknown.put((float("inf"), (r, c)))

        distances[start] = 0
        unknown.put((0, start))

        while unknown.qsize() > 0:
            score, loc = unknown.get()
            letter = self.atlas[loc[0]][loc[1]]

            if score > distances[loc]:
                continue

            for o in self.neighbors[loc]:
                distance = score + 1
                if o not in distances or distances[o] > distance:
                    distances[o] = distance
                    unknown.put((distance, o))

        return distances


def solve(input: str):
    lines = input.split("\n")
    start = locate("S", lines)
    end = locate("E", lines)

    print(f"Starting at {start[0]}, {start[1]}")
    print(f"Ending at {end[0]}, {end[1]}")

    a = Atlas(lines)
    d = a.find_path(start)
    return d[end]


if __name__ == "__main__":
    aoc = AocUtil(__file__)
    input = aoc.read_input()
    answer = solve(input)
    aoc.print_answer(answer)
    aoc.submit(answer)
