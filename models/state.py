#!/usr/bin/python3
"""
This module provides the class `State` which inherits
from the class `BaseModel`
"""
from models.base_model import BaseModel


class State(BaseModel):
    """This class inherits from `BaseModel` and
    creates a sate
    """
    name = ""
