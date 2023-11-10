#!/usr/bin/python3
"""
This module provides the class `Review` which inherits
from the class `BaseModel`
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This class inherits from `BaseModel` and
    creates a review
    """
    place_id = ""
    user_id = ""
    text = ""
