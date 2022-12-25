# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу
#  между максимальным и минимальным 
# значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
my_list = []
for _ in range(5):
    index = random.randint(0,3)
    my_list.append(round(random.uniform(0,10),index))
print(my_list)
numbers = []
for item in my_list:
    if isinstance(item, float):
        numbers.append(item % 1)
result = round(max(numbers)- min(numbers), 2)
print(f'Разница между дробными частями: {result}')