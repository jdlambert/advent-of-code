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

def possible(operands, concat=False):
    if len(operands) > 1:
        last, *rest = operands
        possible_rest = possible(rest)
        plus = [last + r for r in possible_rest]
        times = [last * r for r in possible_rest]
        concats = [concat_two(r, last) for r in possible_rest] if concat else []
        return plus + times + concats
    assert operands
    return operands

def is_valid(total, operands, concat=False):
    return total in possible(list(reversed(operands)), concat=concat)

p1 = sum(total for total, operands in candidates if is_valid(total, operands))
p2 = sum(total for total, operands in candidates if is_valid(total, operands, concat=True))

print(f"Part one: {p1}")
print(f"Part two: {p2}")
