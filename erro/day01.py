from itertools import groupby


if __name__ == "__main__":
    with open(__file__.replace(".py", "_data")) as f:
        data = [r.strip() for r in f.readlines()]

    calories_per_elf = sorted(sum(map(int, g)) for k, g in groupby(data, key=bool) if k)

    # PART 1
    print(calories_per_elf[-1])

    # PART 2
    print(sum(calories_per_elf[-3:]))
