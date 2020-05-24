"""
Дана строка и нужно найти ее первое слово.

Строка состоит только из английских символов и пробелов.
В начале и в конце строки пробелов нет.
Входные параметры: Строка.

Выходные параметры: Строка.
"""


def first_word(text):
    """
        returns the first word in a given text.
    """
    # your code here
    space = ' '
    if space in text:
        find_space = text.find(space)
        first_word = text[0:find_space]
    else:
        symbols_counter = len(text)
        first_word = text[0:symbols_counter]
    return first_word


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"
    print("Coding complete? Click 'Check' to earn cool rewards!")
