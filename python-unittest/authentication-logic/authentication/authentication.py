"""
A simple user authentication module using SQLite.

Provides a small interactive utility to register and login users. Passwords
are stored (intended to be) as SHA-256 hashes in a local SQLite database.

Classes:
    UserAuthentication: Create/manage the local accounts database and provide
        register/login helper methods for interactive use.

Functions:
    main: Run the interactive prompt to choose register or login.
"""

import getpass
import hashlib
import sqlite3


class UserAuthentication:
    """
    Handle user authentication with a local SQLite database.

    Methods:
        database() -> None
        hash_password(password: str) -> str
        existance_username(username: str) -> bool
        existance_password(password: str) -> bool
        validation_login(username: str, password: str) -> bool
        register() -> None
        login() -> None
    """

    def __init__(self):
        """
        Initialize the database connection and ensure the accounts table exists.
        """
        self.con = sqlite3.connect("authentication.db")
        self.cur = self.con.cursor()
        self.database()

    def database(self) -> None:
        """
        Create the accounts table if missing.
        """
        self.con.execute(
            "CREATE TABLE IF NOT EXISTS accounts (username TEXT UNIQUE, password TEXT UNIQUE)"
        )
        self.con.commit()

    def hash_password(self, password: str) -> str:
        """
        Hash a password using SHA-256.

        Arguments:
            password (str): The password to hash.

        Returns:
            str: The SHA-256 hex digest of the password.
        """
        return hashlib.sha256(password.encode()).hexdigest()

    def existance_username(self, username: str) -> bool:
        """
        Check if a username exists.

        Arguments:
            username (str): The username to check.

        Returns:
            bool: True if the username exists, False otherwise.
        """
        return self.cur.execute(
            "SELECT 1 FROM accounts WHERE username = ?",
            (username,)
        ).fetchone()

    def existance_password(self, password: str) -> bool:
        """
        Check if a password hash exists.

        Arguments:
            password (str): The password hash to check.

        Returns:
            bool: True if the password hash exists, False otherwise.
        """
        return self.cur.execute(
            "SELECT 1 FROM accounts WHERE password = ?",
            (password,)
        ).fetchone()

    def validation_login(self, username: str, password: str) -> bool:
        """
        Validate a username/password pair.

        Arguments:
            username (str): The username to validate.
            password (str): The password to validate.

        Returns:
            bool: True if the username/password pair is valid, False otherwise.
        """
        return self.cur.execute(
            "SELECT 1 FROM accounts WHERE username = ? AND password = ?",
            (username, password)
        ).fetchone()

    def register(self) -> None:
        """
        Register a new user interactively.
        """

        username = input("Please Enter Your Name: ")
        password = getpass.getpass("Please Enter Your Password: ")
        hashed_password = self.hash_password(password)

        if self.existance_username(username):
            print("username already exists!")

        elif self.existance_password(hashed_password):
            print("password already exists!")

        else:
            self.cur.execute(
                "INSERT INTO accounts(username, password) VALUES(?, ?)",
                (username, hashed_password)
            )

            self.con.commit()
            print("Register successfully!")

    def login(self) -> None:
        """
        Login an existing user interactively.
        """

        username = input("Please Enter Your Name: ")
        password = getpass.getpass("Please Enter Your Password: ")
        hashed_password = self.hash_password(password)

        if self.validation_login(username, hashed_password):
            print("Login successfully! welcome to your panel")

        else:
            print("Incorrect username or password!")


def main():
    """
    Prompts the user to choose between 'register' or 'login' 
    and calls the corresponding method. Handles invalid input gracefully.
    """
    auth = UserAuthentication()

    user_input = input(f"Authentication System\n1) Login\n2) Register\nPlease select an option: ")

    if (user_input == "1") or (user_input == "Login".lower()):
        auth.login()
    elif (user_input == "2") or (user_input == "Register".lower()):
        auth.register()
    else:
        print("Invalid Input")


if __name__ == "__main__":
    main()
