from collections import defaultdict

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


dir_to_dir = {}

def get_dir(code):
    t = ''
    pre = 'A'
    code = pre+code
    for i in range(len(code)-1):
        t += directional_to_directional[(code[i], code[i+1])]
    return t

for e1 in directional:
    for e2 in directional:
        r1, c1 = directional[e1]
        r2, c2 = directional[e2]
        paths = []

        if not(c2 == 0 and r1 == 0):
            path = col_map[c2 - c1] + row_map[r2 - r1] + 'A'
            paths.append((len(get_dir(get_dir(path))), path))

        if not(r2 == 0 and c1 == 0):
            path = row_map[r2 - r1] + col_map[c2 - c1] + 'A'
            paths.append((len(get_dir(get_dir(path))), path))

        if len(paths) == 2 and paths[0][0] != paths[1][0]:
            print(e1, e2, paths)

        dir_to_dir[(e1, e2)] = sorted(paths)[0][1]


def get_dir(code):
    t = ''
    pre = 'A'
    code = pre+code
    for i in range(len(code)-1):
        t += dir_to_dir[(code[i], code[i+1])]
    return t


for e1 in directional:
    for e2 in directional:
        r1, c1 = directional[e1]
        r2, c2 = directional[e2]
        paths = []

        if not(c2 == 0 and r1 == 0):
            path = col_map[c2 - c1] + row_map[r2 - r1] + 'A'
            paths.append((len(get_dir(get_dir(path))), path))

        if not(r2 == 0 and c1 == 0):
            path = row_map[r2 - r1] + col_map[c2 - c1] + 'A'
            paths.append((len(get_dir(get_dir(path))), path))

        if len(paths) == 2 and paths[0][0] != paths[1][0]:
            print(e1, e2, paths)

        dir_to_dir[(e1, e2)] = sorted(paths)[0][1]


def get_dir(code):
    t = ''
    pre = 'A'
    code = pre+code
    for i in range(len(code)-1):
        t += dir_to_dir[(code[i], code[i+1])]
    return t


for e1 in directional:
    for e2 in directional:
        r1, c1 = directional[e1]
        r2, c2 = directional[e2]
        paths = []

        if not(c2 == 0 and r1 == 0):
            path = col_map[c2 - c1] + row_map[r2 - r1] + 'A'
            paths.append((len(get_dir(get_dir(get_dir(path)))), path))

        if not(r2 == 0 and c1 == 0):
            path = row_map[r2 - r1] + col_map[c2 - c1] + 'A'
            paths.append((len(get_dir(get_dir(get_dir(path)))), path))

        if len(paths) == 2 and paths[0][0] != paths[1][0]:
            print(e1, e2, paths)

        dir_to_dir[(e1, e2)] = sorted(paths)[0][1]


def get_dir(code):
    t = ''
    pre = 'A'
    code = pre+code
    for i in range(len(code)-1):
        t += dir_to_dir[(code[i], code[i+1])]
    return t

## manuell optimiert...
dir_to_dir = {('^', '^'): 'A',
              ('^', 'A'): '>A',
              ('^', '<'): 'v<A',  ### cannot be adjusted
              ('^', 'v'): 'vA',
              ('^', '>'): 'v>A',  ####  ('^', '>'): '>vA',
              ('A', '^'): '<A',
              ('A', 'A'): 'A',
              ('A', '<'): 'v<<A', ### cannot be adjusted
              ('A', 'v'): '<vA',  ###  ('A', 'v'): 'v<A',
              ('A', '>'): 'vA',
              ('<', '^'): '>^A',  ### cannot be adjusted
              ('<', 'A'): '>>^A', ### cannot be adjusted
              ('<', '<'): 'A',
              ('<', 'v'): '>A',
              ('<', '>'): '>>A',
              ('v', '^'): '^A',
              ('v', 'A'): '^>A', #('v', 'A'): '>^A',
              ('v', '<'): '<A',
              ('v', 'v'): 'A',
              ('v', '>'): '>A',
              ('>', '^'): '<^A', # ('>', '^'): '^<A',
              ('>', 'A'): '^A',
              ('>', '<'): '<<A',
              ('>', 'v'): '<A',
              ('>', '>'): 'A'}


def get_dir(code):
    t = ''
    pre = 'A'
    code = pre+code
    for i in range(len(code)-1):
        t += dir_to_dir[(code[i], code[i+1])]
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


ddd = door_dists.copy()

protected = [('1', 'A'), ('4', 'A'), ('7', 'A'), ('1', '0'), ('4', '0'), ('7', '0')]
protected = protected + [(b, a) for a, b in protected]

curr = float('inf') 
ddd = door_dists.copy()

for move, move_pattern in ddd.items():
    if len(set(move_pattern))>2:
        door_dists[move] = move_pattern[:-1][::-1] + 'A'

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
                t += dir_to_dir[(code[i], code[i+1])]

            d = defaultdict(int)
            while t:
                a_ind = t.index("A")
                d[t[:a_ind+1]] += 1
                t = t[a_ind+1:]
            
            pattern_map = {}
            for i in range(24):
                d_new = defaultdict(int)
                for pattern, n in d.items():
                    if pattern in pattern_map:
                        next_pattern = pattern_map[pattern]
                    else:
                        next_pattern = get_dir(pattern)
                        pattern_map[pattern] = next_pattern

                    while next_pattern:
                        a_ind = next_pattern.index("A")
                        d_new[next_pattern[:a_ind+1]] += n
                        next_pattern = next_pattern[a_ind+1:]
                d = d_new.copy()
                
            tot = 0
            for k in d:
                tot += len(k) * d[k]
            
            out += tot * int(code_copy[:-1])

        if out < curr and move not in protected:
            print(out, move, move_pattern, door_dists[move])
            curr = out
            ddd = door_dists.copy()

        door_dists = ddd.copy()

print(curr)