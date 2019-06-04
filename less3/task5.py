import random

SIZE = 20
MIN_ITEM = -20
MAX_ITEM = 20
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

result_num = MIN_ITEM
for n in array:
    if 0 > n > result_num:
        result_num = n

print(f"Result number is {result_num}")
