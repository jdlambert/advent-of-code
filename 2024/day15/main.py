import sys

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

grid_data, moves = data.split("\n\n")
grid = {}
robot = None, None
for i, line in enumerate(grid_data.splitlines()):
    for j, c in enumerate(line):
        if c == '@':
            robot = i, j
        grid[(i, j)] = c
H, W = i + 1, j + 1

def attempt_move(pi, pj, di, dj):
    start = (pi, pj)
    target = (pi + di, pj + dj)
    if grid[target] == 'O':
        attempt_move(pi + di, pj + dj, di, dj)
    if grid[target] == '.':
        grid[start], grid[target] = '.', grid[start]
        return target
    return start

move_map = {
    ">": (0, 1),
    "<": (0, -1),
    "v": (1, 0),
    "^": (-1, 0),
}

for command in moves:
    if command == "\n":
        continue
    move = move_map[command]
    robot = attempt_move(*robot, *move)

for i in range(H):
    for j in range(W):
        print(grid[(i, j)], end="")
    print()

p1 = 0
for (i, j), c in grid.items():
    if c == 'O':
        p1 += 100*i + j

grid = {}
robot = None, None
for i, line in enumerate(grid_data.splitlines()):
    for j, c in enumerate(line):
        j = 2*j
        if c == '@':
            robot = i, j
            grid[(i, j)] = '@'
            grid[(i, j + 1)] = '.'
        elif c == 'O':
            grid[(i, j)] = '['
            grid[(i, j + 1)] = ']'
        else:
            grid[(i, j)] = c
            grid[(i, j + 1)] = c

def attempt_move_ew(pi, pj, di, dj):
    start = (pi, pj)
    target = (pi + di, pj + dj)
    if grid[target] in '[]':
        attempt_move_ew(pi + di, pj + dj, di, dj)
    if grid[target] == '.':
        grid[start], grid[target] = '.', grid[start]
        return target
    return start

def attempt_move_ns(pi, pj, di, dj):
    start = (pi, pj)
    target = (pi + di, pj + dj)
    if grid[target] in '[]':
        attempt_move_rock_ns(*target, di, dj)
    if grid[target] == '.':
        grid[start], grid[target] = '.', grid[start]
        return target
    return start

def attempt_move_rock_ns(pi, pj, di, dj):
    if not can_move_rock_ns(pi, pj, di, dj):
        return
    start = (pi, pj)
    target = (pi + di, pj + dj)
    bound = (pi, pj + 1) if grid[start] == '[' else (pi, pj - 1)
    bound_target = (bound[0] + di, bound[1] + dj)
    if grid[target] in '[]':
        attempt_move_rock_ns(*target, di, dj)
    if grid[bound_target] in '[]':
        attempt_move_rock_ns(*bound_target, di, dj)
    if grid[target] == '.' and grid[bound_target] == '.':
        grid[start], grid[target] = '.', grid[start]
        grid[bound], grid[bound_target] = '.', grid[bound]

def can_move_rock_ns(pi, pj, di, dj):
    start = (pi, pj)
    target = (pi + di, pj + dj)
    bound = (pi, pj + 1) if grid[start] == '[' else (pi, pj - 1)
    bound_target = (bound[0] + di, bound[1] + dj)
    if grid[target] == '#' or grid[bound_target] == '#':
        return False
    if grid[target] in '[]':
        if not can_move_rock_ns(*target, di, dj):
            return False
    if grid[bound_target] in '[]':
        if not can_move_rock_ns(*bound_target, di, dj):
            return False
    return True

for command in moves:
    if command == "\n":
        continue
    move = move_map[command]
    robot = attempt_move_ew(*robot, *move) if command in '<>' else attempt_move_ns(*robot, *move)

p2 = 0

for (i, j), c in grid.items():
    if c == '[':
        p2 += 100*i + j

for i in range(H):
    for j in range(W*2 - 1):
        print(grid[(i, j)], end="")
    print()

print(f"Part one: {p1}")
print(f"Part two: {p2}")
