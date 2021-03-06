# coding: utf-8
import decimal
from getpass import getpass
import json

USERS_FILENAME = 'users.json'

class User:

    _USERS = []

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def check_auth(self, login, password):
        return self.login == login and self.password == password

    @staticmethod
    def create_root_user():
        login = input('Create root user login, please:')
        password = getpass('Create root user password, please:')

        root = User(login, password)
        User._USERS.append(root)

        User._save_users()

    @staticmethod
    def _save_users():

        # сохраняем объект в json
        json.dump(User._USERS, open(USERS_FILENAME, 'w'))

    @staticmethod
    def load_users():
        User._USERS = json.load(open(USERS_FILENAME))

    @staticmethod
    def login(name, password):
        for user in User._USERS:
            if user.check_auth(name, password):
                return user


User._USERS.append(User('root', '1234'))
