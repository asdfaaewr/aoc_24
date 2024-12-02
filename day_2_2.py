day, test = 2, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.readlines()

def is_safe(line):
    diffs = [x-y for x, y in zip(line[1:], line[:-1])] 

    if (max(diffs) <= 3 and min(diffs) >= 1) or (max(diffs) <= -1 and min(diffs) >= -3):
        return 1

t = 0
for line in data:
    line = list(map(int, line.split()))
 
    for i in range(len(line)):
        if is_safe(line[:i]+ line[i+1:]):      
            t += 1
            break

print(t)   
