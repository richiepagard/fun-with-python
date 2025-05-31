"""
This program simply gets a URL from the user input,
and checks its status code. For instance, status code: 200

Methods:
    check_url_status_code (output: int): Gets a URL from its arguments,
    send request to it and then return the status code.
"""

import requests


def check_url_status_code(url: str) -> int:
    """
    Takes a URL and returns its status code.

    Arguments:
        url (str): The URL to send a request to.
    
    Returns:
        status code (int): The status code of the given url.
    """
    page = requests.get(url, timeout=10)
    page_status_code = page.status_code

    return page_status_code
