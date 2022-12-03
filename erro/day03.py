from more_itertools import chunked


def get_priority(c):
    item = set.intersection(*map(set, c)).pop()
    return ord(item) - 96 if ord(item) > ord("Z") else ord(item) - 38


if __name__ == "__main__":
    with open(__file__.replace(".py", "_data")) as f:
        data = [x.strip() for x in f.readlines()]

    # PART 1
    print(sum(get_priority(chunked(x, len(x) // 2)) for x in data))

    # PART 2
    print(sum(get_priority(c) for c in chunked(data, 3)))
