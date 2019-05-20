x1 = float(input("Введите координату X первой точки: "))
y1 = float(input("Введите координату Y первой точки: "))
x2 = float(input("Введите координату X второй точки: "))
y2 = float(input("Введите координату Y второй точки: "))

k = (y2 - y1) / (x2 - x1)
b = y1 - k * x1

if k == 1:
    kx = 'x'
elif k == -1:
    kx = '-x'
else:
    kx = f"{k}x"

if b == 0:
    print(f"y = {kx}")
elif b > 0:
    print(f"y = {kx} + {b}")
else:
    print(f"y = {kx} - {abs(b)}")
