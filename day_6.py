day, test = 6, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.readlines()

for i in range(len(data)):
    for j in range(len(data[-1])):
        if data[i][j] == '^':
            r, c = i, j 

v = set([(r, c)])
d = (-1, 0)

while True:
    if not 0 <= r + d[0] < len(data):
        break

    if not 0 <= c + d[1] < len(data[-1]):
        break

    if data[r + d[0]][c+ d[1]] == '#':
        d = (d[1], -d[0])
    else:
        r, c = r + d[0], c+ d[1]
        v.add((r, c))

print(len(v))
