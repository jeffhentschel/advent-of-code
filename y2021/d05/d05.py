vectors = []
with open("input.txt") as f:
    vectors = f.readlines()


coords = {}
for v in vectors:
    a, ignore, b = v.split(" ")
    x1, y1 = a.split(",")
    x2, y2 = b.split(",")
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    if y2[-1] == "\n":
        y2 = int(y2[:-1])
    else:
        y2 = int(y2)

    if x1 == x2:
        # vertical
        start = y1
        end = y2
        if y2 < y1:
            start = y2
            end = y1

        print("")
        print(f"STATTING VERT ({x1},{start}) -> ({x2},{end})")

        for cy in range(start, end + 1):
            key = f"{x1},{cy}"
            print(f"vert={key}")
            if key in coords:
                coords[key] += 1
            else:
                coords[key] = 1
    elif y1 == y2:
        # horiz
        start = x1
        end = x2
        if x2 < x1:
            start = x2
            end = x1

        print("")
        print(f"STATTING HORIZ ({start},{y1}) -> ({end},{y2})")
        for cx in range(start, end + 1):
            key = f"{cx},{y1}"
            print(f"horiz={key}")
            if key in coords:
                coords[key] += 1
            else:
                coords[key] = 1
    else:
        start_x = x1
        end_x = x2
        start_y = y1
        end_y = y2
        if x1 > x2:
            start_x = x2
            end_x = x1
            start_y = y2
            end_y = y1

        climb = 1
        if start_y > end_y:
            climb = -1

        i = 0
        print("")
        print(f"STATTING DIAG ({start_x},{start_y}) -> ({end_x},{end_y})")
        x_steps = end_x - start_x
        y_steps = end_y - start_y
        if abs(x_steps) != abs(y_steps):
            print("ERROR IN STEPS")
        print(
            f"  - x_steps = {end_x - start_x} and y_steps = {end_y - start_y} | climb = {climb}"
        )
        for x in range(start_x, end_x + 1):
            y = start_y + (i * climb)
            key = f"{x},{y}"
            # if x >= end_x:
            print(f"diag={key}")
            if key in coords:
                coords[key] += 1
            else:
                coords[key] = 1
            i += 1

    # print(f"({x1},{y1}) -> ({x2},{y2})")


print("")
print("CROSSES")
cross = 0
for coord in coords:
    if coords[coord] > 1:
        cross += 1
        print(coord)

print(cross)
