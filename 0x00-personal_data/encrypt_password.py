#!/usr/bin/env python3
'''
Encrypting passwords
'''
import bcrypt


def hash_password(password: str) -> bytes:
    '''
    This function hashes a password using bcrypt
    '''
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed_pw
