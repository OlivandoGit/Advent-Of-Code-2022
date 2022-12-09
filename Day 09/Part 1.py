head = [0, 0]
tail = [0, 0]

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

            if head[0] - tail[0] == 2:
                tail[0] += 1
                tail[1] = head[1]

            elif head[0] - tail[0] == -2:
                tail[0] -= 1
                tail[1] = head[1]

            elif head[1] - tail[1] == 2:
                tail[1] += 1
                tail[0] = head[0]

            elif head[1] - tail[1] == -2:
                tail[1] -= 1
                tail[0] = head[0]

            if tail not in visited:
                visited.append(tail[:])

print(len(visited))
