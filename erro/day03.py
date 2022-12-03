with open(__file__.replace(".py", "_data")) as f:
    data = [x.strip() for x in f.readlines()]

# PART 1
print(sum((y := ord((set(x[:len(x) // 2]) & set(x[len(x) // 2:])).pop())) - (96 if y > ord("Z") else 38) for x in data))

# PART 2
print(sum((y := ord(set.intersection(*map(set, data[3 * i: 3 * (i + 1)])).pop())) - (96 if y > ord("Z") else 38) for i in range(len(data) // 3)))
