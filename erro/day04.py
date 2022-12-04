def get_range(r):
    start, end = map(int, r.split("-"))
    return set(range(start, end + 1))


with open(__file__.replace(".py", "_data")) as f:
    data = [x.split(",") for x in f.readlines()]

sections = [[get_range(i) for i in x] for x in data]

# PART 1
print(sum((x <= y) or (y <= x) for x, y in sections))

# PART 2
print(sum(len(x & y) > 0 for x, y in sections))
