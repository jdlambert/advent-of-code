import sys

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

grid = set()
start = None
end = None
for i, line in enumerate(data.splitlines()):
    for j, c in enumerate(line):
        if c in 'SE.':
            grid.add((i, j))
            if c == 'S':
                start = i, j
            if c == 'E':
                end = i, j

def long_neighbors(i, j, allowed):
    for di in range(-allowed, allowed + 1):
        rem = allowed - abs(di)
        for dj in range(-rem, rem + 1):
            d = abs(di) + abs(dj)
            if d == 0:
                continue
            if (i + di, j + dj) in grid:
                yield (i + di, j + dj, d)

picoseconds = {}
frontier = [(0, start)]
while frontier:
    ps, (ci, cj) = frontier.pop()
    if (ci, cj) in picoseconds:
        continue
    picoseconds[(ci, cj)] = ps
    for ni, nj, _ in long_neighbors(ci, cj, 1):
        frontier.append((ps + 1, (ni, nj)))

def cheats(threshold, allowed):
    total = 0
    for i, j in grid:
        ns = long_neighbors(i, j, allowed)
        savings = [picoseconds[(ni, nj)] - picoseconds[(i, j)] - d for (ni, nj, d) in ns]
        total += len([saving for saving in savings if saving >= threshold])
    return total

p1 = cheats(100, 2)
p2 = cheats(100, 20)

print(picoseconds[end])
print(f"Part one: {p1}")
print(f"Part two: {p2}")
