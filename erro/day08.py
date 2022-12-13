from math import prod


def get_view(height, direction):
    score = 0
    for i in direction:
        score += 1
        if i >= height:
            break
    return score


with open(__file__.replace(".py", "_data")) as f:
    data = f.read().splitlines()

length = len(data)
visible = 4 * (length - 1)
scenic_score = 0
for y, row in enumerate(data[1:-1], 1):
    for x, height in enumerate(row[1:-1], 1):
        up = [data[y - i][x] for i in range(1, y + 1)]
        down = [data[y + i][x] for i in range(1, length - y)]
        left = [data[y][x - i] for i in range(1, x + 1)]
        right = [data[y][x + i] for i in range(1, length - x)]

        # PART 1
        for d in (up, down, left, right):
            if max(d) < height:
                visible += 1
                break

        # PART 2
        scenic_score = max(scenic_score, prod(get_view(height, d) for d in (up, down, left, right)))

print(visible, scenic_score, sep="\n")
