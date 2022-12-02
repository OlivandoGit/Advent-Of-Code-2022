wins = [["S", "R"], ["R", "P"], ["P", "S"]]

translation = {"A": "R", "X": "R", "B": "P", "Y": "P", "C": "S", "Z": "S"}

points = {"R": 1, "P": 2, "S": 3}

score = 0
with open("Input.txt", "r") as file:
    for line in file:
        line = list(line.strip().replace(" ", ""))
        line[0] = translation.get(line[0])
        line[1] = translation.get(line[1])

        if line[0] == line[1]:
            score += 3 + points.get(line[1])
        elif line in wins:
            score += 6 + points.get(line[1])
        else:
            score += points.get(line[1])

print(score)
