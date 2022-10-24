# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

import math 

def prime_factors(number):
    list_prime_factors = []
    while number % 2 == 0: 
        list_prime_factors.append(2)
        number = number / 2 
    for i in range(3, int(math.sqrt(number)) + 1, 2): 
        while number % i == 0: 
            list_prime_factors.append(i) 
            number = number / i 
    if number > 2: 
        list_prime_factors.append(number)
    return list_prime_factors
 
number_user = int(input('Введите число: '))
print('Список простых множителей', prime_factors(number_user))
