"""
Дан массив целых чисел. Нужно найти сумму элементов с четными индексами (0-й, 2-й, 4-й итд), затем перемножить эту сумму и последний элемент исходного массива. Не забудьте, что первый элемент массива имеет индекс 0.

Для пустого массива результат всегда 0 (ноль).

Входные данные: Список (list) целых чисел (int).

Выходные данные: Число как целочисленное (int).

Примеры:

checkio([0, 1, 2, 3, 4, 5]) == 30
checkio([1, 3, 5]) == 30
checkio([6]) == 36
checkio([]) == 0

"""


def checkio(array: list) -> int:

    # list = []
    #
    # if array:
    #     for position, value in enumerate(array):
    #         if position % 2 == 0:
    #             list.append(value)
    #     return sum(list) * array[-1]
    # return 0
    if not array:   return 0
    return sum(array[::2]) * array[-1]


print(checkio([1,3,5]))



