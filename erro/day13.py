import json
from functools import cmp_to_key


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return left - right
    else:
        left = [left] if isinstance(left, int) else left
        right = [right] if isinstance(right, int) else right
        for inner_left, inner_right in zip(left, right):
            result = compare(inner_left, inner_right)
            if result != 0:
                return result
        return len(left) - len(right)


with open(__file__.replace(".py", "_data")) as f:
    packets = [json.loads(line) for line in f.read().split("\n") if line]

# PART 1
pairs = [packets[i:i+2] for i in range(0, len(packets), 2)]
print(sum(i for i, (left, right) in enumerate(pairs, 1) if compare(left, right) < 0))

# PART 2
sorted_packets = sorted(packets + [[[2]], [[6]]], key=cmp_to_key(compare))
print((sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1))
