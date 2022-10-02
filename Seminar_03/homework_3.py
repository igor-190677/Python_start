# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def definition_difference(list_number):
    remainder = round((list_number[0] - int(list_number[0])),2)
    min = remainder
    max = remainder
    for index in range(1, len(list_number)):
        remainder = round((list_number[index] - int(list_number[index])),2)
        if remainder > max and remainder != 0: max = remainder
        if remainder < min and remainder != 0: min = remainder
    print('Разница между максимальным и минимальным значением дробной части элементов равна', max - min)

list_numbers = [1.1, 1.2, 3.1, 5, 10.01]
print('Список вещественных чисел:', list_numbers)
definition_difference(list_numbers)
