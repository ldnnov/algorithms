def sum(n):
	if len(str(n)) == 1:
		return n
	else:
		return sum(n // 10) + n % 10
		
n_max = 0
sum_max = 0

while True:

    n = int(input("Введите натуральное число (0 завершит программу): "))
    
    if n == 0:
        break
    
    summ = sum(int(n))
    
    if sum_max < summ:
        n_max = n
        sum_max = summ

print(f"Наибольшее число по сумме: {n_max}. Сумма: {sum_max}")
