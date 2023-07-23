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
    pairs = [pair.strip().split("\n") for pair in f.read().split("\n\n")]

pairs = [[eval(p) for p in pair] for pair in pairs]

total = 0
for i, pair in enumerate(pairs):
    if compare(pair[0], pair[1]):
        total += i + 1

print(total)
