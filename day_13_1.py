import re

day, test = 13, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read().split('\n\n')

t = 0
for block in data:
    line = [list(map(int, re.findall("\d+", b))) for b in block.split('\n')]

    a = line[1][1] - line[0][1] / line[0][0] * line[1][0]
    b = line[2][1] - line[0][1] / line[0][0] * line[2][0]
    res1, res2 = b / a, (line[2][0] - line[1][0] * (b/a)) / line[0][0]

    t += (abs(res1 - round(res1))<0.0001) * res1   + (abs(res2 - round(res2))<0.0001) * res2 * 3

print(t)

