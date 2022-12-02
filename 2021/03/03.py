data = []
with open("input.txt") as f:
    data = f.readlines()
for i in range(len(data)):
    data[i] = data[i].strip("\n")

# data = [
# "00100",
# "11110",
# "10110",
# "10111",
# "10101",
# "01111",
# "00111",
# "11100",
# "10000",
# "11001",
# "00010",
# "01010"
# ]

print("DATA")
for r in data:
    print(r)
print("====")


vals = [
    ([], []),
    ([], []),
    ([], []),
    ([], []),
    # ([],[]),
    # ([],[]),
    # ([],[]),
    # ([],[]),
    # ([],[]),
    # ([],[]),
    # ([],[]),
    ([], []),
]

ones = [0] * 12

oxygen = set(data)
for digit in range(len(data[0])):
    print("")
    print(f"Searching digit {digit}")
    ones = set()
    zeros = set()
    print(f"oxygen = {oxygen}")
    if len(oxygen) == 1:
        print(f"*****OXYGEN = {oxygen}")
    for num in oxygen:
        if num[digit] == "0":
            zeros.add(num)
        else:
            ones.add(num)
    print(f"ones = {ones}")
    print(f"zeros = {zeros}")
    if len(ones) >= len(zeros):
        oxygen = oxygen.intersection(ones)
    else:
        oxygen = oxygen.intersection(zeros)

if len(oxygen) != 1:
    print("ERROR ERROR TOO MUCH OXYGEN")
oxygen_val = int(oxygen.pop(), base=2)
print(oxygen_val)

co2 = set(data)
for digit in range(len(data[0])):
    print("")
    print(f"Searching digit {digit}")
    ones = set()
    zeros = set()
    print(f"co2 = {co2}")
    if len(co2) == 1:
        print(f"*****co2 = {co2}")
        break
    for num in co2:
        if num[digit] == "0":
            zeros.add(num)
        else:
            ones.add(num)
    print(f"ones = {ones}")
    print(f"zeros = {zeros}")
    if len(zeros) <= len(ones):
        co2 = co2.intersection(zeros)
    else:
        co2 = co2.intersection(ones)

if len(co2) != 1:
    print("ERROR ERROR TOO MUCH co2")
co2_val = int(co2.pop(), base=2)
print(co2_val)


print("ANSWER")
print(co2_val * oxygen_val)
# for row in data:
#     full_num = int(row, base=2)
#     print(f"number = {row} ({full_num})")
#     for i in range(len(row)):
#         digit = int(row[i])
#         # print(f"  i = {i} | digit = {digit}")

#         ones[i] += digit
#         vals[i][digit].append(int(row,base=2))


# print(f"ONES (total = {len(data)}")
# print(ones)
# print("")
# for v in vals:
#     print(v)


# oxygen = set()
# co2_scrubber = set()
# if len(vals[0][1]) >= len(vals[0][0]):
#     oxygen = set(vals[0][1])
#     co2_scrubber = set(vals[0][0])
# else:
#     oxygen = set(vals[0][0])
#     co2_scrubber = set(vals[0][1])
# print("finding oxy/co2")
# for zeros,ones in vals:
#     if len(oxygen) == 1:
#         print(f"OXY FOUND {oxygen}")
#     if len(co2_scrubber) == 1:
#         print(f"CO2 FOUND = {co2_scrubber}")

#     print(f"oxygen = {oxygen}")
#     print(f"co2 = {co2_scrubber}")
#     if len(ones) >= len(zeros):
#         print("ones bigger")
#         oxygen = oxygen.intersection(set(ones))
#         co2_scrubber = oxygen.intersection(set(zeros))
#     else:
#         print("zeros biggger")
#         oxygen = oxygen.intersection(set(zeros))
#         co2_scrubber = co2_scrubber.intersection(set(zeros))


# for digit in range(len(ones)):
#     if ones[digit] > len(data) - ones[digit]:
#         print(f"digit {digit} adding 1s")
#         oxygen += sum(vals[digit][1])
#         co2_scrubber += sum(vals[digit][0])
#     else:
#         print(f"digit {digit} adding 0s")
#         co2_scrubber += sum(vals[digit][1])
#         oxygen += sum(vals[digit][0])

# print(f"O = {oxygen} | co2 = {co2_scrubber}")
# print(f" Answer = {oxygen * co2_scrubber}")

print("it's not  152598569245290")
print("it's not  152888338731348")
# 152598569245290 not right
