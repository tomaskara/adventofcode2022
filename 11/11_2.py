from math import prod

with open('input.txt') as f:
    data = f.read().split("\n\n")


class Monkey:
    def __init__(self, input):
        lines = input.splitlines()
        self.items = [int(x) for x in lines[1].split(": ")[1].split(", ")]
        self.operation = lines[2].split('old ')[-1]
        self.test = int(lines[3].split("by ")[1])
        self.true_monkey = int(lines[4].split("monkey ")[1])
        self.false_monkey = int(lines[5].split("monkey ")[1])
        self.inspections = 0

    def throw(self):
        for item in self.items:
            changed_item = int(eval(str(item) + self.operation, {"old": item}))
            changed_item = changed_item % supermodulo
            if changed_item % self.test == 0:
                monkeys[self.true_monkey].items.append(changed_item)
            else:
                monkeys[self.false_monkey].items.append(changed_item)
            self.inspections += 1
        self.items = []


monkeys = []
for monkey_data in data:
    monkeys.append(Monkey(monkey_data))

for i in range(0,10000):
    supermodulo = prod(monkey.test for monkey in monkeys)
    for monkey in monkeys:
        monkey.throw()

inspections = sorted([monkey.inspections for monkey in monkeys], reverse=True)
print(inspections[0] * inspections[1])


