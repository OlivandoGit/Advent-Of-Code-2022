total = 0

with open("Input.txt", "r") as file:
    for line in file:
        line = line.strip().split(",")

        for i, group in enumerate(line):
            line[i] = [int(j) for j in group.split("-")]

        for i, group in enumerate(line):
            if group[0] >= line[(i + 1) % 2][0] and group[1] <=  line[(i + 1) % 2][1]:
                total += 1
                break

print(total)
