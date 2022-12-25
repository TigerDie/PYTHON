# Задайте число. Составьте список чисел Фибоначчи,
#  в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# Негафибоначчи

k = int(input('Введите число: '))
my_list1, my_list2 = [0, 1], [1]
number1, number2, number_1, number_2 = 0, 1, 0, 1
for _ in range(k - 1):
    number1, number2 = number2, number1 + number2
    my_list1.append(number2)
    number_1, number_2 = number_2, number_1 - number_2
    my_list2.append(number_2)
my_list2.reverse()
my_list = my_list2.copy()
my_list.extend(my_list1)
print(f' k = {k} \n {my_list}')
