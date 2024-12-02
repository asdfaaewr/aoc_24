day, test = 2, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.readlines()

t=0
for line in data:
    line = list(map(int, line.split()))
    diffs = [x-y for x, y in zip(line[1:], line[:-1])] 

    if (max(diffs) <= 3 and min(diffs) >= 1) or (max(diffs) <= -1 and min(diffs) >= -3):
        t += 1

print(t)
