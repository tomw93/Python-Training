"""
https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

- Ask the user for a number.
- Depending on whether the number is even or odd, print out an
    appropriate message to the user.

Hint: how does an even / odd number react differently when divided by 2?

Extras:

- If the number is a multiple of 4, print out a different message.
- Ask the user for two numbers: one number to check (call it num) and one
    number to divide by (check). If check divides evenly into num, tell
    that to the user. If not, print a different appropriate message.

"""


def get_user_input():
    """
    Asks the user for a number.

    Returns:
        The number entered by the user as an int.

    Raises:
        ValueError: If the user does not enter a valid number
    """

    try:
        user_number = int(input("Enter a number: ")) 

    except ValueError:
        print('A number must be entered.')

    return user_number


def print_odd_even(user_number):
    """
    Determines if the number is odd or even, and prints
    the result.

    Args:
        user_number: The number to find out if it's odd or even.
    """

    remainder = user_number % 2

    if remainder == 0:
        print('The number you entered is Even')
    else:
        print('The number you entered is Odd')


def print_multiple_of_four(user_number):
    """
    Prints out a message if the number is a multiple of four.

    Args:
        user_number: The number inputted by the user.
    """

    remainder = user_number % 4

    if remainder == 0:
        print('The number is a multiple of 4')


def get_user_input_2():
    """
    Asks the user to enter a number and a divider.

    Returns:
        The number entered by the user as an int, and the
        divider as an int.

    Raises:
        ValueError: If the user does not enter a valid number
    """

    try:
        user_number = int(input("Enter a number to check: "))
        divider = int(input("Enter a number to divide by: "))

    except ValueError:
        print('Invalid number entered.')

    return user_number, divider


def does_number_divide_evenly(number, divider):
    """
    Prints out if the provided number can be divided evenly
    by the divider.

    Args:
        number: The number to divide.
        divider: The number to divide by.
    """
    remainder = number % divider

    if remainder == 0:
        print(f"{number} can be evenly divided by {divider}")
    else:
        print(f"{number} cannot be evenly divided by {divider}")


# Test odd or even
number = get_user_input()
print_odd_even(number)

# Test multiple of 4
print_multiple_of_four(number)

# Test user number / divide
number2, divider = get_user_input_2()
does_number_divide_evenly(number2, divider)
