from itertools import zip_longest

def compare(left, right):
    zipped = zip_longest(left, right, fillvalue = None)

    for z in zipped:
        l, r = z
        result = None

        if isinstance(l, int) and isinstance(r, int):
            if l < r:
                return True
            if l > r:
                return False

        elif isinstance(l, list) and isinstance(r, list):
            result = compare(l, r)

        elif isinstance(l, int) and isinstance(r, list):
            result = compare([l], r)
        elif isinstance(l, list) and isinstance(r, int):
            result = compare(l, [r])

        elif l == None:
            return True
        elif r == None:
            return False

        if result != None:
            return result

with open("Input.txt", "r") as f:
    packets = [line.strip() for line in f if line != "\n"]

packets = [eval(p) for p in packets]
packets.extend([[[2]], [[6]]])

for i in range(len(packets)):
    for j in range(len(packets)):
        if compare(packets[i], packets[j]):
            temp = packets[j]
            packets[j] = packets[i]
            packets[i] = temp

print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))
