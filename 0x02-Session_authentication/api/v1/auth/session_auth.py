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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        '''
        User ID for session ID
        '''
        if session_id is None or type(session_id) != str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        '''
        This method uses Session ID to identify a User
        '''
        if request is None:
            return None
        session_cookie = self.session_cookie(request)
        if session_cookie is None:
            return None
        user_id = self.user_id_for_session_id(session_cookie)
        if user_id is None:
            return None
        return User.get(user_id)
