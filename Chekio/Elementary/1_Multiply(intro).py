"""Это вводная миссия, целью которой является показать как решать задачи на CheckiO или как получить максимум от этого. Когда эта миссия будет решена еще одна станция будет доступна, с чуть более сложными миссиями.

Итак, это самая простая миссия. Напишите функцию, которая будет получать 2 числа и возвращать результат произведения этих чисел.

Входные данные: Два аргумента. Оба int

Выходные данные: Int.
"""


def mult_two(a, b):
    c = a * b
    return c


if __name__ == '__main__':
    print("Example:")
    print(mult_two(3, 2))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert mult_two(3, 2) == 6
    assert mult_two(1, 0) == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")