day, test = 15, 0

with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data, inst = file.read().split("\n\n")

data = [[*c] for c in data.splitlines()]
inst = [*"".join(inst.splitlines())[::-1]]

new_d = {'#': '##', 'O':'[]', '.':'..', '@':'@.'}
data = [[*''.join([new_d[c] for c in line])] for line in data]

for r in range(len(data)):
    for c in range(len(data[-1])):
        if data[r][c] == "@":
            break
    else:
        continue
    break

dirs = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}

def try_push(r, c, dr, dc):

    if data[r+dr][c+dc] == ".":
        data[r+dr][c+dc] = data[r][c]
        data[r][c] = "."
        r += dr; c += dc
        return 1 
    
    if data[r+dr][c+dc] == "#":
        return 0

    if data[r+dr][c+dc] in "[]" and dr == 0:
        if try_push(r+dr, c+dc, dr, dc):
            data[r+dr][c+dc] = data[r][c]
            data[r][c] = "."
            return 1
        else:
            return 0

    if data[r+dr][c+dc] in "[" and dr != 0:
        if try_push(r+dr, c+dc, dr, dc) and try_push(r+dr, c+1+dc, dr, dc):
            data[r+dr][c+dc] = data[r][c]
            data[r][c] = "."
            return 1
        else:
            return 0

    if data[r+dr][c+dc] in "]" and dr != 0:
        if try_push(r+dr, c+dc, dr, dc) and try_push(r+dr, c-1+dc, dr, dc):
            data[r+dr][c+dc] = data[r][c]
            data[r][c] = "."
            return 1
        else:
            return 0

while inst:
    dr, dc = dirs[inst.pop()]
    data_before_push = [line[:] for line in data] 

    if not try_push(r, c, dr, dc):
        data = data_before_push
    else:
        r+=dr; c+=dc

t = 0
for r in range(len(data)):
    for c in range(len(data[-1])):
        if data[r][c] in "[":
            t += r*100 + c

print(t)
