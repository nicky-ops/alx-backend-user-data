#!/usr/bin/env python3
'''
Auth class to manage the API authentication
'''
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    '''
    This class implements API authentication
    '''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''
        Define paths that require authentication
        '''
        if path is None or excluded_paths is None or not excluded_paths:
            return True
        path = path.rstrip('/') + '/'
        for excluded_path in excluded_paths:
            excluded_path = excluded_path.rstrip('/') + '/'
            if path.startswith(excluded_path):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        HTTP authorization header
        """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """
        This function gets the current authenticated user
        """
        return None

    def session_cookie(self, request=None):
        '''
        this method gets cookie value from a request
        '''
        if request is None:
            return None
        session_name = getenv('SESSION_NAME', '_my_session_id')
        return request.cookies.get(session_name)
