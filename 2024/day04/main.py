import sys

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

grid = data.splitlines()
N = len(grid)
M = len(grid[0])

def xmas_count_dir(i, j, di, dj, word):
    if not word:
        return 1
    if not (0 <= i < N and 0 <= j < M):
        return 0
    if word[0] != grid[i][j]:
        return 0
    return xmas_count_dir(i + di, j + dj, di, dj, word[1:])

def xmas_count(i, j):
    total = 0
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if di == 0 and dj == 0:
                continue
            total += xmas_count_dir(i, j, di, dj, "XMAS")
    return total

def is_ms(a, b):
    return a == 'M' and b == 'S' or a == 'S' and b == 'M'

def x_mas(i, j):
    u = grid[i - 1]
    d = grid[i + 1]
    ul, ur = u[j - 1], u[j + 1]
    dl, dr = d[j - 1], d[j + 1]
    return grid[i][j] == 'A' and is_ms(ul, dr) and is_ms(ur, dl)
        
p1 = sum(xmas_count(i, j) for i in range(N) for j in range(M))
p2 = len([(i, j) for i in range(1, N - 1) for j in range(1, M - 1) if x_mas(i, j)])

print(f"Part one: {p1}")
print(f"Part two: {p2}")
