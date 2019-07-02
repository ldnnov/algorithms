import random


def reverse_bubble_sort(arr):
    n = 1
    arr_len = len(arr)
    while n < arr_len:
        is_sorted = True

        for i in range(arr_len - n):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False

        if is_sorted:
            break

        n += 1

        # for debug
        # print(arr)


array = [random.randint(-100, 99) for _ in range(10)]
print(array)
print('-' * 20)

reverse_bubble_sort(array)

print('-' * 20)
print(array)
