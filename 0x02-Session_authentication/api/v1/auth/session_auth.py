#!/usr/bin/env python3
'''
Session authentication
'''
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    '''
    This class implements session based authentication
    '''
    user_id_by_session_id = {}
    def create_session(self, user_id: str = None) -> str:
        '''
        This function creates a session and returns the session ID
        '''
        if user_id is None or type(user_id) != str:
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

