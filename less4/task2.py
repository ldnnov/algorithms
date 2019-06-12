import cProfile


# variant 1
# O(?) but wiki tells that it's O(n log(log n))
# python3 -m timeit -n 100 -s 'import less4.task2' 'less4.task2.eratosthenes(20)'
# python3 -m timeit -n 100 -s 'import less4.task2' 'less4.task2.eratosthenes(40)'
# python3 -m timeit -n 100 -s 'import less4.task2' 'less4.task2.eratosthenes(80)'
# python3 -m timeit -n 100 -s 'import less4.task2' 'less4.task2.eratosthenes(160)'
# python3 -m timeit -n 100 -s 'import less4.task2' 'less4.task2.eratosthenes(380)'
# results:
# 100 loops, best of 3: 233 usec per loop
# 100 loops, best of 3: 1.04 msec per loop
# 100 loops, best of 3: 4.66 msec per loop
# 100 loops, best of 3: 20.5 msec per loop
# 100 loops, best of 3: 35.5 msec per loop
def eratosthenes(n):
    if n == 1:
        return 2

    max_len = n**2
    primes_count = 0
    deck = [i for i in range(max_len)]
    deck[1] = 0

    for i in range(2, max_len):
        if deck[i] != 0:
            primes_count += 1
            if primes_count == n:
                return deck[i]
            j = i + i
            while j < max_len:
                deck[j] = 0
                j += i


# variant 2
# O(n^2) and works too slow with argument's big number, let's check it with cProfile! (see below)
# python3 -m timeit -n 100 -s 'import less4.task2' 'less4.task2.my_sieve(20)'
# python3 -m timeit -n 100 -s 'import less4.task2' 'less4.task2.my_sieve(40)'
# python3 -m timeit -n 100 -s 'import less4.task2' 'less4.task2.my_sieve(80)'
# python3 -m timeit -n 100 -s 'import less4.task2' 'less4.task2.my_sieve(160)'
# python3 -m timeit -n 100 -s 'import less4.task2' 'less4.task2.my_sieve(380)'
# results:
# 100 loops, best of 3: 128 usec per loop
# 100 loops, best of 3: 709 usec per loop
# 100 loops, best of 3: 3.81 msec per loop
# 100 loops, best of 3: 21.6 msec per loop
# 100 loops, best of 3: 178 msec per loop
def my_sieve(n):
    primes = [2]

    i = 3
    while len(primes) < n:
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
        if is_prime:
            primes.append(i)
        i += 1
    return primes[n-1]


if __name__ == '__main__':
    print('=' * 80)
    print('eratosthenes function\n')
    # print(eratosthenes(380))
    cProfile.run('eratosthenes(380)')
    print('=' * 80)
    print()
    print('=' * 80)
    print('my_sieve function\n')
    # print(my_sieve(380))
    cProfile.run('my_sieve(380)')
    print('=' * 80)

# ================================================================================
# eratosthenes function
#
#          5 function calls in 0.039 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.039    0.039 <string>:1(<module>)
#         1    0.032    0.032    0.038    0.038 task2.py:15(eratosthenes)
#         1    0.006    0.006    0.006    0.006 task2.py:21(<listcomp>)
#         1    0.000    0.000    0.039    0.039 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# ================================================================================
#
# ================================================================================
# my_sieve function
#
#          2999 function calls in 0.184 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.184    0.184 <string>:1(<module>)
#         1    0.184    0.184    0.184    0.184 task2.py:47(my_sieve)
#         1    0.000    0.000    0.184    0.184 {built-in method builtins.exec}
#      2616    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       379    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# ================================================================================

# We can see that my_sieve function calls 'len' and 'append' methods too much times!
# So, Eratosthenes algorithm is faster than my own method.
