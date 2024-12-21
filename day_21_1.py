day, test = 21, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read().splitlines()

door = {'7':(0,0), '8':(0,1), '9':(0,2),
        '4':(1,0), '5':(1,1), '6':(1,2),
        '1':(2,0), '2':(2,1), '3':(2,2),
                 '0':(3,1), 'A':(3,2)}

directional = {'^':(0,1), 'A':(0,2),
    '<':(1,0), 'v':(1,1), '>':(1,2)}


col_map = {-2: '<<', -1: '<', 0: '', 1: '>', 2: '>>'}
row_map = {-3: '^^^', -2: '^^', -1: '^', 0: '', 1: 'v', 2: 'vv', 3: 'vvv'}


door_to_directional = {}

directional_to_directional = {}

for e1 in directional:
    for e2 in directional:
        if directional[e1][1] < directional[e2][1]:
            if directional[e1][0] < directional[e2][0]:
                directional_to_directional[(e1, e2)] = (directional[e2][1] - directional[e1][1]) * '>' + \
                                       (directional[e2][0] - directional[e1][0]) * 'v' + 'A'
            else: 
                directional_to_directional[(e1, e2)] = (directional[e2][1] - directional[e1][1]) * '>' + \
                                       +(directional[e1][0] - directional[e2][0]) * '^' + 'A'
        else:
            if directional[e1][0] < directional[e2][0]:
                directional_to_directional[(e1, e2)] = (directional[e2][0] - directional[e1][0]) * 'v' + \
                                       (directional[e1][1] - directional[e2][1]) * '<' + 'A'
            else: 
                directional_to_directional[(e1, e2)] = (directional[e1][1] - directional[e2][1]) * '<' + \
                                       (directional[e1][0] - directional[e2][0]) * '^' + 'A'           


def get_dir(code):
    t = ''
    pre = 'A'
    code = pre+code
    for i in range(len(code)-1):
        t += directional_to_directional[(code[i], code[i+1])]
    return t


door_dists = {}
for e1 in door:
    for e2 in door:
        r1, c1 = door[e1]
        r2, c2 = door[e2]
        paths = []

        if not(c2 == 0 and r1 == 3):
            path = col_map[c2 - c1] + row_map[r2 - r1] + 'A'
            paths.append((len(get_dir(get_dir(path))), path))

        if not(r2 == 3 and c1 == 0):
            path = row_map[r2 - r1] + col_map[c2 - c1] + 'A'
            paths.append((len(get_dir(get_dir(path))), path))

        door_dists[(e1, e2)] = sorted(paths)[0][1]


out = 0
for code in data:
    code_copy = code
    t = ''
    pre = 'A'
    code = pre+code
    for i in range(len(code)-1):
        t += door_dists[(code[i], code[i+1])]

    code = t
    t = ''
    pre = 'A'
    code = pre+code
    for i in range(len(code)-1):
        t += directional_to_directional[(code[i], code[i+1])]

    code = t
    t = ''
    pre = 'A'
    code = pre+code
    for i in range(len(code)-1):
        t += directional_to_directional[(code[i], code[i+1])]

    out += len(t) * int(code_copy[:-1])

print(out)