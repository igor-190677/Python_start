# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import math

def create_list():
    list_numbers_new = []
    number_items = int(input('Введите количество элементов: '))
    for index in range(number_items):
        flag = False
        while flag == False:
            try:
                number = int(input('Введите целое число: '))
                list_numbers_new.append(number)
                flag = True
            except ValueError:
                print("Это не число!")
    return list_numbers_new

def definition_multiplication(list_numb):
    list_multiplictions_number = []
    for index in range(math.ceil(len(list_numb) / 2)):
        list_multiplictions_number.append(list_numb[index] * list_numb[-1 * (index + 1)])
    return list_multiplictions_number


list_numbers = create_list()
print('Список пользователя: ', list_numbers)
list_multiplictions = definition_multiplication(list_numbers)
print('Произведения пар чисел списка', list_multiplictions)

