# Задайте список из n чисел последовательности (1 + 1/n)^n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

n = int(input('Введите число: '))
current = 0
my_list = []
for i in range(1, n + 1):
    number = round((1 + 1 / i)**i,3)
    if number - int(number) == 1:
        number = int(number)
    else:
        number = round(number, 2)
        my_list.append(number)
        current += number
print(f'n = {n} -> {my_list}\n Сумма {current}')
