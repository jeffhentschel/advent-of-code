import logging
import math
import os
import re
from functools import reduce
from pprint import pprint
from typing import List

import numpy
from advent_of_code_ocr import convert_6
from PIL import Image

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
        self.images: List[Image.Image] = []
        self.iter = 1

    def _update_bounds(self, a):
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
        if self.iter % 2 == 0:
            self.blocks[start] = "o"
            self.images.append(
                self.save_cave_image(f"y2022/d14/images/sand_{self.iter:04}.png")
            )
            del self.blocks[start]
        self.iter += 1

        if start[0] > self.maxs[0] or start[1] > self.maxs[1]:
            return self.sands

        down = (start[0], start[1] + 1)
        if down not in self.blocks:
            return self.add_sand(down)

        dl = (start[0] - 1, start[1] + 1)
        if dl not in self.blocks:
            return self.add_sand(dl)

        dr = (start[0] + 1, start[1] + 1)
        if dr not in self.blocks:
            return self.add_sand(dr)

        self.blocks[start] = "o"
        self.sands += 1
        self.images.append(self.save_cave_image(f"y2022/d14/sand_{self.iter:04}.png"))
        self.iter += 1
        return self.sands

    def print(self):
        print("")
        for row in range(self.mins[1], self.maxs[1] + 1):
            r_str = f"{row: 3} "
            for col in range(self.mins[0], self.maxs[0] + 1):
                r_str += self.blocks.get((col, row), ".")
            print(r_str)

    def save_cave_image(self, filename, blocks=None):
        colors = {
            ".": (37, 36, 34),
            "#": (90, 77, 65),
            "o": (194, 178, 128),
        }
        blocks = blocks or self.blocks
        pixels = []
        for row in range(self.mins[1], self.maxs[1] + 1):
            pixel_row = []
            for col in range(self.mins[0], self.maxs[0] + 1):
                pixel_row.append(colors[blocks.get((col, row), ".")])
            pixels.append(pixel_row)
        array = numpy.array(pixels, dtype=numpy.uint8)
        img = Image.fromarray(array)
        target_size = (img.size[0] * 4, img.size[1] * 4)
        img = img.resize(target_size, resample=Image.Resampling.NEAREST)
        return img


def solve(input: str):
    lines = input.splitlines()
    cave = Cave(lines)
    print(f"Cave mins = {cave.mins}")
    print(f"Cave maxs = {cave.maxs}")
    print(f"Cave rocks: ")
    pprint(cave.blocks)

    cave.print()

    start = (500, 0)

    sands = cave.add_sand(start)
    # images = [cave.save_cave_image("y2022/d14/images/sand_0000.png")]
    for i in range(1, 1000):
        new_sands = cave.add_sand(start)
        if i % 10 == 0:
            print(f"Sand {i} ({sands})")
        if new_sands == sands:
            break
        sands = new_sands
    answer = cave.sands
    durations = 10
    cave.images[0].save(
        "y2022/d14/images/sand.gif",
        save_all=True,
        append_images=cave.images[1:],
        optimize=True,
        duration=durations,
        loop=1,
    )

    return answer


if __name__ == "__main__":
    aoc = AocUtil(__file__)
    input = aoc.read_input()
    answer = solve(input)
    aoc.print_answer(answer)
    aoc.submit(answer)
