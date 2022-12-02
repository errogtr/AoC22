POINTS_DICT = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6
}

if __name__ == "__main__":
    with open(__file__.replace(".py", "_data")) as f:
        rounds = [line.strip() for line in f.readlines()]

    # PART 1
    print(sum(POINTS_DICT[x] for x in rounds))
