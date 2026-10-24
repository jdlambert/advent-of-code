import sys
from collections import Counter

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

left, right = [], []

for line in data.splitlines():
    L, R = line.split('   ')
    left.append(int(L))
    right.append(int(R))

p1 = sum(abs(L - R) for L, R in zip(sorted(left), sorted(right)))

counts = Counter(right)

p2 = sum(L * counts[L] for L in left)

print(f"Part one: {p1}")
print(f"Part two: {p2}")
