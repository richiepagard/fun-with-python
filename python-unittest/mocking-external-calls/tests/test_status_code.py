"""
Test cases for the `check url status code` program.

Classes:
    TestURLStatus: Test various responses and status codes with `mock`.
"""

import unittest
from unittest.mock import patch, Mock

from status_code.get_status_code import check_url_status_code


class TestURLStatus(unittest.TestCase):
    """
    Test class for test different status codes from `check_url_status_code` method.

    Methods:
        test_url_status_200 (self, mock_get): Send a request (as a mock) to a valid URL,
        and expect to see a 200 status code as the result.
    """
    def setUp(self):
        self.TIMEOUT = 10

        self.HTTP_OK = 200
        self.HTTP_NOT_FOUND = 404

    @patch("requests.get")
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

    @patch("requests.get")
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


if __name__ == '__main__':
    unittest.main()
