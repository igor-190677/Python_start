# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

import random

def print_list_file(path):
    print('Список элементов из файла file.txt:')
    data = open(path, 'r')
    for line in data:
        print(line)
    data.close()

def fill_list(path, number_items):
    with open(path, 'w') as data:
        for item in range(number_items):
            number = int(random.randrange(-number_items, number_items))
            data.write(str(number) + '\n')

def sum_items_list(path):
    summa_items = 0
    data = open(path, 'r')
    for line in data:
        summa_items += int(line)
    data.close()
    return summa_items


number_items_list = int(input('Введите число элементов N: '))

path = 'file.txt'
fill_list(path, number_items_list)
print()
print_list_file(path)
sum_items = sum_items_list(path)

print('Сумма элементов списка из файла равна', sum_items)

