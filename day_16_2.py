from collections import deque

day, test = 16, 0

with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read().splitlines()

for r in range(len(data)):
    for c in range(len(data[-1])):
        if data[r][c] == "E":
            r_e, c_e = r, c
        if data[r][c] == "S":
            r_s, c_s = r, c

dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

d = deque([(r_s, c_s, 0, 1, 0, [])])
seen = {(r_s, c_s, 0, 1): 0}

total_best = set([(r_e, c_e)])
best_score = 134588

while d:
    r, c, r_dir, c_dir, score, path = d.popleft()
    new_path = path[:]
    
    if r == r_e and c == c_e and score == best_score:
        total_best.update([*path])

    for dr, dc in dirs:
        if data[r+dr][c+dc] != '#':
            d_score = 1 if (dr == r_dir and dc == c_dir) else 1001
            if (r+dr, c+dc, dr, dc) not in seen or seen[(r+dr, c+dc, dr, dc)] >= score+d_score:
                new_path += [(r, c)]
                d.append([r+dr, c+dc, dr, dc, score+d_score, new_path])
                seen[(r+dr, c+dc, dr, dc)] = score+d_score

print(len(total_best))
