import random


def get_median(size_value):

    array_length = 2 * size_value + 1
    half_length = array_length // 2
    array = [random.randint(10, 99) for _ in range(array_length)]

    print(f"\nGenerated array {array}")
    print(f"Array size: {array_length}")
    print("-" * 30)

    median = None
    n = 0
    while n < array_length:
        bigger = 0
        smaller = 0
        tmp_median = array[n]

        for idx, val in enumerate(array):
            if tmp_median > val:
                bigger += 1
            elif tmp_median < val:
                smaller += 1

        if bigger == smaller or (bigger <= half_length and smaller <= half_length):
            median = tmp_median
            break

        n += 1

    if median:
        print(f"Array median is: {median}")
    else:
        print("Something goes wrong. Median is not found.")

    # uncomment for debug
    # array.sort()
    # print(f"\nGenerated array {array}")


m = int(input("Insert natural number: "))
get_median(m)
