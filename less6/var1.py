import random


SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 20
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
# print(array)

num = array[0]
max_count = 0
for idx, n in enumerate(array):
    count = 1
    for j in array[idx+1:]:
        if n == j:
            count += 1
    if count > max_count:
        max_count = count
        num = n

# print(f"Number {num}: {max_count} times")
