day, test = 20, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read().splitlines()

for r in range(len(data)):
    for c in range(len(data[-1])):
        if data[r][c]=='S':
            sr, sc = r, c
        if data[r][c]=='E':
            er, ec = r, c

def get_map(sr, sc):
    stack = [(sr, sc, 0)]
    seen = set()
    d = {}

    while stack:
        r, c, steps = stack.pop()
        seen.add((r,c))
        d.update({(r, c): steps})

        for cr, cc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
            if cr in range(len(data)) and cc in range(len(data[-1])):
                if data[cr][cc] != '#':
                    if (cr, cc) not in seen:
                        stack.append((cr, cc, steps +1))
    return d

from_start = get_map(sr, sc)
to_end = get_map(er, ec) 

base = from_start[(er, ec)]

res = set()
for (r, c), steps in from_start.items():
    for dr in range(-20, 21):
        for dc in range(-20, 21):
            if abs(dr) + abs(dc) > 20: continue
            cr, cc = r+dr, c+dc
            if cr in range(len(data)) and cc in range(len(data[0])):
                if (cr, cc) in to_end:
                    if steps + to_end[(cr, cc)] + abs(dr)+abs(dc) <= base - 100:
                        res.add(((r, c), (cr, cc)))

print(len(res))
