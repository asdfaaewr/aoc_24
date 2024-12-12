day, test = 12, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read().splitlines()

rows, cols = len(data), len(data[-1])
dirs = ((0,1), (1,0), (-1,0), (0,-1))

covered = set()
t = 0
for r in range(rows):
    for c in range(cols):
        if (r, c) in covered: continue

        stack = [(r,c)]
        covered.add((r, c))
        area, circ = 0, 0

        while stack:
            x, y = stack.pop()
            area += 1

            for dx, dy in dirs:
                if x+dx not in range(rows) or y+dy not in range(cols) or data[x][y] != data[x+dx][y+dy]:
                    circ += 1
                    continue

                if (x+dx, y+dy) in covered: continue

                stack.append((x+dx, y+dy))
                covered.add((x+dx, y+dy))

        t += circ * area



print(t)
