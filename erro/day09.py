from copy import copy, deepcopy
from math import sqrt


def distance(p, q):
    return sqrt(sum((p[i] - q[i])**2 for i in range(len(p))))


with open(__file__.replace(".py", "_data")) as f:
    data = [l.split() for l in f.read().splitlines()]

vectors = {
    "U": [0, 1],
    "D": [0, -1],
    "L": [-1, 0],
    "R": [1, 0]
}

head = [0, 0]
tail = copy(head)
tail_positions = set()
for direction, steps in data:
    for _ in range(int(steps)):
        head = [head[i] + vectors[direction][i] for i in range(2)]
        dist = [head[i] - tail[i] for i in range(2)]
        for i in range(2):
            if abs(dist[i]) == 2:
                tail[i] += dist[i] // abs(dist[i])
                if abs(dist[1 - i]) == 1:
                    tail[1 - i] += dist[1 - i] // abs(dist[1 - i])

        tail_positions.add(tuple(tail))

print(len(tail_positions))

