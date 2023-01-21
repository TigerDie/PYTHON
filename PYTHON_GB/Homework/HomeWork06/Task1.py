# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
#  в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# x = (int(input('Введите координату точки X: ')))          # Старое решение 
# y = (int(input('Введите координату точки Y: ')))
# if x > 0 and y > 0:
#     print(f"{ x =  } ; { y =  } -> 1 четверть")
# elif x < 0 and y > 0:
#     print(f"{ x =  } ; { y =  } -> 2 четверть") 
# elif x < 0 and y < 0:
#     print(f"{ x =  } ; { y =  } -> 3 четверть")
# else:
#     print(f"{ x =  } ; { y =  } -> 4 четверть") 

x, y = map(int, input('Введите координату точки X , Y через пробел: ').split())     # Новое решение
if x > 0 and y > 0:
    print(f"{ x =  } ; { y =  } -> 1 четверть")
elif x < 0 and y > 0:
    print(f"{ x =  } ; { y =  } -> 2 четверть") 
elif x < 0 and y < 0:
    print(f"{ x =  } ; { y =  } -> 3 четверть")
else:
    print(f"{ x =  } ; { y =  } -> 4 четверть")