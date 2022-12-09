import logging
import math
import os
import re
import subprocess
from functools import reduce
from pprint import pprint

from aoc.aoc_util import AocUtil

LOG = logging.getLogger(__name__)


def score_visible(forest, row, col, dir):
    score = 0
    height = forest[row][col]
    row += dir[0]
    col += dir[1]
    while row < len(forest) and row >= 0 and col < len(forest[row]) and col >= 0:
        c_height = forest[row][col]
        if c_height >= height:
            return score + 1
        score += 1
        row += dir[0]
        col += dir[1]
    return score


def score_tree(forest, row_i, col_i):
    # up down left right
    return (
        score_visible(forest, row_i, col_i, (0, -1))
        * score_visible(forest, row_i, col_i, (0, 1))
        * score_visible(forest, row_i, col_i, (1, 0))
        * score_visible(forest, row_i, col_i, (-1, 0))
    )


def solve(input: str):
    answer = ""
    forest = input.split("\n")
    for i in range(len(forest)):
        forest[i] = list(map(lambda x: int(x), forest[i]))

    visible_trees = 0
    max_score = 0
    for i in range(len(forest)):
        row = forest[i]
        for j in range(len(row)):
            score = score_tree(forest, i, j)
            print(f"SCORE ({i},{j}) = {forest[i][j]} = {score}")
            if score > max_score:
                max_score = score

    return max_score


if __name__ == "__main__":
    aoc = AocUtil(__file__)
    input = aoc.read_input()
    answer = solve(input)
    aoc.print_answer(answer)
    aoc.submit(answer)
