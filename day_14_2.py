import re

day, test = 14, 0

with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read().splitlines()

robots, speeds = [], []

for line in data:
    r, c, dr, dc = [int(n) for n in re.findall("-?\d+\.?\d*", line)]
    robots.extend([(r, c)])
    speeds.extend([(dr, dc)])

max_neighbours, max_j = 0, 0
x, y = 103, 101 
rob = robots[:]
for j in range(1, 100000):
    for i in range(len(robots)):
        rob[i] = ((robots[i][0] + speeds[i][0] * j) % y, (robots[i][1] + speeds[i][1] * j) % x)

    neighbours = 0
    for r, c in rob:   
        if (r-1, c) in rob or (r+1, c) in rob or (r+1, c+1) in rob or (r, c+1) in rob or (r, c-1) in rob or (r-1, c-1) in rob or (r+1, c-1) in rob or (r-1, c+1) in rob:
            neighbours += 1

    if neighbours > max_neighbours:
        max_neighbours = neighbours
        max_j = j
    
    if set(robots) == set(rob):
        print(max_j)
        exit(0)