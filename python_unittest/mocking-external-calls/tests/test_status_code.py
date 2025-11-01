"""
Test cases for the `check url status code` program.

Classes:
    TestURLStatus: Test various responses and status codes with `mock`.
"""

import unittest
from unittest.mock import patch, Mock

from requests.exceptions import(
    Timeout, ConnectionError, HTTPError,
    RequestException, MissingSchema, InvalidURL
)

from status_code.get_status_code import check_url_status_code


REQUESTS_GET = "requests.get"


class TestURLStatus(unittest.TestCase):
    """
    Test class for test different status codes from `check_url_status_code` method.

    Methods:
        test_url_status_200(self, mock_get): Simulate a valid request
        and expects an HTTP 200 status code.
        test_url_status_404(self, mock_get): Simulate a request
        to an invalid URL and expects an HTTP 404 status code.

        test_missing_schema_exception(self, mock_get): Somulates a MissingSchema exception when the URL is missing a scheme(e.g., 'http').
        test_invalid_url_exception(self, mock_get): Simulates an InvalidURL exception when the URL is improperly formatted.
        test_timeout_exception(self, mock_get): Simulates a Timeout exception when the request exceeds the specified timeout.
        test_connection_error_exception(self, mock_get): Simulates a ConnectionError when the connection to the server fails.
        test_http_error(self, mock_get): Simulates an HTTPError raised from the response's `raise_for_status()` method.
        test_request_exception(self, mock_get): Simulates a generic RequestException for unexpected request error.
    """

    def setUp(self):
        self.TIMEOUT = 10

        self.HTTP_OK = 200
        self.HTTP_NOT_FOUND = 404

    @patch(REQUESTS_GET)
    def test_url_status_200(self, mock_get):
        """
        Simulate a successful (HTTP 200) response from GitHub's API using mocked requests, with a 10-second timeout.
        """
        mock_response = Mock()
        # Creates a mock response
        mock_response.status_code = self.HTTP_OK
        # Assign the mock response to be returned by the mock object
        mock_get.return_value = mock_response

        # Call the `check url status code` function and assert the result
        status = check_url_status_code(url="https://api.github.com", timeout=self.TIMEOUT)
        self.assertEqual(status, self.HTTP_OK)

        mock_get.assert_called_once_with(url="https://api.github.com", timeout=self.TIMEOUT)

    @patch(REQUESTS_GET)
    def test_url_status_404(self, mock_get):
        """
        Simulate a not found (HTTP 404) response from an imaginary URL using mocked requests, with a 10-second timeout.
        """
        mock_response = Mock()
        # Creates a mock response
        mock_response.status_code = self.HTTP_NOT_FOUND
        # Assign the mock response to be returned by the mock object
        mock_get.return_value = mock_response

        # Call the `check url status code` function and assert the result.
        status = check_url_status_code(url="https://r1ch173s771ss747usc0d3.com", timeout=self.TIMEOUT)
        self.assertEqual(status, self.HTTP_NOT_FOUND)

        mock_get.assert_called_once_with(url="https://r1ch173s771ss747usc0d3.com", timeout=self.TIMEOUT)

    @patch(REQUESTS_GET)
    def test_missing_schema_exception(self, mock_get):
        """
        Simulate a MissingSchema exception.
        It raises when the URL does not have `http` or `http`.
        """
        mock_get.side_effect = MissingSchema

        with self.assertRaises(MissingSchema):
            check_url_status_code(url="www.github.com", timeout=self.TIMEOUT)

    @patch(REQUESTS_GET)
    def test_invalid_url_exception(self, mock_get):
        """
        Simulate an InvalidURL exception.
        It is raised when the URL does not formatted properly.
        """
        mock_get.side_effect = InvalidURL

        with self.assertRaises(InvalidURL):
            check_url_status_code(url="github.com", timeout=self.TIMEOUT)

    @patch(REQUESTS_GET)
    def test_timeout_exception(self, mock_get):
        """
        Simulate a Timeout error exception.
        It is raised when get response from the URL,
        takes longer than the `check_url_status_code` expects.
        """
        mock_get.side_effect = Timeout

        with self.assertRaises(Timeout):
            check_url_status_code(url="https://medium.com", timeout=0.1)

    @patch(REQUESTS_GET)
    def test_connection_error_exception(self, mock_get):
        """
        Simulate a ConnectionError exception.
        It is raised when connection to the server failed.
        """
        mock_get.side_effect = ConnectionError

        with self.assertRaises(ConnectionError):
            check_url_status_code(url="https://richie.com", timeout=self.TIMEOUT)

    @patch(REQUESTS_GET)
    def test_http_error(self, mock_get):
        """
        Simulate a HTTPError exception.
        Not raises automatically unless call `raise_for_status()`
        in `requests.get` response.
        """
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = HTTPError("404 Client Error.")
        mock_get.return_value = mock_response

        with self.assertRaises(HTTPError):
            check_url_status_code(url="https://github.com/somethingforthisexception", timeout=self.TIMEOUT)

    @patch(REQUESTS_GET)
    def test_request_exception(self, mock_get):
        """
        Simulate a RequestException.
        It is raised when the page use gets to requested does not exists.
        """
        mock_get.side_effect = RequestException

        with self.assertRaises(RequestException):
            check_url_status_code(url="https://h3ll0w0rld.com", timeout=self.TIMEOUT)


if __name__ == '__main__':
    unittest.main()
