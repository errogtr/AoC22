from math import prod


def get_directions(data, x, y):
    up = [data[y - i][x] for i in range(1, y + 1)]
    down = [data[y + i][x] for i in range(1, length - y)]
    left = [data[y][x - i] for i in range(1, x + 1)]
    right = [data[y][x + i] for i in range(1, length - x)]
    return up, down, left, right


def get_view(height, direction):
    direction_score = 0
    for i in direction:
        direction_score += 1
        if i >= height:
            break
    return direction_score


with open(__file__.replace(".py", "_data")) as f:
    data = f.read().splitlines()

length = len(data)
visible = 4 * (length - 1)
scenic_score = 0
for y, row in enumerate(data):
    for x, height in enumerate(row):
        if x in (0, length - 1) or y in (0, length - 1):
            continue
        directions = get_directions(data, x, y)

        # PART 1
        for d in directions:
            if max(d) < height:
                visible += 1
                break

        # PART 2
        scenic_score = max(scenic_score, prod(get_view(height, d) for d in directions))

print(visible, scenic_score, sep="\n")
