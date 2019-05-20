year = int(input("Введите год: "))

if year % 400 == 0:
    print("Это високосный год")
else:
    if year % 100 == 0:
        print("Это не високосный год")
    elif year % 4 == 0:
        print("Это високосный год")
    else:
        print("Это не високосный год")
