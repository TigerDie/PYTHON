# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.
from random import randint

def info(name):
    a = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while a < 1 or a > 28:
        if a > 28:
            a = int(input(f"{name}, нельзя брать больше 28 конфет: "))
        elif a < 1:
            a = int(input(f"{name}, вы не можете пропустить ход, возьмите хотя бы одну конфету "))
    return a

def step(name, k, candy, value):
    print(
        f"Ходил {name}, он взял {k}, теперь у него {candy}. Осталось на столе {value} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = int(input("Введите количество конфет на столе: "))
flag = randint(0, 2)  # флаг очередности
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

candy1 = 0
candy2 = 0

while value > 28:
    if flag:
        k = info(player1)
        candy1 += k
        value -= k
        flag = False
        step(player1, k, candy1, value)
    else:
        k = info(player2)
        candy2 += k
        value -= k
        flag = True
        step(player2, k, candy2, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")