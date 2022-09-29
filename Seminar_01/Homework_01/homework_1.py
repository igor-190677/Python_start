# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def input_number():
    numb_day = str(input('Ведите номер дня недели: '))
    while numb_day not in ('1', '2', '3', '4', '5', '6', '7'):
        print('День недели должен быть записан числом от 1 до 7!')
        numb_day = str(input('Ведите номер дня недели: '))
    return numb_day

def check_number_day(number_day):
    if number_day in ('6', '7'):
        print('День является выходным')
    else:
        print('День не является выходным') 

number_day = input_number()
check_number_day(number_day)