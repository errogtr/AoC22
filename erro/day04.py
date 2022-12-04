def get_range(r):
    a, b = r.split("-")
    return set(range(int(a), int(b) + 1))


with open(__file__.replace(".py", "_data")) as f:
    sections = [[get_range(y) for y in x.split(",")] for x in f.readlines()]

# PART 1
print(sum((x <= y) or (y <= x) for x, y in sections))

# PART 2
print(sum(len(x & y) > 0 for x, y in sections))
