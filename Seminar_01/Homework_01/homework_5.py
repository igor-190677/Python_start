# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math

def input_points():
    points = {}
    for point in range(2):
        if point == 0:
            print('Введите координаты точки А:')
        else:
            print('Введите координаты точки B:')
        for coordinate in range(2):
            if coordinate == 0:
                points[point, coordinate] = int(input('X: '))
            else:
                points[point, coordinate] = int(input('Y: '))
    return points

def definition_length(points_array):
    length = math.sqrt(pow((points_array[0, 0] - points_array[1, 0]), 2) + pow((points_array[0, 1] - points_array[1, 1]), 2))
    print('Длина отрезка АВ равна', math.floor(length * 100) / 100)
    
array_points = input_points()
definition_length(array_points)