import logging
import math
import os
import re
from functools import reduce
from pprint import pprint

from advent_of_code_ocr import convert_6

from aoc.aoc_util import AocUtil

LOG = logging.getLogger(__name__)

monkeys = {}


class Monkey:
    def __init__(self, data):
        lines = data.splitlines()
        self.id = int(lines[0].split(":")[0].strip())
        self.items = list(
            map(lambda x: int(x.strip()), lines[1].split(":")[1].split(","))
        )
        self.op = lines[2].split("new = ")[1]
        self.div_test = int(lines[3].split("divisible by ")[1].strip())
        self.true_dest = int(lines[4].split("monkey ")[1])
        self.false_dest = int(lines[5].split("monkey ")[1])
        self.items_inspected = 0
        self.relief = None

    def take_turn(self):
        while len(self.items) > 0:
            yield self.handle_item(self.items.pop(0))

    def handle_item(self, worry):
        self.items_inspected += 1
        val = self.do_op(worry)
        return self.get_dest(val), val

    def do_op(self, old):
        old = old % self.relief
        # Danger!
        return eval(self.op)

    def get_dest(self, x):
        if x % self.div_test == 0:
            return self.true_dest
        return self.false_dest


def solve(input: str):
    lines = input.split("\n")
    answer = ""
    instructions = input.split("\nMonkey")
    instructions[0] = instructions[0][7:]

    monkeys = {}
    for chunk in instructions:
        monkey = Monkey(chunk)
        monkeys[monkey.id] = monkey

    relief = reduce(lambda r, m: r * m.div_test, monkeys.values(), 1)
    for m in monkeys.values():
        m.relief = relief

    for round in range(10000):
        for i in range(len(monkeys)):
            monkey: Monkey = monkeys[i]
            for dest, val in monkey.take_turn():
                monkeys[dest].items.append(val)

    vals = sorted(monkeys.values(), key=lambda m: -m.items_inspected)
    print("______")
    for m in monkeys.values():
        print(f"Monkey {m.id} inspected {m.items_inspected}")
    return vals[0].items_inspected * vals[1].items_inspected


if __name__ == "__main__":
    aoc = AocUtil(__file__)
    input = aoc.read_input()
    answer = solve(input)
    aoc.print_answer(answer)
    aoc.submit(answer)
