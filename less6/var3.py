import random


SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 20
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
# print(array)

max_count = 0
num = None

cur_count = 0
cur_num = array[0]

while len(array) > 0:
    try:
        idx = array.index(cur_num)
        cur_count += 1
        del array[idx]
    except ValueError:
        if cur_count > max_count:
            max_count = cur_count
            num = cur_num
        cur_count = 0
        cur_num = array[0]

# if num is not None:
#     print(f"Number {num}: {max_count} times")
# else:
#     print("All numbers are unique")
