with open("Input.txt", "r") as file:
    line = file.read().strip()

    group = []
    for i, char in enumerate(line):
        if len(group) < 14:
            group.append(char)

        if len(group) == 14:
            found = True
            for char2 in group:
                if group.count(char2) > 1:
                    found = False

            if found:
                print(i + 1)
                break

            group = group[1:]
