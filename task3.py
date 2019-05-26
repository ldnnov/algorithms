a = int(input("Введите натуральное число: "))

def revert(a):
	if len(str(a)) == 1:
		return str(a)
	return str(a % 10) + revert(a // 10)

print(revert(a))