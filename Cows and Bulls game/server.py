import random
import re

number = str(random.randint(1000, 9999))

# print('загаданное число ', number)

try_counter = 0


def inst_number():
    global user_number, try_counter

    try_counter += 1

    user_number = input("Введите четырехзначное число: ")

    if re.search(r'\D', user_number):
        print("Ошибка! Нужно ввести цифры. Начните заново.")
    elif len(user_number) > 4:
        print("Ошибка! Вы ввели слишком много цифр, нужно ввести 4. Начните заново.")
    elif len(user_number) < 4:
        print("Ошибка! Вы ввели слишком мало цифр, нужно ввести 4. Начните заново.")
    else:
        return list(user_number)


def check_number():
    if inst_number():

        cows = []
        bulls = []

        for i, j in zip(number, user_number):
            if i == j:
                bulls.append(1)
            else:
                if j in number:
                    cows.append(1)

        while sum(bulls) < 4:
            print("Коровы:{} Быки: {}".format(sum(cows), sum(bulls)))
            check_number()
            break
        else:
            print("Вы отгадали число! Коровы:{} Быки: {}".format(sum(cows), sum(bulls)))
            print("Количество затраченных попыток - ", try_counter)
