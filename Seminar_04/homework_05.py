# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.


def print_poly(path):
    koeff_poly = []
    data = open(path, 'r')
    for line in data:
        if line != '':
            koeff_poly.append(int(line))
    data.close()

    if koeff_poly[0] == 1:
        print('x^2', end='')
    elif koeff_poly[0] == -1:
        print('-x^2', end='')
    elif koeff_poly[0] != 0:
        print(str(koeff_poly[0]) + '*x^2', end='')
    
    if koeff_poly[1] == 1:
        print('+x', end='')
    elif koeff_poly[1] == -1:
        print('-x', end='')
    elif koeff_poly[1] > 1:
        print('+' + str(koeff_poly[1]) + '*x', end='')
    elif koeff_poly[1] < -1:
        print(str(koeff_poly[1]) + '*x', end='')

    if koeff_poly[2] > 0:
        print('+' + str(koeff_poly[2]))
    elif koeff_poly[2] < 0:
        print(str(koeff_poly[2]))


def fill_file(path):
    with open(path, 'w') as data:
        for item in range(3):
            koeff = str(input('Введите коэффициент ' + str(item + 1) + ': '))
            data.write(koeff + '\n')

def sum_poly(path_1, path_2, path_3):
    koeff_poly_1 = []
    koeff_poly_2 = []
    data = open(path_1, 'r')
    for line in data:
        if line != '':
            koeff_poly_1.append(int(line))
    data.close()
    data = open(path_2, 'r')
    for line in data:
        if line != '':
            koeff_poly_2.append(int(line))
    data.close()
    with open(path3, 'w') as data:
        for index in range(3):
            koeff = koeff_poly_1[index] + koeff_poly_2[index]
            data.write(str(koeff) + '\n')


path1 = 'poly_1.txt'
path2 = 'poly_2.txt'
path3 = 'sum_poly.txt'
print('Введите коэффициенты k1, k2, k3 для первого полинома вида k1*x^2 + k2*x + k3')
fill_file(path1)
print('Введите коэффициенты k1, k2, k3 для второго полинома вида k1*x^2 + k2*x + k3')
fill_file(path2)
sum_poly(path1, path2, path3)
print('Первый полином:')
print_poly(path1)
print('Второй полином:')
print_poly(path2)
print('Сумма полиномов:')
print_poly(path3)