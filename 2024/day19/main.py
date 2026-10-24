import sys

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

pattern_str, target_str = data.split("\n\n")
patterns = pattern_str.split(", ")
targets = target_str.splitlines()
END = "END"

class Trie:

    def __init__(self, source):
        self.root = {}
        for word in source:
            cur = self.root
            for c in word:
                cur = cur.setdefault(c, {})
            cur[END] = END

    def matches(self, target):
        rets = []
        letters = []
        cur = self.root
        for letter in target:
            if letter not in cur:
                break
            letters.append(letter)
            cur = cur[letter]
            if END in cur:
                rets.append("".join(letters))
        return reversed(rets)

trie = Trie(patterns)

buildable_cache = dict()
def buildable(trie, target):
    if target in buildable_cache:
        return buildable_cache[target]
    if not target:
        rv = 1
    else:
        rv = sum(buildable(trie, target[len(match):]) for match in trie.matches(target))
    buildable_cache[target] = rv
    return rv

p1 = len([target for target in targets if buildable(trie, target) > 0])
p2 = sum(buildable(trie, target) for target in targets)

print(f"Part one: {p1}")
print(f"Part two: {p2}")
