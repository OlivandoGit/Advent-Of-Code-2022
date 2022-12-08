trees = [[int(x) for x in line.strip()] for line in open("Input.txt", "r")]

scores = []

for y in range(1, len(trees) - 1):
    for x in range(1, len(trees[y]) - 1):
        sights = [trees[y][: x][::-1], trees[y][x + 1 :], [line2[x] for line2 in trees[: y]][::-1], [line2[x] for line2 in trees[y + 1 :]]]

        total = 0
        for i, sight in enumerate(sights):
            for height in sight:
                if trees[y][x] > height:
                    total += 1

                else:
                    total += 1
                    break

            sights[i] = total
            total = 0

        total = 1
        for s in sights:
            total *= s

        scores.append(total)

print(max(scores))
