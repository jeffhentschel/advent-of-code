import logging
import math
import os
import re
from functools import reduce
from pprint import pprint

from aoc.input import read_input

LOG = logging.getLogger(__name__)
input = read_input(__file__)


def create_crates(lines):
    crates = {}
    for line_i in range(len(lines)):
        line = lines[line_i]
        if line[1] == "1":
            return crates, line_i
        for i in range(1, len(line), 4):
            crate_i = str(round(i / 4) + 1)
            if line[i] != " ":
                if crate_i not in crates:
                    crates[crate_i] = []
                crates[crate_i].insert(0, line[i])


lines = input.split("\n")
crates, crate_end = create_crates(lines)

instruction = "move (\d+) from (\d+) to (\d+)"
for i in range(crate_end + 2, len(lines)):
    count, src, dest = re.search(instruction, lines[i]).groups()
    letters = crates[src][-int(count) :]
    del crates[src][-int(count) :]
    crates[dest].extend(letters)

tops = reduce(lambda t, k: t + crates[k][-1], sorted(crates.keys()), "")
print(tops)
