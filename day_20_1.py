from collections import deque

day, test = 20, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read().splitlines()

for r in range(len(data)):
    for c in range(len(data[-1])):
        if data[r][c]=='S':
            sr, sc = r, c
        if data[r][c]=='E':
            er, ec = r, c

def get_time(cheat=[]):
    stack = deque([(sr, sc, 0)])
    seen = set()

    while stack:
        r, c, steps = stack.popleft()
        seen.add((r,c))
        if r ==er and c == ec:
            return steps

        for cr, cc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
            if cr in range(len(data)) and cc in range(len(data[-1])):
                if data[cr][cc] != '#' or (cr, cc) in cheat:
                    if (cr, cc) not in seen:
                        stack.append((cr, cc, steps +1))

q  = []
base = get_time()

for r in range(0, len(data)-1):
    for c in range(0, len(data[-1])-1):
        if data[r][c] == '.': continue
        cheat = [(r, c)]
        if base - get_time(cheat) > 0:
            q.append(base - get_time(cheat))

print(sum([1 for c in q if c>=100]))
