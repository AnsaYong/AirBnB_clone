#!/usr/bin/python3
"""
This module provides the class `Amenity` which inherits
from the class `BaseModel`
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """This class inherits from `BaseModel` and
    creates a new amenity
    """
    name = ""
