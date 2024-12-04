day, test = 4, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read().splitlines()

t = 0

for r in range(len(data)):
    for c in range(len(data[0])):
        if data[r][c] != 'X':
            continue

        for r_o in [-1, 0, 1]:
            for c_o in [-1, 0, 1]:
                if not (0 <= r+r_o < len(data) and 0 <= c+c_o < len(data[0])) or data[r+r_o][c+c_o] != 'M':
                    continue

                if not (0 <= r+r_o*2 < len(data) and 0 <= c+c_o*2 < len(data[0])) or data[r+r_o*2][c+c_o*2] != 'A':
                    continue

                if not (0 <= r+r_o*3 < len(data) and 0 <= c+c_o*3 < len(data[0])) or data[r+r_o*3][c+c_o*3] != 'S':
                    continue
            
                t += 1

print(t)
