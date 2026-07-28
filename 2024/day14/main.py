import sys
from functools import reduce
import re

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

num_re = re.compile(r"(-?\d+)")
robots = [[int(n) for n in num_re.findall(line)] for line in data.splitlines()]
quads = [0] * 4

H = 7 if "x" in sys.argv else 103
W = 11 if "x" in sys.argv else 101
H_SPLIT = (H - 1) // 2
W_SPLIT = (W - 1) // 2

for x, y, dx, dy in robots:
    final_x = (x + 100*dx) % W
    final_y = (y + 100*dy) % H
    if final_x == W_SPLIT or final_y == H_SPLIT:
        continue
    q = (1 if final_x > W_SPLIT else 0) + (2 if final_y > H_SPLIT else 0)
    quads[q] += 1

def print_at_t(t):
    robots_at_t = {((x + t*dx) % W, (y + t*dy) % H) for x, y, dx, dy in robots}
    for y in range(H):
        for x in range(W):
            print("0" if (x, y) in robots_at_t else ".", end="")
        print("")

min_counts = float("inf")
min_t = 0
for t in range(10000):
    rows, cols = set(), set()

    row_counts = [0]*len(robots)
    for x, y, dx, dy in robots:
        rows.add((y + t*dy) % H)
        cols.add((x + t*dx) % W)
    if len(rows) + len(cols) < min_counts:
        min_counts = len(rows) + len(cols)
        min_t = t

p1 = reduce(lambda acc, x: acc * x, quads, 1)
print_at_t(min_t)
p2 = min_t

print(f"Part one: {p1}")
print(f"Part two: {p2}")
