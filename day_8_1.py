from collections import defaultdict
import itertools

day, test = 8, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.readlines()

d = defaultdict(list)
for r in range(len(data)):
    for c in range(len(data[-1])):
        d[data[r][c]].append((r, c))

s = set([])    
for c, antennas in d.items():
    if c == '.': continue
    for (r, c), (r2, c2) in itertools.combinations(antennas, 2):
        if r - (r2-r) in range(len(data)) and c - (c2-c) in range(len(data[-1])):
            s.add((r - (r2-r), c - (c2-c)))

        if r2 - (r-r2) in range(len(data)) and c2 - (c-c2) in range(len(data[-1])):
            s.add((r2 - (r-r2), c2 - (c-c2)))

print(len(s))