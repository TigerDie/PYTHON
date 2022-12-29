# 3. Создайте словать заданный по формуле 3*n+1, где n это ключ,
#  а формула значение

# *Пример:*

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# my_dict = {}

# number = int(input('Введитет целое число: '))

# for n in range(1, number + 1):
#     my_dict[n] = 3*n + 1

# print(my_dict)

# my_string = 'Питон самый лучший язык в мире'

# # my_string = my_string.split('и')  #  split удаляет # replace заменяет 
# my_list = ['1', '4', '6', '784',]
# print('-'.join(my_list))
# print(my_string.lower().startswith('пит'))
# print(my_string.lower().endswith('ире'))
# print(my_string)

# Найдите корни квадратного уравнения 
# Ax² + Bx + C = 0 с помощью математических формул 
# нахождения корней квадратного уравнения

# equation = '3*x**2 + 5*x - 6 = 0'

# # a = 3
# # b = 5
# # c = -6
# equation = equation.replace('x**2', '')
# equation = equation.replace('x', '')
# equation = equation.replace('*', '')
# equation = equation.rstrip()
# equation = equation.split(' ')
# a = int(equation[0])
# b = int(equation[2])
# c = int(equation[4])
# if equation[2] == '-':
#     b *= -1
# if equation[3] == '-':
#     c *= -1
# print(f' a = {a}, b = {b}, c= {c}')
# discriminant = b**2 - 4 * a * c
# def function (d):
#     if d < 0:
#         return('Решений нет')
#     elif d == 0:
#         return(-(b/(2*a)))
#     else:
#         return  [round((-b +(d)**0.5)/(2*a),3),round((-b -(d)**0.5)/(2*a),3)]
# z = function(discriminant)
# print(z)
import math
equation = 'x ** 2 -   x *6  =  0'
def create_koef(equation: str):
    new_equation = equation.replace(' ', '').replace('=0', '') \
        .replace('+', ' ').replace('-', ' -')
    new_equation = new_equation.split()
    new_list = []
    for item in new_equation:
        if item.startswith('x'):
            new_list.append(1)
        elif item.startswith('-x'):
            new_list.append(-1)
        else:
            new_list.append(item.split('*x'[0]))
    return new_list

def solve_equation(koef):
    a, b, c = int(koef[0]), int(koef[1]), int(koef[2])
    disc = b**2 - 4 * a * c
    if disc > 0:
        x1 = (- b - math.sqrt(disc))/ (2*a)
        x2 = (- b + math.sqrt(disc))/ (2*a)
        return round(x1, 2) , round(x2, 2)
    elif disc == 0:
        x = (- b - math.sqrt(disc))/ (2*a)
        return round(x, 2)
    else:
        return None
print(create_koef(equation))
print(solve_equation(create_koef(equation)))