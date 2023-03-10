# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, 
# стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint as RI
my_list = [RI(1, 10) for _ in range(RI(1, 10))]
position = 0
for i in range(1, len(my_list), 2):
    position += my_list[i]
print(f'Полученный список: {my_list}\n Cумма элементов нечетного индекса: {position}')
