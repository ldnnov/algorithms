from collections import deque


def convert_num(num, to='dec'):
    helper = ['A', 'B', 'C', 'D', 'E', 'F']
    first_hex_char_num = 10

    if to == 'dec':
        num = num.upper()
        if num in helper:
            return helper.index(num) + first_hex_char_num
        return int(num)
    elif to == 'hex':
        if num >= first_hex_char_num:
            return helper[num - first_hex_char_num]
        return str(num)


num1 = deque(input("Insert first hexadecimal number: "))
num2 = deque(input("Insert second hexadecimal number: "))

hex_len = 16
total_sum = deque()
num1_length = len(num1)
num2_length = len(num2)

if num1_length < num2_length:
    num1.appendleft('0' * (num2_length-num1_length))
    max_len_of_num = num2_length
else:
    num2.appendleft('0' * (num1_length-num2_length))
    max_len_of_num = num1_length


num_in_mind = 0
for i in range(-1, -(max_len_of_num + 1), -1):
    dec_num1 = convert_num(num1[i])
    dec_num2 = convert_num(num2[i])

    dec_sum = dec_num1 + dec_num2 + num_in_mind

    if dec_sum >= hex_len:
        num_in_mind = 1
        dec_sum = dec_sum - hex_len
    else:
        num_in_mind = 0

    total_sum.appendleft(convert_num(dec_sum, to='hex'))

if num_in_mind:
    total_sum.appendleft(convert_num(num_in_mind, to='hex'))

print(f"Sum is: {''.join(total_sum)}")
