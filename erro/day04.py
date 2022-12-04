import re


with open(__file__.replace(".py", "_data")) as f:
    sections = [list(map(int, re.findall(r"\d+", x))) for x in f.readlines()]

# PART 1
print(sum((a <= c <= d <= b) or (c <= a <= b <= d) for a, b, c, d in sections))

# PART 2
print(sum(c <= b <= d or a <= d <= b for a, b, c, d in sections))
