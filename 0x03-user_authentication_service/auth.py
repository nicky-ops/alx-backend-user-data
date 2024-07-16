#!/usr/bin/env python3
'''
Hash passwords
'''
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    '''
    This function hashes a password using bcrypt
    '''
    salt = bcrypt.gensalt()
    hashed_pwd = bcrypt.hashpw(password.encode(), salt)
    return hashed_pwd


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        '''
        This method registers a new user
        '''
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_pwd = _hash_password(password)
            new_user = self._db.add_user(email, hashed_pwd)
            return new_user
        else:
            raise ValueError(f'user {email} already exists')

    def valid_login(self, email: str, password: str) -> bool:
        '''
        This method validates user credentials
        '''
        try:
            user = self._db.find_user_by(email=email)
            if user:
                if bcrypt.checkpw(password.encode(), user.hashed_password):
                    return True
                else:
                    return False
        except NoResultFound:
            return False
