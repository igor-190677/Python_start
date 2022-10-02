# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def definition_binary_number(number_dec):
    if (number_dec == 0):
        return 1
    digital = number_dec % 2
    list_number_binary.append(digital)
    definition_binary_number(number_dec // 2)

list_number_binary = []
number_decimal = int(input('Введите десятичное число: '))

definition_binary_number(number_decimal)
list_number_binary.reverse()

print('Двоичния запись числа: ', end='')
for dig in list_number_binary:
    print(dig, end='')