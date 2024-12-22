day, test = 22, 0
with open('in_' + str(day) + '_test' * test + '.txt') as file:
    data = file.read()

data = list(map(int, data.splitlines()))

def get_secret(secret, n):
    for i in range(n):
        secret = ((secret << 6) ^ secret) % 16777216
        secret = ((secret >> 5) ^ secret) 
        secret = ((secret << 11) ^ secret) % 16777216

    return secret

print(sum([get_secret(s, 2000) for s in data]))