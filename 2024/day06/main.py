import sys

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

lines = data.splitlines()
N, M = len(lines), len(lines[0])

obstacles = set()
start_pos = None
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if '^' == c:
            start_pos = i, j
        if '#' == c:
            obstacles.add((i, j))

# the search space can be significantly reduceed, only checking spaces that were visited,
# and starting the search immediately before collision
def does_loop(oi, oj):
    if (oi, oj) == start_pos or (oi, oj) in obstacles:
        return False

    di, dj = -1, 0
    i, j = start_pos
    visited = set()
    while 0 <= i < N and 0 <= j < M:
        while (i + di, j + dj) in obstacles or (i + di, j + dj) == (oi, oj):
            di, dj = dj, -di
        pos_dir = i, j, di, dj
        if pos_dir in visited:
            return True
        visited.add(pos_dir)
        i += di
        j += dj
    return False

di, dj = -1, 0
visited = set()
loopable = set()
i, j = start_pos
while 0 <= i < N and 0 <= j < M:
    visited.add((i, j))
    if (i + di, j + dj) in obstacles:
        di, dj = dj, -di
    i, j = i + di, j + dj

p1 = len(visited)
print(f"Part one: {p1}")
p2 = len([(i, j) for i in range(N) for j in range(M) if does_loop(i, j)])
print(f"Part two: {p2}")
