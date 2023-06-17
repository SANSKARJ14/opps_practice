# Question:
"""
You are working on a Python project that involves processing a list of integers.
 Write a Python function called `find_max_odd_number` that takes a list of integers as input
 and returns the maximum odd number from the list.

Your task is to complete the implementation of the `find_max_odd_number` function and handle possible exceptions.

The function should:
1. Accept a list of integers as input.
2. Find the maximum odd number from the list.
3. Return the maximum odd number as an integer.

If any exception occurs during the execution
 (e.g., the input is not a list, it contains non-integer elements,
or there are no odd numbers in the list), raise a custom exception called `InvalidInputError` with an appropriate error message.

Complete the missing parts of the code below to achieve the requirements.

Example usage:
numbers = [1, 3, 2, 4, 5]
max_odd = find_max_odd_number(numbers)
print(max_odd)
# Output: 5

numbers = [2, 4, 6, 8]
max_odd = find_max_odd_number(numbers)
# Output: InvalidInputError: No odd numbers found in the list.
"""
import logging

logging.basicConfig(level=logging.INFO)

class invalidinputerror(Exception):
    pass

def max_odd_number(numbers):
    try:
        if  not isinstance(numbers, list):
            raise invalidinputerror ("invalid input. input list")

        odd_number = [num for num in numbers if num % 2 != 0]

        if not odd_number:
            raise invalidinputerror("no odd number in list")

        max_odd = max (odd_number)

        logging.info(F"max odd number is {max_odd}")
        print (odd_number)

    except invalidinputerror as e:
        logging.error(f"invalid input error{e}")
        raise

    except exception as e :
        logging.error(f"an error occured{e}")
        raise

max_odd_number([2,33,44,56,54,75])