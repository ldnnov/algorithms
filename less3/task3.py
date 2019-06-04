import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f"Original: {array}")

idx_max = 0
idx_min = 0

for i, n in enumerate(array):
    if n > array[idx_max]:
        idx_max = i
    elif n < array[idx_min]:
        idx_min = i

array[idx_min], array[idx_max] = array[idx_max], array[idx_min]

print(f"Switched: {array}")
