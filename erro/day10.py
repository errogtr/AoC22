with open(__file__.replace(".py", "_data")) as f:
    data = f.read().splitlines()


# PART 1
register = 1
cycle = 1
i = 0
signal_strength = 0
first = True
while i < len(data):
    if (cycle - 20) % 40 == 0:
        signal_strength += cycle * register
    if data[i][:4] == "addx":
        if first:
            i -= 1
        else:
            register += int(data[i][4:])
        first = not first
    cycle += 1
    i += 1

print(signal_strength)

