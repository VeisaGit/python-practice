"""
You have a positive integer. Try to find out how many digits it has?

Input: A positive Int

Output: An Int.

Example:

number_length(10) == 2
number_length(0) == 1
"""


# First example:
def number_length(number):
    list = []
    for i in str(number):
        list.append(i)
    print(len(list))

number_length(10)

# Second example:
def number_length_2(number):
    print(len(str(number)))

number_length_2(12345)

