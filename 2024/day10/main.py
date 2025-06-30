import sys
from collections import defaultdict

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

grid = data.strip().splitlines()
N, M = len(grid), len(grid[0])

def in_bounds(i, j):
    return 0 <= i < N and 0 <= j < M

reachable = defaultdict(set)
ratings = defaultdict(int)

def ripple(i, j):
    value = int(grid[i][j])
    for (di, dj) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = i + di, j + dj
        if in_bounds(ni, nj) and int(grid[ni][nj]) == value - 1:
            reachable[(ni, nj)] |= reachable[(i, j)]
            ratings[(ni, nj)] += 1
            ripple(ni, nj)

for i in range(N):
    for j in range(M):
        if grid[i][j] == '9':
            reachable[(i, j)].add((i, j))
            ripple(i, j)

p1 = sum(len(peaks) for (i, j), peaks in reachable.items() if grid[i][j] == '0')
p2 = sum(rating for (i, j), rating in ratings.items() if grid[i][j] == '0')

print(f"Part one: {p1}")
print(f"Part two: {p2}")
