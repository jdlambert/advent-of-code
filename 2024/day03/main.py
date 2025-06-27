import sys
import re

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

pattern = re.compile(
    r"(?P<mul>mul\(\s*(?P<n>\d+)\s*,\s*(?P<m>\d+)\s*\))"
    r"|(?P<do>do\(\))"
    r"|(?P<dont>don't\(\))"
)

muls = []
do = True

for match in pattern.finditer(data):
    match_type = match.lastgroup
    if match_type == "mul":
        n = int(match.group('n'))
        m = int(match.group('m'))
        muls.append((n, m, do))
    else:
        do = match_type == "do"

p1 = sum(n * m for m, n, _ in muls)
p2 = sum(n * m for m, n, d in muls if d)

print(f"Part one: {p1}")
print(f"Part two: {p2}")
