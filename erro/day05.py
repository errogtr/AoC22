from copy import deepcopy
import re


def move_crate(positions, x, y, idx):
    positions[x].append(positions[y].pop(idx))


with open(__file__.replace(".py", "_data")) as f:
    drawing, instructions = [x.split("\n") for x in f.read().split("\n\n")]

# INPUT PARSING
crates = [list() for x in drawing[-1] if x.isdigit()]
for line in drawing[:-1]:
    for idx, c in enumerate(line):
        if c.isalpha():
            crates[int(drawing[-1][idx]) - 1].insert(0, c)
moves = [list(map(int, re.findall(r"\d+", line))) for line in instructions]

# PART 1 & 2
pos9000, pos9001 = [deepcopy(crates) for _ in [1, 2]]
for num, initial, final in moves:
    for i in range(num):
        move_crate(pos9000, final - 1, initial - 1, -1)
        move_crate(pos9001, final - 1, initial - 1, i - num)
print("".join(x[-1] for x in pos9000))
print("".join(x[-1] for x in pos9001))
