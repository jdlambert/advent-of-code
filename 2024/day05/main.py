import sys
from collections import defaultdict

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

rules, updates = data.split("\n\n")

grid = defaultdict(set)
for line in rules.splitlines():
    L, R = line.split("|")
    grid[L].add(R)

p1 = 0
updates = updates.splitlines()
bad_updates = []
for update in updates:
    split_update = update.split(',')
    if all(r0 not in grid[r1]
           for i, r0 in enumerate(split_update)
           for r1 in split_update[i + 1:]
        ):
         p1 += int(split_update[len(split_update) // 2])
    else:
        bad_updates.append(split_update)
            
p2 = 0
for split_update in bad_updates:
    for i in range(len(split_update)):
        for j in range(i, len(split_update)):
            if split_update[i] in grid[split_update[j]]:
                split_update[i], split_update[j] = split_update[j], split_update[i]
    p2 += int(split_update[len(split_update) // 2])

print(f"Part one: {p1}")
print(f"Part two: {p2}")
