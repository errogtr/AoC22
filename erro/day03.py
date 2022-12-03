from string import ascii_lowercase, ascii_uppercase
from more_itertools import chunked

CHR2NUM = {c: i for i, c in enumerate(ascii_lowercase + ascii_uppercase, 1)}

if __name__ == "__main__":
    with open(__file__.replace(".py", "_data")) as f:
        data = [x.strip() for x in f.readlines()]

    # PART 1
    print(sum(CHR2NUM[set.intersection(*map(set, chunked(x, len(x) // 2))).pop()] for x in data))

    # PART 2
    print(sum(CHR2NUM[set.intersection(*map(set, c)).pop()] for c in chunked(data, 3)))
