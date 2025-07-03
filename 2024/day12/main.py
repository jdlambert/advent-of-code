import sys

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

grid = data.splitlines()

visited = set()

def in_bounds(pos):
    i, j = pos
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def cost(pos):
    i, j = pos
    if pos in visited:
        return 0, 0, 0
    visited.add(pos)

    def diff(pos):
        ni, nj = pos
        return not in_bounds(pos) or grid[ni][nj] != grid[i][j]
    
    uu = (i - 1, j)
    ll = (i, j - 1)
    rr = (i, j + 1)
    dl = (i + 1, j - 1)
    dd = (i + 1, j)
    dr = (i + 1, j + 1)
    
    area, perimeter, corners = 1, 0, 0
    my_perimeter = 0
    for np in (uu, ll, rr, dd):
        if in_bounds(np) and not diff(np):
            neighbor_area, neighbor_perimeter, neighbor_corners = cost(np)
            area += neighbor_area
            perimeter += neighbor_perimeter
            corners += neighbor_corners
        else:
            perimeter += 1
            my_perimeter += 1

    for p0, p1 in ((uu, ll), (uu, rr), (ll, dd), (rr, dd)):
        if diff(p0) and diff(p1):
            corners += 1
    
    if len([p for p in(rr, dd, dr) if diff(p)]) == 1:
        corners += 1
    
    if diff(ll) and not diff(dl) and not diff(dd):
        corners += 1

    return area, perimeter, corners


p1 = 0
p2 = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (i, j) not in visited:
            a, p, c = cost((i, j))
            p1 += a * p
            p2 += a * c 

print(f"Part one: {p1}")
print(f"Part two: {p2}")
