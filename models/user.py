#!/usr/bin/python3
"""
This module provides the class `User` which inherits
from the class `BaseModel`
"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class inherits from `BaseModel` and
    creates a new user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
