import getpass
import hashlib
import sqlite3


class UserAuthentication:
    """
    A class to handle user registration and authentication using SQLite.

    This class provides methods to register new users, ensuring that usernames
    and passwords are unique, and to authenticate existing users. Passwords
    are securely stored using SHA-256 hashing.

    Attributes:
        con (sqlite3.Connection): SQLite database connection object.
        cur (sqlite3.Cursor): SQLite cursor object for executing queries.

    Methods:
        database():
            Creates the 'users' table if it does not already exist.
        
        hash_password(password: str) -> str:
            Returns the SHA-256 hash of the given password.
        
        existance_username(username: str) -> bool:
            Checks if a username already exists in the database.

        existance_password(password: str) -> bool:
            Checks if a hashed password already exists in the database.
        
        validation_login(username: str, password: str) -> bool:
            Validates that the provided username and password combination exists.
        
        register():
            Prompts the user to enter a username and password, hashes the password,
            and inserts the new user into the database if both are unique.
        
        login():
            Prompts the user to enter a username and password, hashes the password,
            and verifies the credentials against the database.
        """

    def __init__(self):
        self.con = sqlite3.connect('Authentication.db')
        self.cur = self.con.cursor()
        self.database()

    def database(self):
        self.con.execute('CREATE TABLE IF NOT EXISTS accounts (username TEXT UNIQUE, password TEXT UNIQUE)')
        self.con.commit()

    def hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def existance_username(self, username: str) -> bool:
        return self.cur.execute('SELECT 1 FROM accounts WHERE username = ?', (username,)).fetchone()

    def existance_password(self, password: str) -> bool:
        return self.cur.execute('SELECT 1 FROM accounts WHERE password = ?', (password,)).fetchone()

    def validation_login(self, username: str, password: str) -> bool:
        return self.cur.execute('SELECT 1 FROM accounts WHERE username = ? AND password = ?', (username, password)).fetchone()

    def register(self):
        username = input('Please Enter Your Name: ')
        password = getpass.getpass('Please Enter Your Password: ')
        self.hash_password(password)

        if self.existance_username(username):
            print('username already exists!')

        elif self.existance_password(password):
            print('password already exists!')

        else:
            self.cur.execute('INSERT INTO accounts(username, password) VALUES(?, ?)', (username, password))
            self.con.commit()
            print('Register successfully!')

    def login(self):
        username = input('Please Enter Your Name: ')
        password = getpass.getpass('Please Enter Your Password: ')
        self.hash_password(password)

        if self.validation_login(username, password):
            print('Login successfully! welcome to your panel')

        else:
            print('Incorrect username or password!')


def main():
    """
    Prompts the user to choose between 'register' or 'login' 
    and calls the corresponding method. Handles invalid input gracefully.
    """
    auth = UserAuthentication()

    User_Input = input(f''' what do you want to do?
1) Login
2) Register
''')

    if (User_Input == '1') or (User_Input == 'Login'.lower()):
        auth.login()

    elif (User_Input == '2') or (User_Input == 'Register'.lower()):
        auth.register()

    else:
        print('Invalid Input')


if __name__ == '__main__':
    main()
