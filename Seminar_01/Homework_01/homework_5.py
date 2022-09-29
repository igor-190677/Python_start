# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math

def input_points():
    points = {}
    for point in 'A', 'B':
        if point == 'A':
            ax = int(input(f'Введите координату X точки {point}: '))
            ay = int(input(f'Введите координату Y точки {point}: '))
        else:
            bx = int(input(f'Введите координату X точки {point}: '))
            by = int(input(f'Введите координату Y точки {point}: '))
    return ax, ay, bx, by

def definition_length(a1, a2, b1, b2):
    length = math.sqrt(pow((a1 - b1), 2) + pow((a2 - b2), 2))
    print('Длина отрезка АВ равна', math.floor(length * 100) / 100)
    
ax, ay, bx, by = input_points()
definition_length(ax, ay, bx, by)