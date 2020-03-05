import random


number = str(random.randint(1000, 9999))

print(number, ' - загаданное число')

def check_number(u_number):

    cows = []
    bulls = []

    for i, j in zip(number, u_number):
        if i == j:
            print(i)
            bulls.append(1)
        else:
            print(i)
            cows.append(1)


    print("Коровы:{} Быки: {}".format(sum(cows), sum(bulls)))


