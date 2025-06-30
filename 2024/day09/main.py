import sys

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read().strip()

file_id = 0
array = []
free_spaces = []
files = []
for i, c in enumerate(data):
    count = int(c)
    if i % 2 == 0:
        files.append((len(array), count, file_id))
        array.extend([file_id] * count)
        file_id += 1
    else:
        free_spaces.append((len(array), count))
        array.extend([-1] * count)

i, j = 0, len(array) - 1

while i < j:
    while array[i] != -1:
        i += 1
    while array[j] == -1:
        j -= 1
    if i < j:
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1

defragged = {}
for file_i, file_count, file_id in reversed(files):
    for j in range(len(free_spaces)):
        free_j, free_count = free_spaces[j]
        if free_count >= file_count:
            for defragged_i in range(free_j, free_j + file_count):
                defragged[defragged_i] = file_id
            free_count -= file_count
            free_j += file_count
            free_spaces[j] = free_j, free_count
            break
    else:
        for defragged_i in range(file_i, file_i + file_count):
            defragged[defragged_i] = file_id
        
p1 = sum(i * id for i, id in enumerate(array) if id != -1)
p2 = sum(i * id for i, id in defragged.items())

eof = max(defragged.keys())
for i in range(eof + 1):
    print(str(defragged.get(i, ".")), end="")
print()

print(f"Part one: {p1}")
print(f"Part two: {p2}")
