import re
from fractions import Fraction

day, test = 13, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read().split('\n\n')

t = 0
for block in data:
    line = [list(map(int, re.findall("\d+", b))) for b in block.split('\n')]
    line[2][1] +=  10000000000000
    line[2][0] +=  10000000000000

    a = line[1][1] - Fraction(line[0][1],  line[0][0]) * line[1][0]
    b = line[2][1] - Fraction(line[0][1],  line[0][0]) * line[2][0]
    res1, res2 = Fraction(b , a), Fraction(line[2][0] - line[1][0] * (Fraction(b , a)) , line[0][0])

    t += (res1 == round(res1)) * res1   + (res2 == round(res2))  * res2 *3

print(t)

