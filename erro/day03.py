from string import ascii_letters
from more_itertools import chunked

CHR2NUM = {c: i for i, c in enumerate(ascii_letters, 1)}


def get_priority(c):
    return CHR2NUM[set.intersection(*map(set, c)).pop()]


if __name__ == "__main__":
    with open(__file__.replace(".py", "_data")) as f:
        data = [x.strip() for x in f.readlines()]

    # PART 1
    print(sum(get_priority(chunked(x, len(x) // 2)) for x in data))

    # PART 2
    print(sum(get_priority(c) for c in chunked(data, 3)))
