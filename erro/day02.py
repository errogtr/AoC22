if __name__ == "__main__":
    with open(__file__.replace(".py", "_data")) as f:
        rounds = [line.split() for line in f.readlines()]

    # PART 1
    print(sum(ord(j) - ord("W") + (ord(j) - ord(i) - 1) % 3 * 3 for i, j in rounds))

    # PART 2
    print(sum(3 * (ord(j) - ord("X")) + (ord(j) + ord(i) - 1) % 3 + 1 for i, j in rounds))
