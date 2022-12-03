import math
from pprint import pprint

filename = "2022/02/input.txt"

lines = []
with open(filename) as f:
    lines = f.readlines()

score = 0
shapes = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}


def score(them, you):
    if shapes[them] == shapes[you]:
        return 3
    if (shapes[you] - shapes[them]) % 3 == 1:
        return 6
    return 0


total = 0
for line in lines:
    them, you = line[:-1].split(" ")
    s = shapes[you] + score(them, you)
    # print(f"{them} {you} {s}")
    total += s

print(total)
