# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

def input_number():
    number_str = str(input('Введите число: '))
    if ',' in number_str:
        number_user_array = number_str.split(',')
        number_user_str = number_user_array[0] + number_user_array[1]
    elif '.' in number_str:
        number_user_array = number_str.split('.')
        number_user_str = number_user_array[0] + number_user_array[1]
    else:
        number_user_str = number_str
    return number_user_str

def definition_summ(number_string):
    summa = 0
    for number in number_string:
        summa += int(number)
    print('Сумма цифр в числе равна', summa)

number_user = input_number()
definition_summ(number_user)