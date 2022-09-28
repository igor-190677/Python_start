# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def inputNumbers(x):
    array_xyz = ["X", "Y", "Z"]
    array_user_numbers = []
    for i in range(x):
        array_user_numbers.append(input(f"Введите значение {array_xyz[i]}: "))
    return array_user_numbers


def check_predicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result


user_array_number = inputNumbers(3)

if check_predicate(user_array_number) == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")