# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
#  максимум использование библиотеки Random для и получения случайного int

from random import randint as RI

my_first_list = [RI(1, 50) for _ in range(1, 10)]
my_second_list = my_first_list.copy()
for i in range(len(my_second_list)):
    j = RI(0, (len(my_second_list) - 1))
    if i != j:
        my_second_list[i], my_second_list[j] = my_second_list[j], my_second_list[i]
print(f'Созданный список: {my_first_list}')
print(f'Перемешанный список: {my_second_list}')