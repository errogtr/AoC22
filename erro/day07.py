from collections import defaultdict


def get_size(tree, parent, elements, size=0):
    for info, name in elements:
        if info == "dir":
            dirname = parent + "/" + name
            size = get_size(tree, dirname, tree[dirname], size)
        else:
            size += int(info)
    return size


with open(__file__.replace(".py", "_data")) as f:
    data = [line.strip() for line in f.readlines()]


current = list()
tree = defaultdict(list)
for line in data:
    if line == "$ ls":
        continue
    info, name = line.rsplit(" ", 1)
    if info == "$ cd":
        match name:
            case "..": current.pop()
            case "/": current.append("/home")
            case other: current.append(name)
    else:
        tree["/".join(current)].append((info, name))

# PART 1
sizes = [get_size(tree, parent, elements) for parent, elements in tree.items()]
print(sum(s for s in sizes if s <= 100000))

# PART 2
unused_space = 70000000 - sizes[0]
print(min(s for s in sizes if unused_space + s >= 30000000))
