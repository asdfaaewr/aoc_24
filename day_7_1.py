import itertools

day, test = 7, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.readlines()

t = 0
for line in data:
    a, b = line.split(': ')
    a = int(a)

    b = [int(c) for c in b.split()]
    ops = list(itertools.product(['+', '*'], repeat=len(b)-1))

    for o in ops:
        r = b[0]
        for i, w in enumerate(o):
            if w == '*':
                r *= b[i+1]
            else:
                r += b[i+1]

        if a == r:
            t += a
            break

print(t)