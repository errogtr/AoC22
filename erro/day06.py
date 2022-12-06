def get_message(data: str, length: int):
    for idx, c in enumerate(data[:-length + 1]):
        if len(set(data[idx:idx + length])) == length:
            return idx + length


with open(__file__.replace(".py", "_data")) as f:
    data = f.read()


# PART 1
print(get_message(data, length=4))

# PART 2
print(get_message(data, length=14))
