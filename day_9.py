day, test = 9, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read()

nums, free, a = [], [], 0

for i, c in enumerate(data):
    for j in range(int(c)):
        if i % 2 == 0:
            nums.append(i//2)
        else:
            nums.append(-1)
            free.append(a)
        a += 1

free = free[::-1]
while free:
    while (id := nums.pop()) == -1:
        pass

    idx = free.pop() 
    if idx >= len(nums):
        nums.append(id)
    else:
        nums[idx] = id   
 
t = 0
for i in range(len(nums)):
    t += nums[i] * i

print(t)