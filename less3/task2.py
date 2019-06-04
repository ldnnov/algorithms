import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

res = []

for idx, val in enumerate(array):
    if val % 2 == 0:
        res.append(idx)

print(res)
