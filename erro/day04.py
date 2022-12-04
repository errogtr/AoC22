with open(__file__.replace(".py", "_data")) as f:
    data = [x.split(",") for x in f.readlines()]

# PART 1
counts = 0
for range_1, range_2 in data:
    section_1 = range_1.split("-")
    section_2 = range_2.split("-")
    set_1 = set(range(int(section_1[0]), int(section_1[1]) + 1))
    set_2 = set(range(int(section_2[0]), int(section_2[1]) + 1))
    if set_1 <= set_2 or set_2 <= set_1:
        counts += 1
print(counts)

# PART 2
counts = 0
for range_1, range_2 in data:
    section_1 = range_1.split("-")
    section_2 = range_2.split("-")
    set_1 = set(range(int(section_1[0]), int(section_1[1]) + 1))
    set_2 = set(range(int(section_2[0]), int(section_2[1]) + 1))
    if set_1 & set_2:
        counts += 1
print(counts)
