import logging
import math
import os
import re
import subprocess
from functools import reduce
from pprint import pprint

from aoc.aoc_util import AocUtil

LOG = logging.getLogger(__name__)


def can_see(tree, max_height, row_range, col_range):
    for row in row_range:
        for col in col_range:
            if tree[row][col] >= max_height:
                return False

    return True


def is_visible(tree, row_i, col_i):
    max_height = tree[row_i][col_i]
    bottom_edge = len(tree)
    right_edge = len(tree[bottom_edge - 1])
    return (
        can_see(tree, max_height, [row_i], range(col_i - 1, -1, -1))
        or can_see(tree, max_height, [row_i], range(col_i + 1, right_edge))
        or can_see(tree, max_height, range(row_i - 1, -1, -1), [col_i])
        or can_see(tree, max_height, range(row_i + 1, bottom_edge), [col_i])
    )


def solve(input: str):
    trees = input.split("\n")
    for i in range(len(trees)):
        trees[i] = list(map(lambda x: int(x), trees[i]))

    visible_trees = 0
    for i in range(len(trees)):
        for j in range(len(trees[i])):
            if is_visible(trees, i, j):
                print(f"YES visible ({i},{j}) = {trees[i][j]} ")
                visible_trees += 1
            else:
                print(f"NOT visible ({i},{j}) = {trees[i][j]} ")

    return visible_trees


if __name__ == "__main__":
    aoc = AocUtil(__file__)
    input = aoc.read_input()
    answer = solve(input)
    aoc.print_answer(answer)
    aoc.submit(answer)
