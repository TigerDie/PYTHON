# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет
a = int(input('Введите день недели: '))
if a >= 6 and a <= 7:
    print('Да')
else:
    print('Нет')