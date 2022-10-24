# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

def calculation_pi(prec):
    square = 0
    d = 1
    sgn = 1
    while True:
        degree = 4 / d
        square = square + sgn * degree
        if degree < prec:
            return square
        sgn =- sgn
        d = d + 2
 
precision = 0.001
print(calculation_pi(precision))