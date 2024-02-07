#!/usr/bin/python3
""" holds class User"""
import hashlib
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Representation of a user """
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
        
    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        user_dict = super().to_dict()
        if 'password' in user_dict and models.storage_t != 'db':
            del user_dict['password']
        return user_dict

    @property
    def password(self):
        """Getter method for password"""
        return self._password

    @password.setter
    def password(self, value):
        """Setter method for password"""
        if isinstance(value, str):
            self._password = hashlib.md5(value.encode()).hexdigest()
        else:
            self._password = value