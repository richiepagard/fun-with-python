"""
The calculator program with `add, subtract, multiply, and divide` methods.
Logs the whole program in `file` and `stream` handlers.

Classse:
    Calculator: Give two numbers and has four main actions on the numbers.

Functions:
    main: Give inputs from the user and handle the exceptions.
"""

import logging
import os

# Ensure logs directory exists
os.makedirs("../logs", exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Set and config file handler
file_handler = logging.FileHandler("../logs/calculation_logs.log")
file_handler.setLevel(logging.WARNING)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

# Set and config stream handler
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
stream_handler.setFormatter(stream_formatter)

# Add handlers to the logger
if not logger.hasHandlers():
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)


class Calculator:
    """
    Methods:
        add (self): Return the additional result of two given numbers.
        subtract (self): Return the subtraction result of two given numbers.
        multiply (self): Return the multiplication result of two given numbers.
        divide (self): Return the division result of two given numbers.
    """

    def __init__(self, first_number: float, second_number: float):
        """
        Initialize method for the class.

        Check if the first and second numbers are not integer or float,
        raise TypeError exception.
        """

        if not isinstance(first_number, (int, float)) or\
            not isinstance(second_number, (int, float)):
            raise TypeError("Inputs must be numbers.")

        self.first_number = first_number
        self.second_number = second_number

    def add(self) -> float:
        """ Additional result of two provided numbers. """
        return self.first_number + self.second_number

    def subtract(self) -> float:
        """ Subtraction result of two given numbers. """
        return self.first_number - self.second_number

    def multiply(self) -> float:
        """
        Multiply result of two given numbers.
        """
        return self.first_number * self.second_number

    def divide(self) -> float:
        """ Division result of two provided numbers. """
        try:
            return self.first_number / self.second_number

        except ZeroDivisionError:
            logger.exception("Zero division exception occured.")
            logger.warning("-" * 40)
            # Re-raise the occured excepiton
            raise


def main():
    """
    The main method for run the program and methods.
    Gives user inputs and logs them, also handle the possible exceptions.
    """
    logger.debug("Program started.")

    first_number = second_number = None

    try:
        first_number = int(input("Enter the first number for your calculation please: "))
        second_number = int(input("Enter the second number for your calculation please: "))

        logger.info(
            "Received user inputs: First number: %s and Second number: %s.", \
                    first_number, second_number
        )
        logger.info("-" * 40)

    except EOFError:
        logger.exception("End of file error. No input received.")
        logger.warning("-" * 40)
        # Re-raise the occured exception
        raise

    except ValueError:
        logger.exception("Value error occured, use did not enter number.")
        logger.warning("-" * 40)
        # Re-raise the occured exception
        raise

    except Exception as occured_exception:
        logger.exception("An unexpected exception occured: %s", occured_exception)
        logger.warning("-" * 40)
        # Re-raise the occured exception
        raise

    # Check inputs if each of them is NULL, then set it as `0`
    first_number = first_number or 0
    second_number = second_number or 0

    # Logs the `Calculator` class methods
    calculate = Calculator(first_number, second_number)
    add = calculate.add()
    subtract = calculate.subtract()
    multiply = calculate.multiply()
    divide = calculate.divide()

    logger.info("Result of \"Add\" method: %s", add)
    logger.info("Result of \"Subtract\" method: %s", subtract)
    logger.info("Result of \"Multiply\" method: %s", multiply)
    logger.info("Result of \"Divide\" method: %s", divide)
    logger.info("-" * 40)


if __name__ == '__main__':
    main()
