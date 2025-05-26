import os
import logging

from utils import devide


def make_directory(directory_name: str) -> None:
    """
    Check if a directory with given name does not exists in the current path,
    then create a new directory with given name.

    Arguments:
        directory_name (str): The name of directory will created.
    """

    is_directory_exists = os.path.isdir(directory_name)

    if not is_directory_exists:
        os.makedirs(directory_name)

make_directory('logs')

logger = logging.getLogger(__name__)
# Set custom level for logger
logger.setLevel(logging.DEBUG)

# Declare handlers
file_handler = logging.FileHandler("logs/division_logs.log")
stream_handler = logging.StreamHandler()

# Determine and set specific formatter for file handler
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
# Determine and set specific formatter for stream handler
stream_formatter = logging.Formatter("%(levelname)s - %(name)s - %(message)s")
stream_handler.setFormatter(stream_formatter)

# Set specific level for each handler
file_handler.setLevel(logging.WARNING)
stream_handler.setLevel(logging.DEBUG)

# Check if the logger does not have any handlers, then add the handlers to the logger
if not logger.hasHandlers():
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)


def main():
    logger.debug("Program started.")

    numerator = denominator = None

    try:
        numerator = int(input("Enter the numerator please: "))
        denominator = int(input("Enter denomerator please: "))

        logger.info("Received user inputs. Numerator: {} and Denominator: {}".format(numerator, denominator))
        logger.info("-" * 40)
    
    except EOFError as e:
        logger.exception("End of file error. No input received.")
        logger.warning("-" * 40)
        # Re-raise the cought exception
        raise

    except Exception as e:
        logger.exception("An unexpected error occured: {}".format(e))
        logger.warning("-" * 40)
        # Re-raise the cought exception
        raise

    except ValueError as e:
        logger.exception("Value error occured, user did not enter numebr.")
        logger.warning("-" * 40)
        # Re-raise the cought exception
        raise

    # Check inputs if each of them is NULL, then set it as `1`
    numerator = numerator or 0
    denominator = denominator or 0

    # Logs the `divide` function
    result = devide(numerator, denominator)
    logger.info("Division result: {}".format(result))
    logger.info("-" * 40)


if __name__ == '__main__':
    main()
