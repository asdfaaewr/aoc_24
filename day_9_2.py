day, test = 9, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read()

free, nums, a = [], [], 0

for i, c in enumerate(data):

    if i%2 != 0:
        free.append((a,int(c)))
    else: 
        nums.append((a, a+int(c)-1, i//2))  
    a += int(c) 

nums_temp = nums = nums[::-1]

for num_idx, (start, end, id) in enumerate(nums):
    for free_idx, (free_start, free_length) in enumerate(free):
        if end-start+1 <= free_length and start > free_start:
            free_new = free[:]
            free_new.append((start, end-start+1))
            free_new[free_idx] = (free_start + end-start+1, free_length - (end-start+1))
            nums_temp[num_idx] = (free_start, free_start + end - start,id)
            break
    free = sorted(free_new)

t = 0
for start, end, id in nums_temp:
    for i in range(start, end +1):
        t += i*id

print(t)


