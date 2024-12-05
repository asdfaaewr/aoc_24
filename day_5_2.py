from collections import defaultdict

day, test = 5, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read()
    rules, updates = data.split("\n\n")

d = defaultdict(tuple)
for line in rules.splitlines():
    a, b = [int(x) for x in line.split('|')]
    d[b] = (*d[b], a)

t = 0

for line in updates.splitlines():
    line = list(map(int, line.split(',')))
    error = 0

    for i, n in enumerate(line):
        for x in d[n]:
            if x in line and x not in line[:i]:
                error = 1
    
    while error:
        for i, n in enumerate(line):
            for x in d[n]:
                if x in line and x not in line[:i]:
                    pos_x = line.index(x)
                    line[i], line[pos_x] = line[pos_x] , line[i]
        
        error = 0            
        for i, n in enumerate(line):
            for x in d[n]:
                if x in line and x not in line[:i]:      
                    error = 1
        
        if not error:
            t += line[len(line)//2]

print(t)


