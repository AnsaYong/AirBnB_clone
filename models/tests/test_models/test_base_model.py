#!/usr/bin/python3
"""
Test module for the ``BaseModel`` class.
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    description
    """
    def test_id_string(self):
        """
        description
        """
        base = BaseModel()
        self.assertTrue(isinstance(base.id, str))

    def test_id(self):
        """
        Check if id is unique
        """
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)

    def test_time_format(self):
        """
        Check that the time format is changed
        """
        base1 = BaseModel()
        self.assertTrue(isinstance(base1.created_at, datetime))

    def test_parts_string_representation(self):
        """
        Check if the string representation has specific parts
        """
        base1 = BaseModel()

        # Check if the string contains patterns for class name, id, dates
        str_representation = str(base1)
        self.assertIn("[BaseModel]", str_representation)
        self.assertIn(" ({})".format(base1.id), str_representation)
        self.assertIn(str(base1.__dict__), str_representation)
