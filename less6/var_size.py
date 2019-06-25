"""
count_variables_size does not work properly with functions and classes

It can only work with variables like:
    string,
    number,
    one-dimensional list,
    flat dictionary

Total size of all variables calculates after the execution of script
(That's why we will se some interesting results).
"""

import sys
from types import ModuleType


def count_variables_size(module_name):

    total_size = 0
    mod = globals().get(module_name, None)

    module_vars = {key: value for key, value in mod.__dict__.items() if not key.startswith('__')}

    for var in module_vars.values():
        if isinstance(var, ModuleType):
            continue
        if isinstance(var, list):
            for value in var:
                total_size += sys.getsizeof(value)
        elif isinstance(var, dict):
            for key, value in var.items():
                total_size += sys.getsizeof(key)
                total_size += sys.getsizeof(value)
        else:
            total_size += sys.getsizeof(var)

    print(module_vars)
    print(f'Bytes total (except imported modules): {total_size}')


if __name__ == '__main__':
    from less6 import var1, var2, var3

    # Bytes total (except imported modules): 808

    # 9 variables with Integer type
    # 1 variable with List type (20 integers)

    # Just 808 bytes. I don't really know if that's a good thing or not.
    # Maybe it's OK for Python.
    count_variables_size('var1')
    print('*' * 80)

    # Bytes total (except imported modules): 1676

    # 6 variables with Integer type
    # 1 variable with List type (20 integers)
    # 1 variable with Dict type (1-20 integers as keys and the same for values)

    # increasing in size because of 'counters' dictionary,
    # but it is the fastest algorithm
    count_variables_size('var2')
    print('*' * 80)

    # Bytes total (except imported modules): 216

    # 8 variables with Integer type
    # 1 variable with List type (empty);
    #
    # variables removes from list in loop, so at the end it becomes empty.
    # results of this analysis are not quite correct.
    count_variables_size('var3')

