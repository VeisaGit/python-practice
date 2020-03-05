"""
# Правила:
# Компьютер загадывает четырехзначное число, все цифры которого различны
# (первая цифра числа отлична от нуля). Игроку необходимо разгадать задуманное число.
# Игрок вводит четырехзначное число c неповторяющимися цифрами,
# компьютер сообщают о количестве «быков» и «коров» в названном числе:
# «бык» — цифра есть в записи задуманного числа и стоит в той же позиции, что и в задуманном числе
# «корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции, что и в задуманном числе
#
# Например, если задумано число 3275 и названо число 1234,
# получаем в названном числе одного «быка» и одну «корову».
# Очевидно, что число отгадано в том случае, если имеем 4 «быка».
#
# Формат ответа компьютера
# > быки - 1, коровы - 1
"""

import server

while True:
    server.check_number(u_number = list(input("Введите четырехзначное число: ")))
