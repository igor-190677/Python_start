# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def find_return_number(old_list):
    new_list = []
    new_list.append(int(old_list[0]))
    for i in range(1, len(old_list)):
        if int(old_list[i]) not in new_list:
            new_list.append(int(old_list[i]))
    return new_list

list = input('Введите список чисел через запятую без пробелов:').split(',')
print(find_return_number(list))
