from more_itertools import chunked


if __name__ == "__main__":
    with open(__file__.replace(".py", "_data")) as f:
        data = [x.strip() for x in f.readlines()]

    # PART 1
    print(sum((y := ord(set.intersection(*map(set, chunked(x, len(x) // 2))).pop())) - (96 if y > ord("Z") else 38) for x in data))

    # PART 2
    print(sum((y := ord(set.intersection(*map(set, c)).pop())) - (96 if y > ord("Z") else 38) for c in chunked(data, 3)))