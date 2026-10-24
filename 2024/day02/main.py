import sys

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

reports = [[int(level) for level in line.split(' ')] for line in data.splitlines()]

def safe(report):
    asc = report[1] > report[0]
    return all( 
            (asc and rl < rr or not asc and rl > rr)
            and abs(rl - rr) < 4
            for rl, rr in zip(report, report[1:]))

def almost_safe(report):
    return safe(report) or any(safe(report[:i] + report[i + 1:]) for i in range(len(report)))

p1 = len([report for report in reports if safe(report)])
p2 = len([report for report in reports if almost_safe(report)])

print(f"Part one: {p1}")
print(f"Part two: {p2}")
