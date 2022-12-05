stacksprep = []
stacks = []

with open("input.txt", "r") as file:
    complete = False
    for line in file:
        if not complete and line != "\n":
            stacksprep.append(line)

        elif not complete and line == "\n":
            for char in stacksprep[-1]:
                if char.isdigit():
                    stack = []
                    for stackprep in stacksprep[:-1]:
                        stack.insert(0, stackprep[stacksprep[-1].index(char)])

                    stacks.append(stack)

            stacks = [[char for char in stack if char != " "] for stack in stacks]

            complete = True

        else:
            parts = [int(char) for char in line.strip().split(" ") if char.isdigit()]

            for i in range(parts[0]):
                stacks[parts[2] - 1].append(stacks[parts[1] - 1].pop())

print("".join([stack[-1] for stack in stacks if len(stack) > 0]))
