import random


def choice(data):
    length = len(data)
    pos = random.randrange(0, length, 1)
    return data[pos]


R = [i * i for i in range(15)]
ans = choice(R)
print(ans)
