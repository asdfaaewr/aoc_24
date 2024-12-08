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
        for i in range(-50, 50):
            if r - i * (r2-r) in range(len(data)) and c - i*(c2-c) in range(len(data[-1])):
                s.add((r - i*(r2-r), c - i*(c2-c)))

print(len(s))

