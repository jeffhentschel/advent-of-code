import math
from pprint import pprint

filename = "2022/02/input.txt"

lines = []
with open(filename) as f:
    lines = f.readlines()

score = 0
shapes = {"A": 1, "B": 2, "C": 3, "X": 0, "Y": 3, "Z": 6}


def score(them, result):
    val = shapes[them]
    if shapes[result] == 6:
        val += 1
    elif shapes[result] == 0:
        val += 2
    if val > 3:
        val -= 3
    return val


total = 0
for line in lines:
    them, result = line[:-1].split(" ")
    s = shapes[result] + score(them, result)
    # print(f"{them} {result} {s}")
    total += s

print(total)
