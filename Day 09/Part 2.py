head = [0, 0]
tails = [[0, 0] for i in range(9)]

visited = []
with open("Input.txt", "r") as file:
    for line in file:
        parts = line.strip().split()
        parts[1] = int(parts[1])

        for i in range(parts[1]):
            if parts[0] == "U":
                head[1] += 1
            elif parts[0] == "D":
                head[1] -= 1
            elif parts[0] == "R":
                head[0] += 1
            elif parts[0] == "L":
                head[0] -= 1

            for i, tail in enumerate(tails):
                if i == 0:
                    prev = head
                else:
                    prev = tails[i - 1]

                dx = 0
                dy = 0

                if prev[0] - tail[0] == 2:
                    dx += 1

                    if prev[1] > tail[1]:
                        dy += 1
                    elif prev[1] < tail[1]:
                        dy -= 1

                elif prev[0] - tail[0] == -2:
                    dx -= 1

                    if prev[1] > tail[1]:
                        dy += 1
                    elif prev[1] < tail[1]:
                        dy -= 1

                elif prev[1] - tail[1] == 2:
                    dy += 1

                    if prev[0] > tail[0]:
                        dx += 1
                    elif prev[0] < tail[0]:
                        dx -= 1

                elif prev[1] - tail[1] == -2:
                    dy -= 1

                    if prev[0] > tail[0]:
                        dx += 1
                    elif prev[0] < tail[0]:
                        dx -= 1

                tails[i] = [tail[0] + dx, tail[1] + dy]

            if tails[i] not in visited:
                visited.append(tails[i][:])

print(len(visited))
