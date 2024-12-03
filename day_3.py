day, test = 3, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read()

t1, t2, i  = 0, 0, 0

while i < len(data):
    if data[i:i+4] == 'mul(':
        last_do = data[:i].rfind(r"do()")
        last_dont = data[:i].rfind(r"don't()")

        i += 4
        s = i

        while data[i] in '0123456789':
            i += 1
        e = i
        a = int(data[s:e])

        if data[i] != ',':
            continue
        else:
            i += 1
            s = i

        while data[i] in '0123456789':
            i += 1
        e = i
        b = int(data[s:e])

        if data[i] != ')':
            continue
        
        t1 += a*b

        t2 += a*b * (last_dont <= last_do)  
    i+=1

print(t1)
print(t2)