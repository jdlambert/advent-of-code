import sys
import re

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

stones = [tuple(int(d) for d in re.findall(r'-?\d+', line)) for line in data.splitlines()]
subset = stones[:4]

lo, hi = (7, 27) if "x" in sys.argv else (200000000000000, 400000000000000)

PARALLEL = float("inf")

def IJ(s):
    return (s[0], s[1], s[3], s[4])

def IK(s):
    return (s[0], s[2], s[3], s[5])

p1 = 0

def collide(s0, s1, getter, rock_dx=0, rock_dy=0):
    x0, y0, dx0, dy0 = getter(s0)
    x1, y1, dx1, dy1 = getter(s1)
    dx0 -= rock_dx
    dx1 -= rock_dx
    dy0 -= rock_dy
    dy1 -= rock_dy
    det = dx1*dy0 - dy1*dx0
    if det == 0:
        return PARALLEL
    di = x1 - x0
    dj = y1 - y0
    t0 = (dj*dx1 - di*dy1) / det
    t1 = (dj*dx0 - di*dy0) / det
    if t0 <= 0 or t1 <= 0:
        return None
    return (x0 + t0*dx0, y0 + t0*dy0)

for i, s0 in enumerate(stones):
    for s1 in stones[i + 1:]:
        collision = collide(s0, s1, IJ)
        p1 += (
            collision is not None and
            collision is not PARALLEL and
            all(lo <= p <= hi for p in collision)
        )

print(f"Part one: {p1}")

def rock_collisions(rock_dx, rock_dy, getter):
    p = None
    for i, s0 in enumerate(subset):
        for s1 in subset[i + 1:]:
            collision = collide(s0, s1, getter, rock_dx, rock_dy)
            if collision is PARALLEL:
                continue
            if collision is None:
                return None
            if p is not None and collision != p:
                return None
            p = collision
    return p

for di in range(256):
    for dj in range(256):
        ij = rock_collisions(di, dj, IJ)
        if ij is not None:
            for dk in range(256):
                ik = rock_collisions(di, dk, IK)
                if ik is not None:
                    print(f"Part two: {int(ij[0] + ij[1] + ik[1])}")
                    break
            break
