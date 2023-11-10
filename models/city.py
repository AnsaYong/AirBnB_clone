#!/usr/bin/python3
"""
This module provides the class `City` which inherits
from the class `BaseModel`
"""
from models.base_model import BaseModel


class City(BaseModel):
    """This class inherits from `BaseModel` and
    creates a new state
    """
    name = ""
    state_id = ""
