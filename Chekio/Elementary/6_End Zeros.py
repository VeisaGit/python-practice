"""
Try to find out how many zeros a given number has at the end.

Input: A positive Int

Output: An Int.

Example:

end_zeros(0) == 1
end_zeros(1) == 0
end_zeros(10) == 1
end_zeros(101) == 0
"""
import re

#First example
def end_zeros(num: int) -> int:
    # your code here

    sep_list = []

    amount_of_zeros = []

    for i in str(num):
        sep_list.append(i)
    for i in sep_list[::-1]:
        if i == '0':
            amount_of_zeros.append(int(i))
        else:
            break
    return len(amount_of_zeros)



if __name__ == '__main__':
    print("Example:")
    print(end_zeros(101000))

    # # These "asserts" are used for self-checking and not for an auto-testing
    # assert end_zeros(0) == 1
    # assert end_zeros(1) == 0
    # assert end_zeros(10) == 1
    # assert end_zeros(101) == 0
    # assert end_zeros(245) == 0
    # assert end_zeros(100100) == 2
    # print("Coding complete? Click 'Check' to earn cool rewards!")
