# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def number_fibonacci(number):
    if number >= 0:
        list_number_fibonacci = [0, 1]
        for numb in range(2, number + 1):
            list_number_fibonacci.append(list_number_fibonacci[numb - 1] + list_number_fibonacci[numb - 2]) 
        return list_number_fibonacci[number]
    else:
        number =- (number - 1)
        list_number_fibonacci = [1, 0]
        for numb in range(2, number + 1):
            list_number_fibonacci.append(list_number_fibonacci[numb - 2] - list_number_fibonacci[numb - 1]) 
        list_number_fibonacci.reverse()
    return list_number_fibonacci[0]

number_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))

list_fibonacci = []
for number_fib in range(-number_pos, number_pos + 1):
    list_fibonacci.append(number_fibonacci(number_fib))

print(list_fibonacci)