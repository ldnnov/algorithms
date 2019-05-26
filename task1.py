while True:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    op = input("Введите операцию: ")
    
    if op == '0':
        break
    elif op == '+':
        print(f"сумма: {a + b}")
    elif op == '-':
        print(f"разность: {a - b}")
    elif op == '*':
        print(f"произведение: {a * b}")
    elif op == '/':
        if b == 0:
            print("деление на ноль")
        else:
            print(f"деление: {a / b}")
    else:
        print("операция недоступна")