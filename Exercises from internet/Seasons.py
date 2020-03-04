'''
Написать функцию, принимающую 1 аргумент — номер месяца (от 1 до 12),
и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).
'''
import re


def season(month_number):
    months = ([1, 2, 12], [3, 4, 5], [6, 7, 8], [9, 10, 11])

    if month_number in months[0]:
        print('зима')
    elif month_number in months[1]:
        print('весна')
    elif month_number in months[2]:
        print('лето')
    else:
        print('осень')


while True:
    month_number = input("Введите номер месяца: ")
    if not month_number:
        print("Вы ничего не ввели.")
    elif re.search('\D', month_number):
        print("Нужно ввести цифры.")
    else:
        month_number = int(month_number)
        if month_number > 12 or month_number == 0:
            print("Месяца с таким номером нет. Введите номер от 1 до 12.")
        else:
            season(month_number)
            break
