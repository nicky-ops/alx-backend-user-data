#!/usr/bin/env python3
'''
Hash passwords
'''
import bcrypt


def _hash_password(password: str) -> bytes:
    '''
    This function hashes a password using bcrypt
    '''
    salt = bcrypt.gensalt()
    hashed_pwd = bcrypt.hashpw(password.encode(), salt)
    return hashed_pwd
