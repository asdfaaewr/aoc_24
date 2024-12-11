from collections import defaultdict

day, test = 11, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read().strip()


d = defaultdict(int)
for n in data.split():
    d[int(n)] += 1


def get_next(n):
    new = [] 
    if n == 0:
        new.append(1)
    elif (l:=len(s:=str(n))) %2 == 0:
        new.append(int(s[:l//2]))
        new.append(int(s[l//2:]))
    else:
        new.append(n*2024)
    return new


for i in range(75):
    d_new = d.copy()
    for n in d:
        if d[n]==0: continue
        for e in get_next(n):
            d_new[e] += d[n]
        d_new[n] -= d[n]
    d = d_new

print(sum([d[k] for k in d]))

