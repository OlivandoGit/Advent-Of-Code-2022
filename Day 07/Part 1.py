def getValue(sizes, evaluated, dir):
    total = 0

    for k in dir.keys():
        if dir[k] == "dir":
            ret, evaluated = getValue(sizes, evaluated, sizes[k])
            evaluated[k] = ret

            total += ret

        else:
            total += dir[k]

    return total, evaluated

sizes = {}
current = ""

with open("Input.txt", "r") as file:
    for line in file:
        parts = line.strip().split(" ")

        if parts[1] == "cd":
            if parts[2] == "..":
                current = "/".join(current.split("/")[:-1])

                if current == "":
                    current = "/"

            elif parts[2] == "/":
                current = "/"
            else:
                if len(current) > 1:
                    current += "/" + parts[2]
                else:
                    current += parts[2]

        if parts[0] != "$":
            if current not in sizes.keys():
                sizes[current] = {}

            if parts[0].isdigit():
                parts[0] = int(parts[0])

            path = current

            if len(path) > 1:
                path += "/" + parts[1]
            else:
                path += parts[1]

            sizes[current][path] = parts[0]

evaluated = {}

ret, evaluated = getValue(sizes, evaluated, sizes["/"])

evaluated["/"] = ret

total = 0

for v in evaluated.values():
    if v < 100000:
        total += v

print(total)
