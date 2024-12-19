from functools import lru_cache

day, test = 19, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    towels, designs = file.read().split('\n\n')

towels = [t.strip() for t in towels.split(',')]
designs = designs.splitlines()

@lru_cache
def is_possible(d):
    w = 0
    for tow in towels:
        if d.startswith(tow):
            if len(d) == len(tow):
                w += 1
            if (len(d) > len(tow)) and (q:=is_possible(d[len(tow):])):
                w += q 
    return w


t = 0
for d in designs:
    t += is_possible(d)

print(t)