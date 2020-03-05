import random


number = str(random.randint(1000, 9999))
print(number, ' - загаданное число')

def check_number(u_number):

    r = dict(zip(number, u_number))
    print(r)

    cows = []
    bulls = []

    for i in r:
        if i == r[i]:
            print(i)
            bulls.append(1)
        else:
            print(i)
            cows.append(1)

    print("Коровы:{} Быки: {}".format(sum(cows), sum(bulls)))


    # print(u_number, ' - введенное число')

