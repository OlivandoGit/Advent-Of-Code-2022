class Monkey:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.operation = lambda x: x
        self.test = lambda x: x
        self.outcomes = {True: 0, False: 0}
        self.tests = 0

    def turn(self, monkeys):
        for item in self.items[:]:
            self.items.pop(0)
            item = self.operation(item) // 3

            monkeys[self.outcomes[self.test(item)]].items.append(item)
            self.tests += 1

        return monkeys

monkeys = []

with open("Input.txt", "r") as file:
    for line in file:
        line = line.strip().split()

        if "Monkey" in line:
            monkeys.append(Monkey(int(line[1][:-1])))

        elif "Starting" in line:
            monkeys[-1].items = [int(x.strip(",")) for x in line[2:]]

        elif "Operation:" in line:
            if line[-2] == "+" and line[-1] == "old":
                monkeys[-1].operation = lambda x: x + x

            elif line[-2] == "+":
                monkeys[-1].operation = lambda x, y = int(line[-1]): x + y

            elif line[-2] == "*" and line[-1] == "old":
                monkeys[-1].operation = lambda x: x * x

            elif line[-2] == "*":
                monkeys[-1].operation = lambda x, y = int(line[-1]): x * y

        elif "Test:" in line:
            monkeys[-1].test = lambda x, y = int(line[-1]): x % y == 0

        elif "true:" in line:
            monkeys[-1].outcomes[True] = int(line[-1])

        elif "false:" in line:
            monkeys[-1].outcomes[False] = int(line[-1])

for round in range(20):
    for monkey in monkeys:
        monkeys = monkey.turn(monkeys)

inspects = sorted([monkey.tests for monkey in monkeys])

print(inspects[-1] * inspects[-2])
