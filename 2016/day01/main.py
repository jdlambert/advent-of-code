import sys

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

x, y = 0, 0
dx, dy = 0, -1

instructions = [(inst[0], int(inst[1:])) for inst in data.strip().split(", ")]

visited = set()
first_visited_twice = None
for turn, num in instructions:
    dx, dy = (dy, -dx) if turn == "L" else (-dy, dx)
    for i in range(num):
        point = (x + dx*i, y + dy*i)
        if point in visited and first_visited_twice is None:
            first_visited_twice = point
        visited.add(point)
    x, y = x + num*dx, y + num*dy

p1 = abs(x) + abs(y)
p2 = abs(first_visited_twice[0]) + abs(first_visited_twice[1])

print(f"Part one: {p1}")
print(f"Part two: {p2}")
