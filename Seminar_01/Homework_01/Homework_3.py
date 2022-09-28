# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def input_coordinate():
    flag = False
    while flag == False:
        try:
            coordinate = int(input())
            flag = True
        except ValueError:
            print("Это не число!")
    return coordinate

def definition_quarter(coord_x, coord_y):
    if coord_x > 0 and coord_y > 0:
        quarter = 1
    if coord_x < 0 and coord_y > 0:
        quarter = 2
    if coord_x < 0 and coord_y < 0:
        quarter = 3
    if coord_x > 0 and coord_y < 0:
        quarter = 4        
    print('Точка находится в четверти', quarter)


print('Введите координату Х: ',end='')
coordinate_x = input_coordinate()
print('Введите координату Y: ',end='')
coordinate_y = input_coordinate()
definition_quarter(coordinate_x, coordinate_y)