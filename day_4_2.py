day, test = 4, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read().splitlines()

t = 0

for r in range(1, len(data)-1):
    for c in range(1, len(data[0])-1):
        if data[r][c] != 'A':
            continue

        if set([data[r-1][c-1], data[r+1][c+1]]) == {'M', 'S'} and set([data[r-1][c+1], data[r+1][c-1]]) == {'M', 'S'}:
            t +=1

print(t)
