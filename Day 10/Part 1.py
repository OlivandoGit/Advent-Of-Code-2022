clock = 1
reg = 1

signals = 0
with open("Input.txt", "r") as file:
    for line in file:
        parts = line.strip().split()

        for i in range(len(parts)):
            if clock in [20, 60, 100, 140, 180, 220]:
                signals += clock * reg

            clock += 1

        if parts[0] != "noop":
            parts[1] = int(parts[1])
            reg += parts[1]

print(signals)
