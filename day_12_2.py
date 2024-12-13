day, test = 12, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read().splitlines()

rows, cols = len(data), len(data[-1])
dirs = ((0,1), (1,0), (-1,0), (0,-1))

def check_sides(s):
    t = 0 
    for r in range(min(s)[0], max(s)[0]+2):
        for c in range(min([b for a,b  in s]), 2+max([b for a,b  in s])): 

            if ((r,c) in s) == ((r,c-1) in s) and ((r-1,c) in s) == ((r-1,c-1) in s): continue
            if ((r,c) in s) == ((r-1,c) in s): continue
            if ((r,c) in s) != ((r-1,c) in s): t+=1

    return 2*t

covered = set()
t = 0
for r in range(rows):
    for c in range(cols):
        if (r, c) in covered: continue

        stack = [(r,c)]
        covered.add((r, c))
        area = 0
        curr_set = set([(r, c)])

        while stack:
            x, y = stack.pop()
            area += 1

            for dx, dy in dirs:
                if x+dx not in range(rows): continue
                if y+dy not in range(cols): continue
                if data[x][y] != data[x+dx][y+dy]: continue
                if (x+dx, y+dy) in covered: continue

                stack.append((x+dx, y+dy))
                covered.add((x+dx, y+dy))
                curr_set.add((x+dx, y+dy))
               
        t += area * check_sides(curr_set)

print(t)



