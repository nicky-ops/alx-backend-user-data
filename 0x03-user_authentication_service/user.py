#!/usr/bin/env python3
'''
User model
'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class User(Base):
    '''
    This class defines an SQLAlchemy model named User for a database table
    named users

    Fields:
        id: integer type, primary key
        email: a non nullable string
        hashed_password: a non nullable string
        session_id: a nullable string
        reset_token: a nullable string
    '''
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
