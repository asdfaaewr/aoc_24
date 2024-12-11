day, test = 11, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read().strip()

data = list(map(int, data.split()))

for i in range(25):
    new = [] 
    for i, n in enumerate(data):
        if n == 0:
            new.append(1)
        elif (l:=len(s:=str(n))) %2 == 0:
            new.append(int(s[:l//2]))
            new.append(int(s[l//2:]))
        else:
            new.append(n*2024)
    data = new

print(len(new))
    
        
    
    

