sum = 0

with open("Input.txt", "r") as file:
    for line in file:
        line = line.strip()

        for char in line[:len(line) // 2]:
            if char in line[len(line) // 2 :]:
                sum += ord(char.lower()) - 96

                if char.isupper():
                    sum += 26

                break

print(sum)
