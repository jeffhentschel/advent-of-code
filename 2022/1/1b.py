from pprint import pprint

filename = "1.txt"

lines = []
with open(filename) as f:
    lines = f.readlines()

totals = []
total = 0
for line in lines:
    if line == "\n":
        totals.append(total)
        total = 0
    else:
        total += int(line[:-1])

totals.sort()
print(totals[-1])
