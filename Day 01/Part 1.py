elves = []

with open("Input.txt", "r") as f:
    total = 0
    for line in f:
        if line == "\n":
            elves.append(total)
            total = 0

        else:
            total += int(line.strip())

print(max(elves))
