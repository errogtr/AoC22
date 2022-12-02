STRATEGY_1 = {
    "A X": 1 + 3,
    "A Y": 2 + 6,
    "A Z": 3 + 0,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 1 + 6,
    "C Y": 2 + 0,
    "C Z": 3 + 3
}

STRATEGY_2 = {
    "A X": 3 + 0,
    "A Y": 1 + 3,
    "A Z": 2 + 6,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 2 + 0,
    "C Y": 3 + 3,
    "C Z": 1 + 6
}

if __name__ == "__main__":
    with open(__file__.replace(".py", "_data")) as f:
        rounds = [line.strip() for line in f.readlines()]

    # PART 1
    print(sum(STRATEGY_1[x] for x in rounds))

    # PART 2
    print(sum(STRATEGY_2[x] for x in rounds))
