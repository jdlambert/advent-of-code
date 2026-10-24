import sys
import heapq

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

grid = {}
pos = None
dir = 0, 1
for i, line in enumerate(data.splitlines()):
    for j, c in enumerate(line):
        if c != '#':
            if c == 'S':
                pos = i, j
            grid[(i, j)] = c
H, W = 1 + i, 1 + j

def rot(didj):
    return [(0, 1), (0, -1)] if didj[1] == 0 else [(1, 0), (-1, 0)]

def neighbors(i, j, di, dj):
    if (i + di, j + dj) in grid:
        yield (1, i + di, j + dj, di, dj)
    for new_dir in rot((di, dj)):
        yield (1000, i, j, *new_dir)

p1 = 0
p2 = 0

frontier = [(0, *pos, *dir, set())]
visited = dict()
while frontier:
    score, i, j, di, dj, pathset = heapq.heappop(frontier)
    if (i, j, di, dj) in visited and visited[(i, j, di, dj)] < score:
        continue
    visited[(i, j, di, dj)] = score
    pathset = pathset.union({(i, j)})
    if grid[(i, j)] == 'E':
        p1 = score 
        p2set = pathset
        print(score)
        for f in frontier[:25]:
            print(f)
        while frontier[0][0] == score:
            _, ni, nj, _, _, pathset = heapq.heappop(frontier)
            if (ni, nj) == (i, j):
                print(pathset)
                p2set.update(pathset)
        p2 = len(p2set)
        break
    for dscore, i, j, di, dj in neighbors(i, j, di, dj):
        heapq.heappush(frontier, (score + dscore, i, j, di, dj, pathset))

for i in range(H):
    for j in range(W):
        if (i, j) in pathset:
            print("O", end="")
        elif (i, j) in grid:
            print(".", end="")
        else:
            print("#", end="")
    print()

print(f"Part one: {p1}")
print(f"Part two: {p2}")
