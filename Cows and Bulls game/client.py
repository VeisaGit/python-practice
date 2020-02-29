from server import make_number, check_number

def game():
    client_number = list(input("Введите четырехзначное число: "))
    check_number()

game()

# print(make_number())