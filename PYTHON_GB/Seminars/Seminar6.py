# my_list = []                             # List complication (улучшение кода методом)

# for i in range(1,10):
#     my_list.append


# from random import randint as RI
# my_list = [RI(0,10) for i in range(10)]

# print(my_list)

# string = ' 1 2 3 45 5 6 78 96 345'
# # # string = string.split()
# # print(string)

# # # for i in range(len(string)):             # Map 
# # #     string[i] = int(string[i])

# # string = list(map(int, string))
# # print(string)

# def odd(x):                                  # Filter
#     if x % 2 != 0:
#         return x
# string = list(map(int, string.split()))
# print(string)
# string = list(filter(odd, string))
# print(string)

# string = ' 1 2 3 45 5 6 78 96 345'             # Enumerate

# string = string.split()
# # for item in string:
# #     print(item)

# # for i in range(len(string)):
# #     print(string[i])

# for i, item in enumerate(string):
#     print(f'Индекс {i}, элемент = {item}')

# string = ' 1 2 3 45 5 6 78 96 345'              # Zip

# nums = ' 1 2 3 4 5 6 7'
# letters = ' a b c d e f g'
# signs = ' + - # $ ^ & !'

# nums = nums.split()
# letters = letters.split()

# new_list = list(zip(nums, letters, signs))

# print(new_list)

# calc = {'Сложение': lambda x, y, z: x + y + z}                         # Lambda 

# print(calc.get('Сложение')(4, 5, 6))

# Задача  Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

# data = [1, 2, 3, 5, 1, 5, 3, 10]

# my_dict = dict()

# for i in range(len(data)):
#     my_dict[data[i]] = my_dict.get(data[i], 0) + 1
# print(my_dict)

# new_data = [x[0] for x in my_dict.items() if x[1] == 1]
# print(new_data)

# my_list = [1, 2, 3, 5, 1, 5, 3, 10]                    # Второй способ 

# my_dict = {}

# for item in my_list:
#     my_dict[item] = my_dict.get(item, 0) + 1

# for key, value in my_dict.items():
#     if value == 1:
#         print(key)

# my_list = [1, 2, 3, 5, 1, 5, 3, 10]                    # третий способ 

# proverka = lambda x: my_list.count(x) == 1
# new_data = filter(proverka, my_list)
# new_data = list(new_data)
# print(new_data)

# my_list = [1, 2, 3, 5, 1, 5, 3, 10]                                 # Четвертый способ
# new_data = list(filter(lambda x: my_list.count(x) == 1, my_list))
# print(new_data)

# my_list = [1, 2, 3, 5, 1, 5, 3, 10]                        # Пятый способ
# print([x for x in my_list if my_list.count(x) == 1])

# Задача 1 напишите программу вычисления арифмитического выражения заданного строкой. Используйте 
#          операции + - / * приоритет операции стандартный.     
# Пример: 2+2 = 4 , 1 + 2* 3 = 7; 1- 2* 3 = -5 

string_1 = '2+2'
string_2 = '1+2*3'
string_3 = '1-2*3'
string = string_2.replace('+', ' + ').replace('-',' - ').replace('/',' / ').replace('*', ' * ')
string = string.split()
print(string)

oper = {
    '+': lambda x, y: int(x) + int(y),
    '-': lambda x, y: int(x) - int(y),
    '/': lambda x, y: int(x) / int(y),
    '*': lambda x, y: int(x) * int(y)
}
def calc(string:list) -> int:
    for i in range(len(string)- 1):
        if string[i] in '*/':
            operation = string[i]
            left = string[i - 1]
            right = string[i + 1]
            res = oper[operation](left, right)
            print(f'Результат операции {left} {operation} {right} = {res} ')
            return string[: i - 1] + [str(res)] + string[i + 1:]
    for j in range(len(string) - 1):
        if string[j] in '+-' and j != 0:
            operation = string[j]
            left = string[j - 1]
            right = string[j+ 1]
            res = oper[operation](left, right)
            print(f'Результат операции {left} {operation} {right} = {res} ')
            return string[: j - 1] + [str(res)] + string[j + 2:]

for item in oper.keys():
    while item in string:
        string = calc(string)
print(string[0])
