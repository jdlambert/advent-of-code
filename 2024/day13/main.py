import sys
import re

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()
machine_strs = data.split("\n\n")
num_re = re.compile(r"(\d+)")
machines = []
for machine_str in machine_strs:
    machines.append([int(n) for n in num_re.findall(machine_str)])

print(machines[0])

def div(px, py, ax, ay):
    if px < ax or py < ay:
        return -1
    if px % ax or py % ay:
        return 0
    if (rem := px // ax) == py // ay:
        return rem
    return 0

for ax, ay, bx, by, px, py in machines:
    pass

p1 = 0
for ax, ay, bx, by, px, py in machines:
    t = 0
    while not div(px, py, ax, ay):
        t += 1
        px -= bx
        py -= by
    if (rem := div(px, py, ax, ay)) > 0:
        print(t, rem)
        p1 += t + 3*rem
    else:
        print("none")
print(f"Part one: {p1}")

error = 10000000000000

p2 = 0
for ax, ay, bx, by, px, py in machines:
    px += error
    py += error
    det = (ax * by) - (bx * ay)
    nad = px*by - py*bx
    nbd = py*ax - px*ay
    if det == 0 or nad % det or nbd % det:
        print("none d")
        continue
    na = nad // det
    nb = nbd // det
    if na >= 0 and nb >= 0:
        print(nb, na)
        p2 += 3*na + nb
    else:
        print("none -")

print(f"Part two: {p2}")
