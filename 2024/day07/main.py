import sys

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

candidates = []
for line in data.splitlines():
    total, operands = line.split(":")
    int_ops = [int(op) for op in operands.strip().split(" ")]
    candidates.append((int(total), int_ops))

def concat_two(seq):
    return int("".join(str(op)) for op in seq)

def plus_minuses(operands):
    first, *rest = operands
    accumulators = {first}
    while rest:
        first, *rest = rest
        accumulators = {acc + first for acc in accumulators}.union({acc * first for acc in accumulators})
    return accumulators

p1 = sum(total for total, operands in candidates if total in plus_minuses(operands))
p2 = 0

print(f"Part one: {p1}")
print(f"Part two: {p2}")
