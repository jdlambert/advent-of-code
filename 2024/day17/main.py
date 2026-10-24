import sys

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

reg_block, op_block = data.split("\n\n")

regs = dict(zip(("A", "B", "C"), [int(line.split(" ")[-1]) for line in reg_block.splitlines()]))

print(regs["A"], regs["B"], regs["C"])

program = op_block.split(" ")[1]
ops = [int(op) for op in program.split(",")]

def combo(op, regs):
    if 0 <= op <= 3: return op
    if op == 4: return regs['A']
    if op == 5: return regs['B']
    if op == 6: return regs['C']

def adv(op, regs):
    regs["A"] //= 2 ** combo(op, regs)

def bxl(op, regs):
    regs["B"] ^= op

def bst(op, regs):
    regs["B"] = combo(op, regs) % 8

def jnz(op, regs, pc):
    if regs["A"] != 0:
        return op
    return pc + 2

def bxc(_op, regs):
    regs["B"] ^= regs["C"]

def out(op, regs):
    return str(combo(op, regs) % 8)
    
def bdv(op, regs):
    regs["B"] = regs["A"] // (2 ** combo(op, regs))

def cdv(op, regs):
    regs["C"] = regs["A"] // (2 ** combo(op, regs))

op_map = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv,
}

def run(regs):
    pc = 0
    output = []
    while pc < len(ops):
        operator = op_map[ops[pc]]
        operand = ops[pc + 1]
        if operator is jnz:
            pc = operator(operand, regs, pc)
        elif operator is out:
            output.append(out(operand, regs))
            pc += 2
        else:
            operator(operand, regs)
            pc += 2
    return ','.join(output)

p1 = run(regs)

def one_step_output(a):
    b = (a % 8) ^ 1
    c = a // (2 ** b)
    return (b ^ c ^ 4) % 8

def reverse_construct(program_digits):
    candidates = {0}
    for target in reversed(program_digits):
        next_candidates = set()
        for suffix in candidates:
            for digit in range(8):
                a = (suffix << 3) | digit
                if one_step_output(a) == target:
                    next_candidates.add(a)
        candidates = next_candidates
    print([oct(c) for c in candidates])
    return min(candidates)

p2 = reverse_construct(ops)

print(f"Part one: {p1}")
print(f"Part two: {p2}")
