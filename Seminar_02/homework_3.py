# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# Пример:

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

def input_number():
    flag = False
    while flag == False:
        try:
            number = int(input('Введите число последовательностей: '))
            flag = True
            if number <= 0:
                print('Значение числа не должно быть равно 0 или меньше 0!')
                flag = False
        except ValueError:
            print("Это не число!")
    return number

def add_sequences(sequences):
    tuple_sequenses = {}
    for number in range(1, sequences + 1):
        tuple_sequenses[number] = round(sum_sequences(number))
    return tuple_sequenses

def sum_sequences(number_seq):
    sequence = 0
    for number in range(1, number_seq + 1):
        sequence += (1 + 1 / number) ** number
    return sequence

number_sequences = input_number()
print(add_sequences(number_sequences))
