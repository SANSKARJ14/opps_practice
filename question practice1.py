# Question:
"""
Create a Python class called `Product` that represents a product in an e-commerce store.
The class should have the following attributes:
- `name` (string): The name of the product.
- `price` (float): The price of the product.

The class should also have a method called `calculate_discounted_price` that takes a discount percentage
as input and calculates the discounted price of the product. The discounted price is calculated by subtracting
the discount amount from the original price.

Your task is to complete the implementation of the `Product` class and handle possible exceptions.

Additionally, you need to add logging statements to record the discount calculation.
 Each time the `calculate_discounted_price` method is called, the log should include the original price,
  the discount percentage, the discount amount, and the discounted price.

Complete the missing parts of the code below to achieve the requirements.

Note:
- The logging statements should use the `logging` module from the Python standard library and have a logging level of INFO.

You can use the `logging.info()` function to log the messages.

Example usage:
product = Product("Laptop", 1000)
product.calculate_discounted_price(10)
# Output: Discounted price of Laptop: $900.0 (Original price: $1000, Discount: 10%)
"""


import logging

class product:
    def __init__(self, name  , price):
        self.name = name
        self.price = price
        logging.basicConfig(level= logging.INFO)

    def discount_calculation(self,discountpercentage):
        try:
            discount = (self.price * discountpercentage)/100
            actual_price = self.price - discount
            logging.info(f"discounted price of {self.name} is {actual_price}")
            return actual_price
        except exception as e:
            logging.error(f"error is {e}")

product = product("ship",23423434)
product.discount_calculation(195)



