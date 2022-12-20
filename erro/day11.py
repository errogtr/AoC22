from typing import List, Callable
import re
from math import prod
from copy import deepcopy


class Monkey:
    def __init__(self, note_lines: List[str]):
        self.items = self.get_items(note_lines[1])
        self.op = self.get_operation(note_lines[2])
        self.div = self.get_dividend(note_lines[3])
        self.test = self.get_test(" ".join(note_lines[4:]))
        self.business = 0

    @staticmethod
    def get_items(line: str) -> List[int]:
        return [int(x) for x in re.findall(r"\d+", line)]

    @staticmethod
    def get_operation(line: str) -> Callable[[int], int]:
        operation, operand = re.search(r"([+*])\s(old|\d+)", line).group(1, 2)
        if operand.isdigit():
            if operation == "*":
                return lambda x: int(operand) * x
            else:
                return lambda x: int(operand) + x
        else:
            return lambda x: x ** 2

    @staticmethod
    def get_dividend(line: str) -> int:
        return int(re.search(r"(\d+)", line).group(1))

    def get_test(self, text: str) -> Callable:
        dst_monkeys = [int(x) for x in re.findall(r"\d", text)]
        return lambda x: dst_monkeys[0] if x % self.div == 0 else dst_monkeys[1]


def game(monkeys: List[Monkey], rounds: int, lcm: int, reduce_worry_lvl: bool = False):
    for _ in range(rounds):
        for monkey in monkeys:
            monkey.items = [monkey.op(item) % lcm for item in monkey.items]
            if reduce_worry_lvl:
                monkey.items = [item // 3 for item in monkey.items]
            monkey.business += len(monkey.items)
            while monkey.items:
                item = monkey.items.pop(0)
                monkeys[monkey.test(item)].items.append(item)
    return prod(sorted(m.business for m in monkeys)[-2:])


with open(__file__.replace(".py", "_data")) as f:
    monkeys_start = [Monkey(note.split("\n")) for note in f.read().split("\n\n")]

LCM = prod(x.div for x in monkeys_start)

monkeys = deepcopy(monkeys_start)
print(game(monkeys, 20, LCM, True))

monkeys = deepcopy(monkeys_start)
print(game(monkeys, 10000, LCM))
