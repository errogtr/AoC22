with open(__file__.replace(".py", "_data")) as f:
    data = f.read()

# PART 1 & 2
for l in [4, 14]:
    print(next(idx + l for idx, c in enumerate(data[:1 - l]) if len(set(data[idx:idx + l])) == l))