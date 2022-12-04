total = 0

with open("Input.txt", "r") as file:
    for line in file:
        line = line.strip().split(",")

        for i, group in enumerate(line):
            line[i] = [int(j) for j in group.split("-")]

        for i, group in enumerate(line):
            group2 = line[(i + 1) % 2]
            
            if group[0] >= group2[0] and group[0] <= group2[1] or group[1] <=  group2[1] and group[1] >= group2[0]:
                total += 1
                break

print(total)
