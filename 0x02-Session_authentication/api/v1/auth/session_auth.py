#!/usr/bin/env python3
'''
Session authentication
'''
from api.v1.auth.auth import Auth
import uuid
from models.user import User


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
        session_cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_cookie)
        user = User.get(user_id)
        return user

    def destroy_session(self, request=None):
        '''
        This function deletes the user session/logout
        '''
        if request is None:
            return False
        session_cookie = self.session_cookie(request)
        if session_cookie is None:
            return False
        user_id = self.user_id_for_session_id(session_cookie)
        if user_id is None:
            return False
        del self.user_id_by_session_id[session_cookie]
        return True
