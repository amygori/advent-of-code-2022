import sys
from pathlib import Path
import re
import pprint

ROUNDS = 20


def find_out_monkey_business(input):
    monkeys = parse_input(input)
    for _ in range(ROUNDS):
        round(monkeys)

    activity_levels = sorted([monkey.activity for monkey in monkeys])
    return activity_levels[-1] * activity_levels[-2]


def round(monkeys):
    for monkey in monkeys:
        if len(monkey.items) < 1:
            continue  # skip monkey if no items
        items_copy = monkey.items.copy()
        for idx in range(len(items_copy)):
            # inspect each item
            item = int(items_copy[idx])
            monkey.activity += 1
            # worry level is modified based on operation
            if "old" in monkey.operation:
                new_level = eval(f"{item} {monkey.operation[0]} {item}")
            else:
                new_level = eval(f"{item} {monkey.operation}")
            # divide level by 3
            item = new_level // 3
            # determine monkey recipient
            target_monkey_idx = monkey.get_target(item)

            target_monkey = monkeys[target_monkey_idx]
            target_monkey.items.append(item)
            # remove item from first monkey
            monkey.items.pop()


class Monkey:
    def __init__(self, num=0, operation="", items=[], divisor=None):
        self.num = num
        self.operation = operation
        self.items = items
        self.divisor = divisor
        self.target_if_true = None
        self.target_if_false = None
        self.activity = 0

    def __repr__(self):
        return f"<Monkey {self.num} op={self.operation} items={self.items} divisor={self.divisor} target_T={self.target_if_true} target_F={self.target_if_false} activity={self.activity}>"

    def set_target_monkey(self, test_result, target):
        if test_result == "true":
            self.target_if_true = target
        else:
            self.target_if_false = target

    def get_target(self, item):
        if item % self.divisor:
            return self.target_if_false
        else:
            return self.target_if_true


def parse_input(input):
    monkeys = []
    current_monkey = None
    for line in input:
        line = line.strip()
        match re.match(r"^\w*", line).group():
            case "Monkey":
                # create monkey
                current_monkey = Monkey(num=line[-2:-1])
                monkeys.append(current_monkey)
                monkey_index = monkeys.index(current_monkey)
            case "Operation":
                # get the operations at the end of the line
                op = re.search(r"=(\B\W\w*\s)(\W\s\S*)", line).group(2)
                current_monkey.operation = op
            case "Starting":
                items = re.findall(r"([0-9]+)", line)
                current_monkey.items = items
            case "Test":
                condition = line[6:]
                current_monkey.divisor = int(condition[-2:])
            case "If":
                outcome = re.search(r"\s(\w*)", line).group(1)
                current_monkey.set_target_monkey(outcome, int(line[-1:]))
        monkeys[monkey_index] = current_monkey
    return monkeys


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        input = Path.read_text(file).splitlines()
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(find_out_monkey_business(input))
    else:
        raise TypeError("This is not a file")
