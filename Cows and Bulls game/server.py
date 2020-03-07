import random

number = str(random.randint(1000, 9999))

print('загаданное число ', number)

def inst_number():
    global user_number
    user_number = list(input("Введите четырехзначное число: "))
    return user_number



def check_number():

    inst_number()

    cows = []
    bulls = []

    for i, j in zip(number, user_number):
        if i == j:
            bulls.append(1)
        else:
            if j in number:
                cows.append(1)

    while True:

        if sum(bulls) != 4:
            print("Коровы:{} Быки: {}".format(sum(cows), sum(bulls)))
            check_number()
            break

        else:
            print("Коровы:{} Быки: {}".format(sum(cows), sum(bulls)))
            break


