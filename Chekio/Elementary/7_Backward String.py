"""
You should return a given string in reverse order.

Input: A string.

Output: A string.

Example:

backward_string('val') == 'lav'
backward_string('') == ''
backward_string('ohho') == 'ohho'
backward_string('123456789') == '987654321'
"""

#First example
def backward_string(val: str) -> str:
    # your code here
    return val[::-1]

#Second example (It's example with return template like at site)
def backward_string2(val: str) -> str:
    # your code here
    if val =='' or val:
        return val[::-1]
    return None


if __name__ == '__main__':
    print("Example:")
    print(backward_string2(''))

    # # These "asserts" are used for self-checking and not for an auto-testing
    # assert backward_string('val') == 'lav'
    # assert backward_string('') == ''
    # assert backward_string('ohho') == 'ohho'
    # assert backward_string('123456789') == '987654321'
    # print("Coding complete? Click 'Check' to earn cool rewards!")
