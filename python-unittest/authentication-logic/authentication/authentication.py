import getpass
import hashlib
import sqlite3


class UserAuthentication:

    def __init__(self):
        self.con = sqlite3.connect('Authentication.db')
        self.cur = self.con.cursor()
        self.database()

    def database(self):
        self.con.execute('CREATE TABLE IF NOT EXISTS users (username TEXT UNIQUE, password TEXT UNIQUE)')
        self.con.commit()

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def exist_username(self, username):
        return self.cur.execute('SELECT 1 FROM users WHERE username = ?', (username,)).fetchone()

    def exist_password(self, password):
        return self.cur.execute('SELECT 1 FROM users WHERE password = ?', (password,)).fetchone()

    def validation_login(self, username, password):
        return self.cur.execute('SELECT 1 FROM users WHERE username = ? AND password = ?', (username, password))

    def register(self):
        username = input('Please Enter Your Name: ')
        password = getpass.getpass('Please Enter Your Password: ')
        self.hash_password(password)

        if self.exist_username(username):
            print('username already exists!')

        elif self.exist_password(password):
            print('password already exists!')

        else:
            self.cur.execute('INSERT INTO users(username, password) VALUES(?, ?)', (username, password))
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

    def main(self):
        match input('register or login ?'):
            case 'register':
                self.register()
            
            case 'login':
                self.login() 

if __name__ == '__main__':
    auth = UserAuthentication()
    auth.main()
