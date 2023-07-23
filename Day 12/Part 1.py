class node:
    def __init__(self, x, y, height):
        self.x = x
        self.y = y
        self.height = height
        self.previous = None
        self.distance = -1

    def checkneighbours(self, heightmap):
        neighbours = []

        tocheck = [[self.x, self.y - 1], [self.x, self.y + 1], [self.x - 1, self.y], [self.x + 1, self.y]]
        for pos in tocheck:
            if pos[0] not in range(0, len(heightmap[0])):
                continue

            if pos[1] not in range(0, len(heightmap)):
                continue

            neighbour = heightmap[pos[1]][pos[0]]
            if neighbour.height - self.height > 1:
                continue

            if neighbour.distance == -1 or neighbour.distance > self.distance + 1:
                neighbour.distance = self.distance + 1
                neighbour.previous = self

                neighbours.append(neighbour)

        return neighbours

heightmap = []
with open("Input.txt", "r") as f:
    for y, line in enumerate(f):
        row = [node(x, y, ord(char) - 97) for x, char in enumerate(line.strip())]
        heightmap.append(row)

start = None
end = None
for y, row in enumerate(heightmap):
    for x, node in enumerate(row):
        if node.height == -14:
            node.height = 0
            node.distance = 0
            start = node

        elif node.height == -28:
            node.height = 25
            end = node

tocheck = [start]
checked = []
while len(tocheck) > 0:
    current = tocheck.pop(0)
    tocheck2 = current.checkneighbours(heightmap)
    checked.append(current)

    tocheck.extend([node for node in tocheck2 if node not in checked])

print(end.distance)
