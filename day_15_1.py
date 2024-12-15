day, test = 15, 0

with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data, inst = file.read().split("\n\n")

data = [[*c] for c in data.splitlines()]
inst = [*"".join(inst.splitlines())[::-1]]

for r in range(len(data)):
    for c in range(len(data[-1])):
        if data[r][c] == "@":
            break
    else:
        continue
    break

dirs = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}

while inst:
    dr, dc = dirs[inst.pop()]

    if data[r+dr][c+dc] == ".":
        data[r+dr][c+dc] = "@"
        data[r][c] = "."
        r += dr; c += dc
        continue
    
    if data[r+dr][c+dc] == "#":
        continue

    i = 1
    while data[r+i*dr][c+i*dc] == "O":
        i +=1
    
    if data[r+i*dr][c+i*dc] == "#":
        continue
    
    if data[r+i*dr][c+i*dc] == ".":
        data[r+i*dr][c+i*dc] = "O"
        data[r+dr][c+dc] = "@"
        data[r][c] = "."
        r += dr; c += dc

t = 0
for r in range(len(data)):
    for c in range(len(data[-1])):
        if data[r][c] == "O":
            t += (r)*100 + c

print(t)
