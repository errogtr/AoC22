from math import sqrt


def move_tail(moves: list, length: int, vectors: dict):
    rope = [0j] * length
    tail_positions = set()
    for direction, steps in moves:
        for _ in range(int(steps)):
            rope[0] += vectors[direction]
            for n in range(1, len(rope)):
                diff = rope[n - 1] - rope[n]
                if abs(diff) > sqrt(2):
                    if diff.real != 0:
                        rope[n] += diff.real / abs(diff.real)
                    if diff.imag != 0:
                        rope[n] += complex(0, diff.imag) / abs(diff.imag)
            tail_positions.add(rope[-1])
    return tail_positions


with open(__file__.replace(".py", "_data")) as f:
    moves = [l.split() for l in f.read().splitlines()]

vectors = {"U": 1j, "D": -1j, "L": -1, "R": 1}

# PART 1
print(len(move_tail(moves, 2, vectors)))

# PART 2
print(len(move_tail(moves, 10, vectors)))
