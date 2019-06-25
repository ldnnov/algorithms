import random


SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 20
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
# print(array)

counters = {}
num = None
max_count = 1

for i in array:
    if i not in counters:
        counters[i] = 1
    else:
        counters[i] += 1

    if counters[i] > max_count:
        max_count = counters[i]
        num = i

# if num is not None:
#     print(f"Number {num}: {max_count} times")
# else:
#     print("All numbers are unique")
