from collections import defaultdict

day, test = 22, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read()

data = list(map(int, data.splitlines()))

def get_secret_list(secret, n):
    res = [secret % 10]
    for i in range(n-1):
        secret = ((secret << 6) ^ secret) % 16777216
        secret = ((secret >> 5) ^ secret) 
        secret = ((secret << 11) ^ secret) % 16777216

        res.append(secret % 10)
    return res

summary = defaultdict(int)

for secret in data:
    q = (get_secret_list(secret, 2000))
    seen = set()
    for i in range(len(q)-4):
        a, b, c, d = q[i+1] - q[i+0], q[i+2] - q[i+1], q[i+3] - q[i+2], q[i+4] - q[i+3]
        if (a, b, c, d) in seen: continue
        seen.add((a, b, c, d))
        summary[(a, b, c, d)] += q[i+4]

print(max(summary.values()))


