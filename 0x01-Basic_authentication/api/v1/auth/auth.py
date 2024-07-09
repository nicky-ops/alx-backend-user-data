#!/usr/bin/env python3
'''
Auth class to manage the API authentication
'''
from flask import request
from typing import List, TypeVar


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
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        This function gets the current authenticated user
        """
        return None
