import math
import random
import sys

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

V = set()
E = set()
for line in data.splitlines():
    node, *adjs = line.replace(":", " ").split()
    V |= {node, *adjs}
    E |= {(node, adj) for adj in adjs}


ss = lambda v: next(s for s in subsets if v in s)

while True:
    subsets = [{v} for v in V]
    
    while len(subsets) > 2:
        s1, s2 = map(ss, random.choice([*E]))
        if s1 != s2:
            s1 |= s2; 
            subsets.remove(s2)
    if sum(ss(u) != ss(v) for u,v in E) < 4:
        break

print(math.prod(map(len, subsets)))