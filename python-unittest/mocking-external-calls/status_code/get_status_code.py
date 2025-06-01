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
        logger.info("Sent a request to the \"%s\" URL with \"%i\" seconds timeout.", url, timeout)
        page_status_code = page.status_code
        logger.info("The status code of \"%s\" URL is \"%i\"", url, page_status_code)

    except MissingSchema:
        logger.exception("Missing schema. Include \"http\" or \"https\".")
        logger.warning("-" * 40)
        # Re-raise the occured exception
        raise

    except InvalidURL:
        logger.exception("The URL is not properly formatted.")
        logger.warning("-" * 40)
        # Re-raise the occured exception
        raise

    except Timeout:
        logger.exception("Timeout error exception occured.")
        logger.warning("-" * 40)
        # Re-raise the occured exception
        raise

    except ConnectionError:
        logger.exception("Failed to connect to the server.")
        logger.warning("-" * 40)
        # Re-raise the occured exception
        raise

    except HTTPError as http_error:
        logger.exception("HTTP error occurred: %s", http_error.response.status_code)
        logger.warning("-" * 40)
        # Re-raise the occured exception
        raise

    except RequestException:
        logger.exception("Request Error. The page you requested does not exists.")
        logger.warning("-" * 40)
        # Re-raise the occured exception
        raise

    return page_status_code


def main():
    """
    The main method for run the program and methods.
    Gets user inputs and logs them, also handle the possible exceptions.
    """

    print(check_url_status_code('https://api.github.com', 5))


if __name__ == '__main__':
    main()
