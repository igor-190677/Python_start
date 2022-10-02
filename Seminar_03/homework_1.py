# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

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

def summa_number(list_numb):
    summ = 0
    for index in range(1, len(list_numb), 2):
        summ += list_numb[index]
    return summ


list_numbers = create_list()
print('Список пользователя:', list_numbers)
summa_numbers = summa_number(list_numbers)
print('Сумма нечетных чисел списка:', summa_numbers)