import sys
import re

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

boss_hp, boss_damage, boss_armor = [int(num) for num in re.findall(r"\d+", data)]

weapons = [
    ("Dagger", 8, 4, 0),
    ("Shortsword", 10, 5, 0),
    ("Warhammer", 25, 6, 0),
    ("Longsword", 40, 7, 0),
    ("Greataxe", 74, 8, 0),
]

armor = [
    ("Leather", 13, 0, 1),
    ("Chainmail", 31, 0, 2),
    ("Splintmail", 53, 0, 3),
    ("Bandedmail", 75, 0, 4),
    ("Platemail", 102, 0, 5),
    ("Empty", 0, 0, 0)
]

rings = [
    ("Damage +1", 25, 1, 0),
    ("Damage +2", 50, 2, 0),
    ("Damage +3", 100, 3, 0),
    ("Defense +1", 20, 0, 1),
    ("Defense +2", 40, 0, 2),
    ("Defense +3", 80, 0, 3),
    ("Empty 1", 0, 0, 0),
    ("Empty 2", 0, 0, 0)
]

loadouts = []
for w in weapons:
    for a in armor:
        for r1 in rings:
            for r2 in rings:
                if r1 != r2:
                    loadouts.append((w, a, r1, r2))

p1 = float("inf")
p2 = float("-inf")

for loadout in loadouts:
    my_cost = sum([item[1] for item in loadout])
    my_damage = sum([item[2] for item in loadout])
    my_armor = sum([item[3] for item in loadout])

    boss_hit = max(1, boss_damage - my_armor)
    my_hit = max(1, my_damage - boss_armor)

    my_hits_til_dead = 100 // boss_hit
    boss_hits_til_dead = boss_hp // my_hit

    if boss_hits_til_dead > my_hits_til_dead:
        p2 = max(my_cost, p2)
    else:
        p1 = min(my_cost, p1)

print(f"Part one: {p1}")
print(f"Part two: {p2}")
