"""
This program simply gets a URL from the user input,
and checks its status code. For instance, status code: 200

Methods:
    check_url_status_code (output: int): Gets a URL from its arguments,
    send request to it and then return the status code.
"""

import logging
import os

import requests
from requests.exceptions import(
    Timeout, ConnectionError, HTTPError,
    RequestException, MissingSchema, InvalidURL
)


# Ensure logs directory exists
os.makedirs("../logs", exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Set and config file handler
file_handler = logging.FileHandler("../logs/request_logs.log")
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


def check_url_status_code(url: str, timeout: int) -> int:
    """
    Takes a URL and returns its status code.

    Arguments:
        url (str): The URL to send a request to.
    
    Returns:
        status code (int): The status code of the given url.
    """
    try:
        page = requests.get(url=url, timeout=timeout)
        page_status_code = page.status_code
        page.raise_for_status()

        logger.info("Sent a request to the \"%s\" URL with \"%i\" seconds timeout.", url, timeout)
        logger.info("The status code of \"%s\" URL is \"%i\"", url, page_status_code)

    except MissingSchema:
        logger.exception("Missing schema. Include \"http\" or \"https\".")
        logger.warning("-" * 40)
        # Re-raise the occurred exception
        raise

    except InvalidURL:
        logger.exception("The URL is not properly formatted.")
        logger.warning("-" * 40)
        # Re-raise the occurred exception
        raise

    except Timeout:
        logger.exception("Timeout error exception occured.")
        logger.warning("-" * 40)
        # Re-raise the occurred exception
        raise

    except ConnectionError:
        logger.exception("Failed to connect to the server.")
        logger.warning("-" * 40)
        # Re-raise the occurred exception
        raise

    except HTTPError as http_error:
        logger.exception("HTTP error occurred: %s", http_error)
        logger.warning("-" * 40)
        # Re-raise the occurred exception
        raise

    except RequestException:
        logger.exception("Request Error. The page you requested does not exists.")
        logger.warning("-" * 40)
        # Re-raise the occurred exception
        raise

    return page_status_code


def main():
    """
    The main method for run the program and methods.
    Gets user inputs and logs them, also handle the possible exceptions.
    """
    logger.debug("Program started.")

    url_input = "Nothing"
    timeout_input = None

    try:
        url_input = input("Enter a URL to send a request to: ")
        timeout_input = int(input("Enter the timeout for waiting to the response: "))

        logger.info("Received user information.")
        logger.debug("-" * 40)

    except EOFError:
        logger.exception("End of file error. No input received.")
        logger.warning("-" * 40)
        # Re-raise the cought exception
        raise

    except Exception as exception:
        logger.exception("An unexpected error occured. %s", exception)
        logger.warning("-" * 40)
        # Re-raise the cought exception
        raise

    url_input = url_input or "Nothing"
    timeout_input = timeout_input or 5

    # Logs the `check_url_status_code` function
    logger.info(check_url_status_code(url_input, timeout_input))
    logger.debug("-" * 40)


if __name__ == '__main__':
    main()
