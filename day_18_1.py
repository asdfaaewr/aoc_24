from collections import deque

dirs4 = [[0, 1], [0, -1], [1, 0], [-1, 0]]

day, test = 18, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read().splitlines()

data = set([tuple(map(int, line.split(','))) for line in data[:1024]])

d = deque([(0, 0, 0)])
seen = set()

low = 100000000000

while d:
    r, c, steps = d.popleft()
    if (r, c) in seen: continue
    seen.add((r, c))
    if r == 70 and c == 70:
        low = min(low, steps)
    for dr, dc in dirs4:
        if not 0 <= r+dr <= 70: continue
        if not 0 <= c+dc <= 70: continue
        if (r+dr, c+dc) in data: continue

        d.append((r+dr, c+dc, steps+1))

print(low)

        
    



