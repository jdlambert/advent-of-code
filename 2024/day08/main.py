import sys
from collections import defaultdict

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

lines = data.splitlines()
N, M = len(lines), len(lines[0])

antennae = defaultdict(list)
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c != '.':
            antennae[c].append((i, j))

def in_bounds(i, j):
    return 0 <= i < N and 0 <= j < M

def antinodes(i0, j0, i1, j1):
    nodes = set()
    a0i = i0 + (i0 - i1)
    a0j = j0 + (j0 - j1)
    nodes.add((a0i, a0j))

    a1i = i1 + (i1 - i0)
    a1j = j1 + (j1 - j0)
    nodes.add((a1i, a1j))
    return {(i, j) for i, j in nodes if in_bounds(i, j)}

def more_antinodes(i0, j0, i1, j1):
    nodes = set()
    di = i0 - i1
    dj = j0 - j1
    ai, aj = i0, j0
    while in_bounds(ai, aj):
        nodes.add((ai, aj))
        ai -= di
        aj -= dj
    ai, aj = i0, j0
    while in_bounds(ai, aj):
        nodes.add((ai, aj))
        ai += di
        aj += dj
    return nodes

def antinode_set(points, a=antinodes):
    nodes = set()
    for i, p0 in enumerate(points):
        for p1 in points[i + 1:]:
            nodes |= a(*p0, *p1)
    return nodes

full_set = set()
more_full_set = set()
for points in antennae.values():
    full_set |= antinode_set(points)
    more_full_set |= antinode_set(points, a=more_antinodes)

for i in range(N):
    for j in range(M):
        if lines[i][j] != ".":
            print(lines[i][j], end="")
        elif (i, j) in full_set:
            print('#', end="")
        else:
            print('.', end="")
    print()

p1 = len(full_set)
p2 = len(more_full_set)

print(f"Part one: {p1}")
print(f"Part two: {p2}")
