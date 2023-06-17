# Question:
"""
You are building a simple calculator program using object-oriented programming in Python. Implement a class called `Calculator` with the following functionalities:

1. Addition: The `add` method should take two numbers as parameters and return their sum.
2. Subtraction: The `subtract` method should take two numbers as parameters and return their difference.
3. Multiplication: The `multiply` method should take two numbers as parameters and return their product.
4. Division: The `divide` method should take two numbers as parameters and return their quotient. If the second number is zero, raise a custom exception called `ZeroDivisionError` with an appropriate error message.

Example usage:
calc = Calculator()

# Addition
result = calc.add(5, 3)
print(result)
# Output: 8

# Subtraction
result = calc.subtract(10, 4)
print(result)
# Output: 6

# Multiplication
result = calc.multiply(2, 6)
print(result)
# Output: 12

# Division
result = calc.divide(10, 2)
print(result)
# Output: 5

result = calc.divide(7, 0)
# Output: ZeroDivisionError: Cannot divide by zero.
"""

class ZeroDivisionError(Exception):
    pass

class calculator:
    def addition(self,a,b):
        return a  + b

    def subtraction(self , a ,b):
        return a - b

    def multipication (self,a,b):
        return a * b

    def division (self,a,b):
        if b == o:
            raise ZeroDivisionError("b cannot divide by zero")
        return a / b

calc = calculator()


result = calc.addition(5, 3)
print(result)




