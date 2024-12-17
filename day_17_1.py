import re

day, test = 17, 0

with open('in_' + str(day) + '_test' * test + '.txt') as file:
    regs, program = file.read().split("\n\n")
    a, b, c = [[i] for i in list(map(int, re.findall(r"-?\d+", regs)))]
    program = list(map(int, program[9:].split(',')))

d = {0:[0], 1: [1], 2:[2], 3:[3], 4: a, 5: b, 6: c}

output = [""]

def adv(op):
    a[0] =  int(a[0]/(2**d[op][0]))
    pointer[0] += 2

def bxl(op):
    b[0] = b[0] ^ int(op)
    pointer[0] += 2

def bst(op):
    b[0] = d[op][0] % 8
    pointer[0] += 2

def jnz(op):
    if a[0] == 0:
        pointer[0] += 2
    else:
        pointer[0] = int(op)

def bxc(op):
    b[0] = int(c[0]) ^ int(b[0])
    pointer[0] += 2

def out(op):
    output[0] += "," + str(d[op][0] % 8)
    pointer[0] += 2

def bdv(op):
    b[0] =  int(a[0]/(2**d[op][0]))
    pointer[0] += 2

def cdv(op):
    c[0] =  int(a[0]/(2**d[op][0]))
    pointer[0] += 2

opcodes = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]

pointer = [0]

while True:
 
    if pointer[0] >= len(program):
        break

    opcode, operand = program[pointer[0]:pointer[0]+2]
    opcodes[opcode](operand)

print(output[0][1:])


