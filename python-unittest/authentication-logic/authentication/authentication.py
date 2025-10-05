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

from pathlib import Path
import string
import logging
import os


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

if not logger.hasHandlers():
    # Ensure logs directory exists
    os.makedirs("logs", exist_ok=True)

    # Set and config file handlers
    file_handler = logging.FileHandler("logs/fileprocessor_logs.log")
    file_handler.setLevel(logging.WARNING)
    file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(file_formatter)

    # Set and config stream handler
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
    stream_handler.setFormatter(stream_formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)


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
        logger.debug("Connecting to SQLite database")
        self.con = sqlite3.connect("authentication.db")
        logger.debug("Connected to SQLite database")

        self.cur = self.con.cursor()
        self.database()

    def database(self) -> None:
        """
        Create the accounts table if missing.
        """
        self.con.execute(
            "CREATE TABLE IF NOT EXISTS accounts (username TEXT UNIQUE, password TEXT UNIQUE)"
        )
        logger.debug("Creating accounts table if not exists")

        self.con.commit()

    def hash_password(self, password: str) -> str:
        """
        Hash a password using SHA-256.

        Arguments:
            password (str): The password to hash.

        Returns:
            str: The SHA-256 hex digest of the password.
        """
        logger.debug("Hashing password")
        hashed = hashlib.sha256(password.encode()).hexdigest()
        logger.debug(f"Hashed password: {hashed}")

        return hashed

    def existance_username(self, username: str) -> bool:
        """
        Check if a username exists.

        Arguments:
            username (str): The username to check.

        Returns:
            bool: True if the username exists, False otherwise.
        """
        logger.debug(f"Checking existence of username: {username}")
        exists = self.cur.execute(
            "SELECT 1 FROM accounts WHERE username = ?",
            (username,)
        ).fetchone()

        return exists is not None

    def validation_login(self, username: str, password: str) -> bool:
        """
        Validate a username/password pair.
        Checks if the provided username exists and if the associated password matches.

        Arguments:
            username (str): The username to validate.
            password (str): The password to validate.

        Returns:
            bool: True if the username/password pair is valid, False otherwise.
        """
        logger.debug(f"Validating login for username: {username}")
        # Retrieve stored password for the username (if any)
        row = self.cur.execute(
            "SELECT password FROM accounts WHERE username = ?",
            (username,)
        ).fetchone()

        if not row:
            # Username not found
            logger.warning("Login attempt for non-existing username: %s", username)
            raise ValueError("username not found")

        stored_password = row[0]
        if stored_password != password:
            # Password mismatch
            logger.warning("Password mismatch for username: %s", username)
            raise ValueError("incorrect password")

        return True

    def register(self, username: str, password: str) -> None:
        """
        Register a new user interactively.
        """
        hashed_password = self.hash_password(password)

        if self.existance_username(username):
            logger.error("Username already exists!")
            raise ValueError("username already exists")

        else:
            self.cur.execute(
                "INSERT INTO accounts(username, password) VALUES(?, ?)",
                (username, hashed_password)
            )

            self.con.commit()
            logger.info("User registered successfully.")

    def login(self, username: str, password: str) -> None:
        """
        Login an existing user interactively.
        """
        hashed_password = self.hash_password(password)

        if self.validation_login(username, hashed_password):
            logger.info("Login successful!")
        else:
            logger.error("Incorrect username or password!")


def get_user_input() -> tuple[str, str, str]:
    """
    Get user input for username, password, and action (login/register).

    Returns:
        tuple: A tuple containing the username, password, and action.
    """
    try:
        action = input(
            f"Authentication System\n1) Login\n2) Register\nPlease select an option: "
        ).strip()

        if action not in ["1", "2", "Login".lower(), "Register".lower()]:
            logger.error("Invalid option selected.")
            raise ValueError(
                "Invalid option selected. Please choose '1' for Login or '2' for Register."
            )

        username = input("Please Enter Your Name: ")
        password = getpass.getpass("Please Enter Your Password: ")

        logger.info(f"User provided username: {username}")
        logger.info(f"User provided password: {password}")
        logger.info(f"User selected option: {action}")

        return username, password, action

    except EOFError:
        logger.exception("End of file error. No input received.")
        logger.warning("-" * 40)
        # Re-raise the occured exception
        raise

    except KeyboardInterrupt:
        logger.exception("Program interrupted by user.")
        logger.warning("-" * 40)
        # Re-raise the occured exception
        raise

    except Exception as e:
        logger.exception(f"An unexpected error occurred: {e}")
        logger.warning("-" * 40)
        # Re-raise the occured exception
        raise

def main():
    """
    Prompts the user to choose between 'register' or 'login' 
    and calls the corresponding method. Handles invalid input gracefully.
    """
    auth = UserAuthentication()

    try:
        # Get user input for username, password, and action
        username, password, user_input = get_user_input()

        if (user_input == "1") or (user_input == "Login".lower()):
            auth.login(username, password)
            logger.info("Login attempted.")
        elif (user_input == "2") or (user_input == "Register".lower()):
            auth.register(username, password)
            logger.info("Registration attempted.")

    except Exception as occured_exception:
        logger.exception(f"An error occurred during authentication: {occured_exception}")
        logger.warning("-" * 40)
        # Re-raise the occured exception
        raise

    finally:
        auth.con.close()
        logger.debug("Database connection closed.")


if __name__ == "__main__":
    main()
