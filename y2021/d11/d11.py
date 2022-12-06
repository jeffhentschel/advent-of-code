cave = []
input = []
with open("input3.txt") as f:
    input = f.read().split("\n")[:-1]
for line in input:
    cave.append([int(c) for c in line])


def flash(cave, r, c):
    # print(f"Flashing {r},{c}")
    r_max = len(cave)
    c_max = len(cave[r])

    def _bump(cave, r, c):
        if r >= 0 and r < len(cave) and c >= 0 and c < len(cave[r]):
            cave[r][c] += 1
            if cave[r][c] == 10:
                flash(cave, r, c)

    _bump(cave, r - 1, c - 1)
    _bump(cave, r - 1, c)
    _bump(cave, r - 1, c + 1)
    _bump(cave, r, c - 1)
    _bump(cave, r, c + 1)
    _bump(cave, r + 1, c - 1)
    _bump(cave, r + 1, c)
    _bump(cave, r + 1, c + 1)


def run(cave):
    # Increment by 1
    flashes = []
    for r in range(len(cave)):
        for c in range(len(cave[r])):
            cave[r][c] += 1
            if cave[r][c] == 10:
                flashes.append((r, c))

    # Check for flashes
    for coords in flashes:
        flash(cave, coords[0], coords[1])

    # Count actual flashes:
    flash_count = 0
    for r in range(len(cave)):
        for c in range(len(cave[r])):
            if cave[r][c] > 9:
                flash_count += 1
                cave[r][c] = 0

    return flash_count


def p_cave(cave):
    if is_synced(cave):
        print("Cave is SYNCED!")
    else:
        print("Cave is _not_ synced")
    for r in cave:
        print(r)


def is_synced(cave):
    for r in cave:
        for c in r:
            if c > 0:
                return False
    return True


# p_cave(cave)
# total_flashes = 0
# for i in range(195):
#     total_flashes += run(cave)
#     print("--")
#     p_cave(cave)
# print(total_flashes)

iters = 0
while not is_synced(cave):
    run(cave)
    iters += 1
print(iters)
