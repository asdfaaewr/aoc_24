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

d = deque([(r_s, c_s, 0, 1, 0)])
seen = {(r_s, c_s, 0, 1): 0}

while d:
    r, c, r_dir, c_dir, score = d.popleft()

    for dr, dc in dirs:
        if data[r+dr][c+dc] != '#':
            d_score = 1 if (dr == r_dir and dc == c_dir) else 1001
            if (r+dr, c+dc, dr, dc) not in seen or seen[(r+dr, c+dc, dr, dc)] > score+d_score:
                d.append([r+dr, c+dc, dr, dc, score+d_score])
                seen[(r+dr, c+dc, dr, dc)] = score+d_score

print(min([seen[key] for key in seen if (key[0]==r_e and key[1]==c_e)]))