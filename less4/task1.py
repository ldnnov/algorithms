# import random
#
# SIZE = 20
# MIN_ITEM = 0
# MAX_ITEM = 20
# array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
# print(array)


# variant 1
# O(n^2), the slowest realization because of two loops

# python3 -m timeit -n 10000 -s 'import less4.task1, random' 'less4.task1.max_count_first([random.randint(0, 20) for _ in range(50)])'
# python3 -m timeit -n 10000 -s 'import less4.task1, random' 'less4.task1.max_count_first([random.randint(0, 20) for _ in range(100)])'
# python3 -m timeit -n 10000 -s 'import less4.task1, random' 'less4.task1.max_count_first([random.randint(0, 20) for _ in range(200)])'
# results:
# 10000 loops, best of 3: 119 usec per loop
# 10000 loops, best of 3: 315 usec per loop
# 10000 loops, best of 3: 315 usec per loop

def max_count_first(arr):
    num = arr[0]
    max_count = 0
    for idx, n in enumerate(arr):
        count = 1
        for j in arr[idx+1:]:
            if n == j:
                count += 1
        if count > max_count:
            max_count = count
            num = n
    # print(f"Number {num}: {max_count} times")
    return num, max_count


# variant 2
# O(n), the best realization

# python3 -m timeit -n 10000 -s 'import less4.task1, random' 'less4.task1.max_count_second([random.randint(0, 20) for _ in range(50)])'
# python3 -m timeit -n 10000 -s 'import less4.task1, random' 'less4.task1.max_count_second([random.randint(0, 20) for _ in range(100)])'
# python3 -m timeit -n 10000 -s 'import less4.task1, random' 'less4.task1.max_count_second([random.randint(0, 20) for _ in range(200)])'
# results:
# 10000 loops, best of 3: 71.8 usec per loop
# 10000 loops, best of 3: 142 usec per loop
# 10000 loops, best of 3: 284 usec per loop

def max_count_second(arr):
    counters = {}
    num = None
    max_count = 1

    for i in arr:
        if i not in counters:
            counters[i] = 1
        else:
            counters[i] += 1

        if counters[i] > max_count:
            max_count = counters[i]
            num = i

    if num is not None:
        # print(f"Number {num}: {max_count} times")
        return num, max_count
    else:
        # print("All numbers are unique")
        return None, None


# variant 3
# O(n) by time but O(n^2) by realization: arr.index(cur_num) is a loop (optimised),
# not so bad by speed but slower and uglier than variant 2

# python3 -m timeit -n 10000 -s 'import less4.task1, random' 'less4.task1.max_count_third([random.randint(0, 20) for _ in range(50)])'
# python3 -m timeit -n 10000 -s 'import less4.task1, random' 'less4.task1.max_count_third([random.randint(0, 20) for _ in range(100)])'
# python3 -m timeit -n 10000 -s 'import less4.task1, random' 'less4.task1.max_count_third([random.randint(0, 20) for _ in range(200)])'
# results:
# 10000 loops, best of 3: 104 usec per loop
# 10000 loops, best of 3: 215 usec per loop
# 10000 loops, best of 3: 486 usec per loop

def max_count_third(arr):
    max_count = 0
    num = None

    cur_count = 0
    cur_num = arr[0]

    while len(arr) > 0:
        try:
            idx = arr.index(cur_num)
            cur_count += 1
            del arr[idx]
        except ValueError:
            if cur_count > max_count:
                max_count = cur_count
                num = cur_num
            cur_count = 0
            cur_num = arr[0]

    if num is not None:
        # print(f"Number {num}: {max_count} times")
        return num, max_count
    else:
        # print("All numbers are unique")
        return None, None


# print(max_count_first(array))
# print(max_count_second(array))
# print(max_count_third(array))
