import re

day, test = 14, 0

with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read().splitlines()

robots, speeds = [], []


for line in data:
    r, c, dr, dc = [int(n) for n in re.findall("-?\d+\.?\d*", line)]
    robots.extend([(r, c)])
    speeds.extend([(dr, dc)])

x, y = 103, 101

n = 100
for i in range(len(robots)):
    robots[i] = ((robots[i][0] + speeds[i][0] * n) % y, (robots[i][1] + speeds[i][1] * n) % x)

a = sum([1 if r[0]< (y-1)/2 and r[1]<(x-1)/2 else 0 for r in robots]) 
b = sum([1 if r[0]> (y-1)/2 and r[1]<(x-1)/2 else 0 for r in robots]) 
c = sum([1 if r[0]< (y-1)/2 and r[1]>(x-1)/2 else 0 for r in robots]) 
d = sum([1 if r[0]> (y-1)/2 and r[1]>(x-1)/2 else 0 for r in robots]) 
print(a*b*c*d)


