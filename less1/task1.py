n = int(input("Введите целое трехзначное число: "))

a = n // 100 % 10
b = n // 10 % 10
c = n % 10

print(f"Сумма чисел: {a + b + c}")
print(f"Произведение чисел: {a * b * c}")
