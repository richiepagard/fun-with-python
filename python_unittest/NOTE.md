# Notes For Python Test (Unittest / Pytest)
I write some important and cool concepts or things I could understand from `unittest` or `pytest` modules, or maybe the whole `testing` concept. This is my notebook of what I found cool or important.

---

## Mock
**According to the Python docs:**
> It allows you to replace parts of your system under test with mock objects and make assertions about how they have been used.

From what I understood yet, **Mocking** is useful when we want to simulate behavior instead of using real external systems, functions, or objects. For instance, if I want to test a function like `is_weekend()` that relies on `detetime.today()`, I can't easily test different days of the week using the real `datetime`.
So instead, I can **mock** `detetime` to simulate different dates.

Example logic:
```python
datetime = Mock()
```

### A More Real Example Of `Mock`:
Test a program which returns the status code of the given URL.

```python
import unittest
from unittest.mock import patch, Mock

from status_code.check_status_code import check_url_status_code


class TestURLStatus(unittest.TestCase):
    """
    Test class for test different status codes from `check_url_status_code` method.

    Methods:
        test_url_status_200 (self, mock_get): Send a request (as a mock) to a valid URL,
        and expect to see a 200 status code as the result.
    """

    @patch("requests.get")
    def test_url_status_200(self, mock_get):
        mock_response = Mock()
        # Creates a mock response
        mock_response.status_code = 200
        # Assign the mock response to be returned by the mock object
        mock_get.return_value = mock_response

        # Call the `check url status code` function and assert the result
        status = check_url_status_code(url="https://api.github.com", timeout=10)
        self.assertEqual(status, 200)

        mock_get.assert_called_once_with(url="https://api.github.com", timeout=10)
```

OK, I want to explain step by step to make sure I could understand :/

- **`mock_get`:**  A mock version of `requests.get`, provided by `@patch`.
- **`mock_response.status_code = 200`:** Create a fake response object with status 200.
- **`mock_get.return_value = mock_response`:** Make `mock_get()` return our fake response.
- **`status = check_url_status_code(...)`:** Calls the real function, which now uses the mock.
- **`mock_get.assert_called_once_with(...)`:** Asserts that `requests.get()` was called exactly once with the expected arguments.

### Side Effect
Using `side_effect` in Mocking when we want to affect when the function or operation start. Like raising an exception when a mock called.

According t what Python docs said:
> This can either be a function to be called when the mock is called, an iterable or an exception (class or instance) to be raised.

It's easy to understand, just need to use it!

---
