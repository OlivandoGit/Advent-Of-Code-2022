trees = [[int(x) for x in line.strip()] for line in open("Input.txt", "r")]

seen = 0

for y in range(1, len(trees) - 1):
    for x in range(1, len(trees[y]) - 1):
        maxes = [max(trees[y][: x]), max(trees[y][x + 1 :]), max([line2[x] for line2 in trees[: y]]), max(line2[x] for line2 in trees[y + 1 :])]

        for m in maxes:
            if trees[y][x] > m:
                seen += 1
                break

print(seen + (4 * len(trees)) - 4)
