import math
from pprint import pprint


def process_input(filename):
    lines = []
    with open(filename) as f:
        lines = f.readlines()
    input = [list(l)[:-1] for l in lines]

    for r in range(len(input)):
        for c in range(len(input[r])):
            input[r][c] = int(input[r][c])
    return input


class TheCave:
    def __init__(self, cave, expand=0):
        self.cave = cave
        self.max_r = len(self.cave) - 1
        self.max_c = len(self.cave[self.max_r]) - 1
        self.dest = self.max_r, self.max_c
        self.costs = {(self.dest): self.value_at(self.dest)}
        if expand > 0:
            self._expand(expand)

    def _expand(self, x):
        for i in range(1, x):
            for r in range(self.max_r + 1):
                for c in range(self.max_c + 1):
                    nv = self.cave[r][c] + i
                    if nv > 9:
                        nv = nv - 9
                    self.cave[r].append(nv)

        for i in range(1, x):
            for r in range(self.max_r + 1):
                new_r = []
                for c in range(len(self.cave[r])):
                    nv = self.cave[r][c] + i
                    if nv > 9:
                        nv = nv - 9
                    new_r.append(nv)
                self.cave.append(new_r)

        self.max_r = len(self.cave) - 1
        self.max_c = len(self.cave[self.max_r]) - 1
        self.dest = self.max_r, self.max_c

    def print_cave(self):
        print(f"   {list(range(self.max_c))}")
        print(f"{'-'*(self.max_c + 10)}")
        for i in range(len(self.cave)):
            print(f"{i}: {self.cave[i]}")
            # print(f"{' '.join(r)}")

    def value_at(self, loc):
        return self.cave[loc[0]][loc[1]]

    def find_min_loc(self, q, scores):
        min_loc = list(q)[0]
        min_score = scores[min_loc]

        for loc in q:
            score = scores[loc]
            if score < min_score:
                min_score = score
                min_loc = loc
        return min_loc

    def calc_score(self, start):
        scores = {}
        prevs = {}
        q = set()
        print(f"Calculating score to {start}")
        for r in range(len(self.cave)):
            for c in range(len(self.cave[r])):
                loc = (r, c)
                scores[loc] = math.inf
                prevs[loc] = None
                q.add(loc)
        scores[start] = 0

        print(f"Scoring started with len(q)={len(q)}")
        while len(q) > 0:
            print(f"len(q) = {len(q)}")
            u = self.find_min_loc(q, scores)
            # print(f"found min u = {u}")
            q.remove(u)

            if u == self.dest:
                break
            else:
                neighbors = [
                    (u[0] - 1, u[1]),  # up
                    (u[0] + 1, u[1]),  # down
                    (u[0], u[1] - 1),  # left
                    (u[0], u[1] + 1),  # right
                ]
                for n in neighbors:
                    if n in q:
                        # print(f"found neighbor to {u} => {n}")
                        alt = scores[u] + self.value_at(n)
                        # print(f"Alt dist {u} => {n} = {alt}")
                        if alt < scores[n]:
                            # print(f" Found new min {u} => {n} = {alt}")
                            scores[n] = alt
                            prevs[n] = u

        print("Path found. Calculating score.")
        s = []
        u = self.dest
        if prevs[u] or u == start:
            while u:
                s.insert(0, u)
                u = prevs[u]

        score = 0
        for l in s:
            score += self.value_at(l)
        return score


cave_data = process_input("input2.txt")
cave = TheCave(cave_data, 5)
cave.print_cave()

start = (0, 0)
cost = cave.calc_score(start) - cave.value_at(start)
print(f"{start} -> {cave.dest} = {cost}")
