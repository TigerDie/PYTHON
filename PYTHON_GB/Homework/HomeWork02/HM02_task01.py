# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

number = input('Введите вещественное число через запятую: ')
current = 0
for item in number:
    if item != ',':
        current += int(item)
print(f'{number} -> {current}')