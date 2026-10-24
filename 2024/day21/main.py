import sys
from functools import lru_cache

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

p1 = 0
p2 = 0

NUMPAD = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['X', '0', 'A'],
]

DIRPAD = [
    ['X', '^', 'A'],
    ['<', 'v', '>'],
]

def interleave(di, dj):
    out = []
    def rec(i, j, commands: list):
        if i == abs(di) and j == abs(dj):
            out.append("".join(commands + ["A"]))
            return
        if i < abs(di):
            commands.append("^" if di < 0 else "v")
            rec(i + 1, j, commands)
            commands.pop()
        if j < abs(dj):
            commands.append("<" if dj < 0 else ">")
            rec(i, j + 1, commands)
            commands.pop()
    rec(0, 0, [])
    return out

def pad_to_map(pad):
    out = {}
    for i, line in enumerate(pad):
        for j, c in enumerate(line):
            out[c] = i, j
    return out

NUMMAP = pad_to_map(NUMPAD)
DIRMAP = pad_to_map(DIRPAD)

path_cache = {}
def allowed_paths(pad_name, src, target):
    cache_key = (pad_name, src, target)
    if cache_key in path_cache:
        return path_cache[cache_key]
    if pad_name == "NUM":
        pad = NUMPAD
        mapping = NUMMAP
    else:
        pad = DIRPAD
        mapping = DIRMAP
    si, sj = mapping[src]
    ti, tj = mapping[target]
    paths = interleave(ti - si, tj - sj)
    out = []
    for path in paths:
        i, j = si, sj
        for command in path:
            match command:
                case "^":
                    i -= 1
                case "v":
                    i += 1
                case ">":
                    j += 1
                case "<":
                    j -= 1
            if pad[i][j] == 'X':
                break
        else:
            out.append(path)
    path_cache[cache_key] = tuple(out)
    return path_cache[cache_key]

@lru_cache()
def dir_cost(src, target, depth):
    paths = allowed_paths("DIR", src, target)
    if depth == 0:
        return min(len(path) for path in paths)
    return min(type_on_dir(path, depth - 1) for path in paths)

@lru_cache()
def type_on_dir(code, depth):
    total = 0
    src = 'A'
    for target in code:
        total += dir_cost(src, target, depth)
        src = target
    return total

def type_on_num(code, directional_robots):
    total = 0
    src = 'A'
    for target in code:
        paths = allowed_paths("NUM", src, target)
        total += min(type_on_dir(path, directional_robots - 1) for path in paths)
        src = target
    return total

for code in data.splitlines():
    number = int(code[:-1])
    p1 += number * type_on_num(code, 2)
    p2 += number * type_on_num(code, 25)

print(f"Part one: {p1}")
print(f"Part one: {p2}")
