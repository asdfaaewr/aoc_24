day, test = 24, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    wires, gates_in = file.read().split('\n\n')

d = {}

for w in wires.splitlines():
    a, b = w.split(": ")
    d[a] = int(b)

gates = []

for g in gates_in.splitlines():
    w1, op, w2, _, w_target = g.split(" ")
    gates.append((w1, w2, op, w_target))

while gates:
    for g in gates:
        if g[0] in d and g[1] in d:
            if g[2] == 'AND':
                d[g[3]] = d[g[0]] & d[g[1]] 
            if g[2] == 'OR':
                d[g[3]] = d[g[0]] | d[g[1]] 
            if g[2] == 'XOR':
                d[g[3]] = d[g[0]] ^ d[g[1]] 

            gates.remove(g)

res = sorted([(e, d[e]) for e in d if e[0] == 'z'])[::-1]
print(int(''.join([str(b) for a, b in res]),2))