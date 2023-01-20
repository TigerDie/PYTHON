# В файле находится N натуральных чисел, записанных
#  через пробел.
# Среди чисел не хватает одного, 
# чтобы выполнялось условие
# A[i] - 1 = A[i-1]. Найдите это число.
# data = '1 2 3 4 5 6 8 9 11'
# data = list(map(int, data.split()))

# my_func = list(filter(lambda i: not
# data[i] + 1 == data[i+ 1], range(len(data) - 1)))

# for item in my_func:
#     print(data[item]+ 1)

# Дан список чисел. Создайте список, в который попадают
#  числа, описываемые возрастающую последовательность.
#  Порядок элементов менять нельзя.
# *Пример:*
# 1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или
#  [1, 6, 7] и т.д.

data = [1, 5, 2, 3, 4, 6, 1, 7]
result = []
count = 0
num1 = 1
while count < len(data):
    for i in range(len(data) - 1):
        temp = []
        temp.append(data[i])
        cur_max = data[i]
        for j in range(num1, len(data)):
            if data[j] > cur_max:
                temp.append(data[j])
                cur_max = data[j]
        if len(temp) > 1 and temp not in result:
                result.append(temp)
    count += 1
    num1 += 1
print(result)

#написать программу, удаляющая из текста все слова, содержащие 'абв'

# from string import punctuation 
# my_str = 'АБВ ылоады фыадлы абв? 3ошолдаф вабвв ффлха абВ'
# res = []

# x = 'абв'
# for c in punctuation:
#     my_str = my_str.replace(c, ' ' + c + ' ')
# data = my_str.split()
# print(data)

# for item in data:
#     if not x.lower() in item.lower():
#         res.append(item)
# res = ' '.join(res)

# for c in punctuation:
#     res = res.replace(' ' + c, c)
# print(res)

