sum = 0

with open("Input.txt", "r") as file:
    group = []
    for line in file:
        group.append(line.strip())

        if len(group) == 3:
            for char in group[0]:
                if char in group[1] and char in group[2]:
                    sum += ord(char.lower()) - 96

                    if char.isupper():
                        sum += 26

                    group = []
                    break

print(sum)
