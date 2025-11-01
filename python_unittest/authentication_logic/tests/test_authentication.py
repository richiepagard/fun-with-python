"""
Unit tests for the authentication logic of the application.

This module tests core functionalities of the `UserAuthentication` class and related utilities:
- Password hashing using `hash_password()`
- User registration behavior (successful and duplicate cases)
- Login validation (handling invalid usernames, wrong passwords, and successful logins)

The tests make use of `unittest` and `unittest.mock` to isolate and verify each component
without requiring a real database connection. Instances of `UserAuthentication` are created
using `__new__` to bypass `__init__`, allowing flexible mocking of database attributes.
"""

import unittest
from unittest.mock import MagicMock, patch

from python_unittest.authentication_logic.authentication.authentication import UserAuthentication, hash_password


class TestHashPassword(unittest.TestCase):
    """Unit tests for the `hash_password` function."""

    def test_hash_password_creates_different_value(self):
        """
        Test that `hash_password` generates a non-identical and consistent hash value.

        This test ensures that:
        1. The hashed password is different from the original plaintext password.
        2. Hashing the same input multiple times returns the same hash value
           (ensuring deterministic behavior).

        Expected:
            - `hash_password(password)` != password
            - Multiple calls with the same input return equal outputs
        """
        password = 'mypassword'
        hashed_password = hash_password(password)
        self.assertNotEqual(password, hashed_password)
        self.assertEqual(hashed_password, hash_password(password))


class TestUserRegister(unittest.TestCase):
    """Unit tests for the user registration logic in `UserAuthentication`."""

    # @patch('builtins.input', return_value='testuser')
    # @patch('getpass.getpass', return_value='testpass')
    # @patch('sys.stdout', new_callable=io.StringIO)
    @patch(
        'python_unittest.authentication_logic.authentication.authentication.hash_password',
        return_value='hashed_pass'
    )
    def test_register(self, mock_hash):
        """
        Test registering a new user with valid credentials.

        Steps:
        1. Create a `UserAuthentication` instance without calling its `__init__` method
           using `__new__`. This allows mocking attributes before initialization.
        2. Mock `existance_username`, `cur`, and `con` methods/attributes.
        3. Call `register()` and verify:
            - The password was hashed correctly.
            - The correct SQL `INSERT` query was executed.
            - The database commit method was called once.

        Expected:
            - `hash_password` called once with the given password.
            - `cur.execute()` called with the correct SQL and parameters.
            - `con.commit()` called once.
        """
        ua = UserAuthentication.__new__(UserAuthentication)
        ua.existance_username = MagicMock(return_value=False)
        ua.cur = MagicMock()
        ua.con = MagicMock()

        ua.register('testuser', 'testpass')

        mock_hash.assert_called_once_with('testpass')
        ua.cur.execute.assert_called_once_with(
            'INSERT INTO accounts(username, password) VALUES(?, ?)',
            ('testuser', 'hashed_pass')
        )

        ua.con.commit.assert_called_once()
        # self.assertIn('Register successfully!', mock_stdout.getvalue())

    @patch(
        'python_unittest.authentication_logic.authentication.authentication.hash_password',
        return_value='hashed_pass'
    )
    def test_register_existing_username(self, mock_hash):
        """
        Test registering a user that already exists in the database.

        Steps:
        1. Create a `UserAuthentication` instance without `__init__` using `__new__`.
        2. Mock `existance_username` to always return `True` (simulate existing user).
        3. Attempt to register the same username again.
        4. Verify that a `ValueError` is raised with the correct message and that
           no database operations (`execute` or `commit`) are called.

        Expected:
            - Raises `ValueError("username already exists")`.
            - No calls to `execute` or `commit`.
        """
        user_auth = UserAuthentication.__new__(UserAuthentication)
        user_auth.existance_username = MagicMock(return_value=True)
        user_auth.cur = MagicMock()
        user_auth.con = MagicMock()

        with self.assertRaises(ValueError) as errormsg:
            user_auth.register('existinguser', 'testpass')

        self.assertEqual(str(errormsg.exception), 'username already exists')

        user_auth.cur.execute.assert_not_called()
        user_auth.con.commit.assert_not_called()


class TestUserLogin(unittest.TestCase):
    """Unit tests for the login and validation logic in `UserAuthentication`."""

    def test_validation_login_user_not_found(self):
        """
        Test that an exception is raised when trying to log in with a non-existent username.

        Steps:
        1. Create a `UserAuthentication` instance using `__new__`.
        2. Mock database cursor to simulate no user found.
        3. Call `validation_login()` with a fake username.

        Expected:
            - Raises `ValueError("username not found")`.
            - Executes the correct SQL query once.
        """
        user_auth = UserAuthentication.__new__(UserAuthentication)

        user_auth.cur = MagicMock()

        user_auth.cur.execute.return_value.fetchone.return_value = None

        with self.assertRaises(ValueError) as err:
            user_auth.validation_login('fakeuser', 'testpass')

        self.assertEqual(str(err.exception), 'username not found')

        user_auth.cur.execute.assert_called_once_with(
            "SELECT password FROM accounts WHERE username = ?",
            ('fakeuser',))

    def test_validation_login_incorrect_password(self):
        """
        Test that an exception is raised when the password does not match the stored hash.

        Steps:
        1. Create a `UserAuthentication` instance with a mocked database cursor.
        2. Simulate a stored hash value for a real user.
        3. Attempt login with an incorrect password.

        Expected:
            - Raises `ValueError("incorrect password")`.
            - Executes the correct SQL query once.
        """
        user_auth = UserAuthentication.__new__(UserAuthentication)
        user_auth.cur = MagicMock()

        user_auth.cur.execute.return_value.fetchone.return_value = ('hashed_pass',)

        with self.assertRaises(ValueError) as err:
            user_auth.validation_login('realuser', 'wrongpass')

        self.assertEqual(str(err.exception), 'incorrect password')

        user_auth.cur.execute.assert_called_once_with(
            "SELECT password FROM accounts WHERE username = ?",
            ('realuser',)
        )

    @patch(
        'python_unittest.authentication_logic.authentication.authentication.hash_password',
        return_value='hashed_pass'
    )
    def test_user_login_successfully(self, mock_hash):
        """
        Test successful login when username and password are valid.

        Steps:
        1. Patch `hash_password` to return a fixed value.
        2. Create a `UserAuthentication` instance using `__new__` and
           mock its `validation_login()` method to return True.
        3. Call `login()` with valid credentials.

        Expected:
            - `hash_password` is called once with the correct password.
            - `validation_login()` is called once with the correct parameters.
        """
        user_auth = UserAuthentication.__new__(UserAuthentication)
        user_auth.validation_login = MagicMock(return_value=True)
        user_auth.login('testuser', 'testpass')

        mock_hash.assert_called_once_with('testpass')
        user_auth.validation_login.assert_called_once_with('testuser', 'hashed_pass')


if __name__ == '__main__':
    unittest.main()
