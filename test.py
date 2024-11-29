# A Python program that calculates the sum of all even numbers in a list

def is_even(number):
    """Returns True if the number is even, otherwise False"""
    return number % 2 == 0

def sum_of_evens(numbers):
    """Returns the sum of all even numbers in the list"""
    total = 0
    for num in numbers:
        if is_even(num):
            total += num
    return total

