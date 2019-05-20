char1 = input("Введите первую строчную букву английского алфавита: ")
char2 = input("Введите вторую строчную букву английского алфавита: ")

letters_from = ord('a') - 1
pos_char1 = ord(char1) - letters_from
pos_char2 = ord(char2) - letters_from
count_between = abs(pos_char2 - pos_char1 - 1)

print(f"Позиция первой буквы: {pos_char1}")
print(f"Позиция второй буквы: {pos_char2}")
print(f"Количество букв между: {count_between}")
