day, test = 17, 0

with open('in_' + str(day) + '_test' * test + '.txt') as file:
    regs, program = file.read().split("\n\n")
    program = list(map(int, program[9:].split(',')))

l = []
stack = [(15, 0)]

while stack:
    n, a = stack.pop()

    for i in range(8):
        new_a = a*8 + i
        if (((new_a%8)^5)^(new_a >> ((new_a%8)^1))) % 8 == program[n]:
            if n == 0:
                l.append(new_a)
            else:
                stack.append((n-1, new_a))

print(min(l))
