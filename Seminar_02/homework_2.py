# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def input_number_factorials():
    number_factorials = int(input('Введите число N: '))
    array_results = []
    for numb in range(number_factorials):
        array_results.append(calculating_factorial(numb + 1))
    print('Результаты:', array_results)

def calculating_factorial(number):
    if number == 1:
        return 1
    else:
        return number*calculating_factorial(number-1)

input_number_factorials()