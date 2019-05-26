n = int(input("Введите натуральное число: "))

sum = 0
cur_num = 1

while n > 0:
    sum += cur_num
    cur_num /= -2
    n -= 1

print(f"Сумма ряда: {sum}")