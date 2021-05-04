"""
Домашнее задание №1
Функции и структуры данных
"""


# def power_numbers():
#     """
#     функция, которая принимает N целых чисел,
#     и возвращает список квадратов этих чисел
#     """


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    """
    return [number * number for number in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


# def filter_numbers():
#     """
#     функция, которая на вход принимает список из целых чисел,
#     и возвращает только чётные/нечётные/простые числа
#     (выбор производится передачей дополнительного аргумента)
#     """


def is_prime(n) -> bool:
    # Corner cases
    if n <= 1:
        return False
    if n <= 3:
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6

    return True


FILTERS_MAP = {
    ODD: lambda n: n % 2 != 0,
    EVEN: lambda n: n % 2 == 0,
    PRIME: is_prime,
}


def filter_numbers(numbers, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    """
    return list(filter(FILTERS_MAP[filter_type], numbers))
