import random
from client import game


def make_number():
    global number
    number = list(str(random.randint(1000, 9999)))
    print(number)



def check_number():
    game()
    if

