import sys

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

candidates = []
for line in data.splitlines():
    total, operands = line.split(":")
    int_ops = [int(op) for op in operands.strip().split(" ")]
    candidates.append((int(total), int_ops))

def concat_two(a, b):
    return int(f"{a}{b}")

def operatorize(operands, concat=False):
    first, *rest = operands
    accumulators = {first}
    while rest:
        first, *rest = rest
        new_accumulators = {acc + first for acc in accumulators}
        new_accumulators |= {acc * first for acc in accumulators}
        if concat:
            new_accumulators |= {concat_two(acc, first) for acc in accumulators}
        accumulators = new_accumulators
    return accumulators

p1 = sum(total for total, operands in candidates if total in operatorize(operands))
p2 = sum(total for total, operands in candidates if total in operatorize(operands, concat=True))

print(f"Part one: {p1}")
print(f"Part two: {p2}")
