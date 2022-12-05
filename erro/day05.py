import re
from collections import defaultdict

with open(__file__.replace(".py", "_data")) as f:
    drawing, instructions = [x.split("\n") for x in f.read().split("\n\n")]

# INPUT PARSING
crates = defaultdict(list)
for line in drawing[:-1]:
    for idx, c in enumerate(line):
        if c.isalpha():
            crates[drawing[-1][idx]].insert(0, c)
moves = [re.findall(r"\d+", line) for line in instructions]

# PART 1
for num, initial, final in moves:
    for _ in range(int(num)):
        crates[final].append(crates[initial].pop(-1))
print("".join(crates[str(key + 1)][-1] for key in range(len(crates))))

