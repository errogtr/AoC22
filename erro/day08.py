from itertools import takewhile


def get_directions(heights, x, y):
    up = [heights[(x, y - i)] for i in range(1, y + 1)]
    down = [heights[(x, y + i)] for i in range(1, length - y)]
    left = [heights[(x - i, y)] for i in range(1, x + 1)]
    right = [heights[(x + i, y)] for i in range(1, length - x)]
    return up, down, left, right


with open(__file__.replace(".py", "_data")) as f:
    data = f.read().splitlines()

heights = dict()
for y, line in enumerate(data):
    for x, val in enumerate(line):
        heights[(x, y)] = int(val)

length = len(data)
visible = 4 * (length - 1)
for (x, y), height in heights.items():
    if x in (0, length - 1) or y in (0, length - 1):
        continue

    for direction in get_directions(heights, x, y):
        if max(direction) < height:
            visible += 1
            break

print(visible)

viewing_score = 0
for (x, y), height in heights.items():
    if x in (0, length - 1) or y in (0, length - 1):
        continue

    up, down, left, right = 0, 0, 0, 0
    for i in range(1, y + 1):
        up += 1
        if heights[(x, y - i)] >= height:
            break

    for i in range(1, length - y):
        down += 1
        if heights[(x, y + i)] >= height:
            break

    for i in range(1, x + 1):
        left += 1
        if heights[(x - i, y)] >= height:
            break

    for i in range(1, length - x):
        right += 1
        if heights[(x + i, y)] >= height:
            break

    viewing_score = max(viewing_score, up * down * left * right)

print(viewing_score)
