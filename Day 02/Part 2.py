wins = {"S": "R", "R": "P", "P": "S"}
loses = {v: k for k, v in wins.items()}

translation = {"A": "R", "B": "P", "C": "S"}

points = {"R": 1, "P": 2, "S": 3}

score = 0
with open("Input.txt", "r") as file:
    for line in file:
        line = list(line.strip().replace(" ", ""))
        line[0] = translation.get(line[0])

        if line[1] == "X":
            score += points.get(loses.get(line[0]))
        elif line[1] == "Y":
            score += 3 + points.get(line[0])
        else:
            score += 6 + points.get(wins.get(line[0]))

print(score)
