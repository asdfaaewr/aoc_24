from collections import defaultdict
from copy import deepcopy

day, test = 23, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read().splitlines()

d = defaultdict(list)
for line in data:
    a, b = line.split('-')
    d[a] += [b]
    d[b] += [a]

groups = [[i] for i in list(d.keys())]
while True:
    groups_old = deepcopy(groups)
    for k in d:
        for g in groups:
            if all([(e in d[k]) for e in g]):
                g.append(k)

    if groups == groups_old:
        q = max([len(g)for g in groups])
        print(','.join([sorted(g) for g in groups if len(g)==q][0]))
        break
