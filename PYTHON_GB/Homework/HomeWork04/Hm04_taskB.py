# B. Даны два файла, в каждом из которых находится запись многочлена.
#  Задача - сформировать файл, содержащий сумму многочленов.

from random import randint as RI
import itertools

k = int(input('Задайте натуральную степень многочлена k: '))

def get_ratio(k):
    ratio = [RI(0, 10) for i in range(k + 1)]
    while ratio[0] == 0:
        ratio[0] = RI(1, 10)
    return ratio

def get_polynomial(k, ratio):
    var = ['*x**'] * (k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c in itertools.zip_longest
    (ratio, var, range(k, 1, -1), fillvalue='') if a != 0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x',' x')

ratio = get_ratio(k)
polynom = get_polynomial(k, ratio)
print(polynom)

m = int(input('Задайте натуральную степень второго многочлена m: '))

second_polynom = get_polynomial(m, ratio)
print(second_polynom)