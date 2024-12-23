from aoc import *

day, test = 23, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read().splitlines()

d = defaultdict(list)
for line in data:
    a, b = line.split('-')
    d[a] += [b]
    d[b] += [a]

res = set()

for k in d:
    for k2 in d[k]:
        for k3 in d[k2]:
            if k in d[k3]:
                candidate = tuple(sorted((k, k2, k3)))
                res.add(candidate)

t=0
for tup in res:
    if tup[0][0] =='t' or tup[1][0] =='t' or tup[2][0] =='t':
        t+=1

print(t)