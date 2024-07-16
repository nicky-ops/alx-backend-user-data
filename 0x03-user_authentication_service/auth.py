#!/usr/bin/env python3
'''
Hash passwords
'''
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    '''
    This function hashes a password using bcrypt
    '''
    salt = bcrypt.gensalt()
    hashed_pwd = bcrypt.hashpw(password.encode(), salt)
    return hashed_pwd


def _generate_uuid() -> str:
    '''
    This method generates a uuid using uuid4
    returns a string representation of the new UUID
    '''
    unique_id = uuid4()
    return str(unique_id)


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

    def create_session(self, email: str) -> str:
        '''
        This method takes an email string argument and creates a session ID
        '''
        try:
            user = self._db.find_user_by(email=email)
            if user:
                session_id = _generate_uuid()
                user.session_id = session_id
                return session_id
        except NoResultFound:
            return None
            return None
