from itertools import groupby


if __name__ == "__main__":
    with open(__file__.replace(".py", "_data")) as f:
        data = f.readlines()

    calories_per_elf = [sum(map(int, g)) for k, g in groupby(data, key=lambda x: x != "\n") if k]

    # PART 1
    print(max(calories_per_elf))

    # PART 2
    print(sum(sorted(calories_per_elf)[-3:]))
