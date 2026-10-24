import sys
from collections import deque
from collections import defaultdict

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

PRUNER = 2 ** 24
MASK = PRUNER - 1
nums = [int(num) for num in data.splitlines()]

def evolve(secret):
    secret = ((secret << 6) ^ secret) & MASK
    secret = ((secret >> 5) ^ secret) & MASK
    return ((secret << 11) ^ secret) & MASK

def twothousand(secret, totals):
    pattern = deque(maxlen=4)
    seen = set()
    last_price = secret % 10
    for _ in range(2000):
        secret = evolve(secret)
        next_price = secret % 10
        delta = next_price - last_price
        pattern.append(delta)
        if len(pattern) == 4:
            key = tuple(pattern)
            if key not in seen:
                seen.add(key)
                totals[key] += next_price
        last_price = next_price
    return secret

totals = defaultdict(int)
p1 = sum(twothousand(secret, totals) for secret in nums)
p2 = max(totals.values(), default=0)

print(f"Part one: {p1}")
print(f"Part two: {p2}")
