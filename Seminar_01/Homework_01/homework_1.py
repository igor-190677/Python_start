# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def input_number():
    day = False
    while day == False:
        try:
            numb_day = int(input('Ведите номер дня недели: '))
            day = True
        except ValueError:
            print("Это не число!")
        if day == True and (numb_day <= 0 or numb_day >= 8):
            print('Число должно быть в диапазоне от 1 до 7!')
            day = False
    return numb_day

def check_number_day(number_day):
    if number_day == 6 or number_day == 7:
        print('День является выходным')
    else:
        print('День не является выходным') 

number_day = input_number()
check_number_day(number_day)