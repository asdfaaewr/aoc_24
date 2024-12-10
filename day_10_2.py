day, test = 10, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read().splitlines()

data = [list(map(int, line)) for line in data]
dirs = [[0,1], [1,0], [-1,0], [0,-1]]

t=0

for r in range(len(data)):
    for c in range(len(data[-1])):
        if data[r][c] != 0: continue
        stack = [(r, c, 0)]
        while stack:
            rt, ct, n = stack.pop()

            for dr, dc in dirs:
                if rt + dr in range(len(data)) and ct + dc in range(len(data[-1])):
                    if data[rt+dr][ct+dc] == n+1:
                        if n+1 == 9:
                            t += 1        
                        else:
                            stack.append((rt+dr, ct+dc, n+1))

print(t)