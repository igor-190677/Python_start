# Реализуйте алгоритм перемешивания списка.

import random

def fill_list(number_items):
    list_number = []
    for item in range(number_items):
        list_number.append(int(random.randrange(1, 100)))
    return list_number

def mix_items_list(list_numbers):
    new_list = list_numbers[:]
    for index in range(len(new_list)):
        number = int(random.randrange(0, len(new_list) - 1))
        new_list[number], new_list[number + 1] = new_list[number + 1], new_list[number]
    return new_list


number_items_list = int(input('Введите число элементов списка: '))

list_numbers = []
list_numbers_new = []
list_numbers = fill_list(number_items_list)
print(list_numbers)
list_numbers_new = mix_items_list(list_numbers)
print(list_numbers_new)
