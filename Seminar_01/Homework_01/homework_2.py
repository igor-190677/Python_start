# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def inputNumbers():
    array_user_numbers = []
    for item in 'X', 'Y', 'Z':
        array_user_numbers.append(input(f'Введите значение {item}: '))
    return array_user_numbers


def check_predicate(user_array):
    left = not (user_array[0] or user_array[1] or user_array[2])
    right = not user_array[0] and not user_array[1] and not user_array[2]
    return left == right


user_array_number = inputNumbers()
print(check_predicate(user_array_number))