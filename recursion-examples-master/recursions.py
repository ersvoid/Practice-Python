

# Factorial

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


def exponent(a, b):
    if b == 0:
        return 1
    else:
        return a * exponent(a, b - 1)


def mult_int(a, b):
    if b == 1:
        return a
    else:
        return a + mult_int(a, b -1)


def divide(a, b):
    if a == 0:
        return 0
    elif a - b < 0:
        return a / b
    else:
        return 1 + divide(a - b, b)


def add(a, b):
    if b == 0:
        return a
    else:
        return 1 + add(a, b - 1)