# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

def input_quarter():
    quarter = str(input('Введите номер четверти координатной плоскости: '))
    while quarter not in ('1', '2', '3', '4'):
        print('Нужно ввести число от 1 до 4!')
        quarter = str(input('Введите номер четверти координатной плоскости: '))
    return quarter    

def definition_range(quart):
    if quart == '1':
        print('Диапазон координат точки для первой четверти')
        print('0 < x < ꝏ')
        print('0 < y < ꝏ')
    elif quart == '2':
        print('Диапазон координат точки для второй четверти')
        print('0 < x < -ꝏ')
        print('0 < y < ꝏ')
    elif quart == '3':
        print('Диапазон координат точки для третьей четверти')
        print('0 < x < -ꝏ')
        print('0 < y < -ꝏ')
    else:
        print('Диапазон координат точки для четвертой четверти')
        print('0 < x < ꝏ')
        print('0 < y < -ꝏ')


quarter = input_quarter()
definition_range(quarter)