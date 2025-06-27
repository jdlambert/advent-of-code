import sys
import re

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

mul = re.compile("mul\((\d+),(\d+)\)")
muls = mul.findall(data)

p1 = sum(int(mul[0]) * int(mul[1]) for mul in muls)
p2 = 0

print(f"Part one: {p1}")
print(f"Part two: {p2}")
