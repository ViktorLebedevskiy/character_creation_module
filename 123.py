from math import sqrt


message = 'Добро пожаловать в самую лучшую программу для вычисления ' \
          'квадратного корня из заданного числа.'


def calculateSquareRoot(Number):
    """ Вычисляет квадратный корень."""
    return sqrt(Number)


def calc(your_number):
    result = calculateSquareRoot(your_number)
    if your_number <= 0:
        return

    print(f"Мы вычислили квадратный корень из "
          f"введённого вами числа. Это будет: {result}")


print(message)
calc(25.5)
