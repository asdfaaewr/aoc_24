from collections import Counter

day, test = 1, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.readlines()

for i in range(len(data)):
    data[i] = list(map(int, data[i].split()))

data_t = [[*row] for row in zip(*data)]

a, b = sorted(data_t[0]), sorted(data_t[1])

t = 0
for i in range(len(a)):
    t += abs(a[i]-b[i])
print(t)

b_counter = Counter(b)
t = 0
for i in range(len(a)):
    t += a[i] * b_counter[a[i]]
print(t)
