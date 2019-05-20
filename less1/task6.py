pos = int(input("Введите порядковый номер буквы английского алфавита: "))

if pos > 26 or pos < 1:
    print("Неправильное значение")
else:
    letters_from = ord('a') - 1
    char = chr(pos + letters_from)
    print(f"Буква: {char}")
