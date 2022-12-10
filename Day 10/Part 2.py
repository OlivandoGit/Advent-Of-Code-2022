clock = 0
reg = 1

display = [[" " for i in range(40)] for j in range(6)]
with open("Input.txt", "r") as file:
    for line in file:
        parts = line.strip().split()

        for i in range(len(parts)):
            if clock % 40 in range(reg - 1, reg + 2):
                display[clock // 40][clock % 40] = "#"

            clock += 1

        if parts[0] != "noop":
            parts[1] = int(parts[1])
            reg += parts[1]

for d in display:
    print(*d)
