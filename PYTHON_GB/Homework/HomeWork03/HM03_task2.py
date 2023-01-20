# Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

from random import randint as RI
my_list = [RI(1, 10) for _ in range(RI(1, 10))]
number = []
for i in range((len(my_list)// 2 + len(my_list) % 2)):
    new_number = my_list[i] * my_list[i - 1]
    number.append(new_number)
print(f'Полученный список: {my_list}\n Произведение пар чисел: {number}')