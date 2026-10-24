import sys
import collections

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

byte_locs = []
for line in data.strip().splitlines():
    a, b = line.split(",")
    byte_locs.append((int(a), int(b)))

H = W = 71

corrupted = set()
for i, j in byte_locs[:1024]:
    corrupted.add((i, j))

def neighbors(i, j):
    if i + 1 < H and not (i + 1, j) in corrupted: yield (i + 1, j)
    if i - 1 > -1 and not (i - 1, j) in corrupted: yield (i - 1, j)
    if j + 1 < W and not (i, j + 1) in corrupted: yield (i, j + 1)
    if j - 1 > -1 and not (i, j - 1) in corrupted: yield (i, j - 1)

p1 = 0
frontier = collections.deque([(0, (0, 0))])
visited = set()
while frontier:
    steps, (i, j) = frontier.popleft()
    if (i, j) in visited:
        continue
    visited.add((i, j))
    if (i, j) == (H - 1, W - 1):
        p1 = steps
        break
    for ni, nj in neighbors(i, j):
        frontier.append((steps + 1, (ni, nj)))

p2 = 0

class CorruptedSets:
    def __init__(self, H, W):
        self.H = H
        self.W = W
        self.corrupted = set()
        self.parent = {}
        self.rank = {}
        self.L = (-1, 0)
        self.U = (-2, 0)
        self.R = (-3, 0)
        self.D = (-4, 0)
        for node in (self.L, self.U, self.R, self.D):
            self.parent[node] = node
            self.rank[node] = 0

    def add(self, node):
        if node in self.parent:
            return
        self.parent[node] = node
        self.rank[node] = 0

    def find(self, node):
        while self.parent[node] != node:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1

    def connected(self, a, b):
        return self.find(a) == self.find(b)

    def add_corrupted(self, i, j):
        if (i, j) in self.corrupted:
            return
        self.corrupted.add((i, j))
        self.add((i, j))

        if j == 0:
            self.union((i, j), self.L)
        if i == 0:
            self.union((i, j), self.U)
        if j == self.W - 1:
            self.union((i, j), self.R)
        if i == self.H - 1:
            self.union((i, j), self.D)

        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                if di == 0 and dj == 0:
                    continue
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= self.H or nj < 0 or nj >= self.W:
                    continue
                if (ni, nj) in self.corrupted:
                    self.union((i, j), (ni, nj))

    def blocks_path(self):
        return (
            self.connected(self.L, self.U)
            or self.connected(self.L, self.R)
            or self.connected(self.U, self.D)
            or self.connected(self.R, self.D)
        )

sets = CorruptedSets(H, W)
for i, j in byte_locs:
    sets.add_corrupted(i, j)
    if sets.blocks_path():
        p2 = f"{i},{j}"
        break

print(f"Part one: {p1}")
print(f"Part two: {p2}")
