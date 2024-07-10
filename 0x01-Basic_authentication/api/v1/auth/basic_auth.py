#!/usr/bin/env python3
'''
Basic authentication
'''
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    '''
    This class defines Basic authentication
    '''
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        '''
        extract and return the Base64 part of the Authorization header
        for a Basic authentication
        '''
        if authorization_header is None or type(authorization_header) != str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split("Basic ", 1)[1]
