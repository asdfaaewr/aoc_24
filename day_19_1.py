from functools import lru_cache

day, test = 19, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    towels, designs = file.read().split('\n\n')

towels = [t.strip() for t in towels.split(',')]
designs = designs.splitlines()

@lru_cache
def is_possible(d):
    if d in towels:
        return True
    else:
        for tow in towels:
            if d.startswith(tow):
                if is_possible(d[len(tow):]):
                    return True
        return False

t = 0
for d in designs:
    if is_possible(d):
        t+=1

print(t)