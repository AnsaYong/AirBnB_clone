#!/usr/bin/python3
"""
This module provides test cases for the `BaseModel` class.
"""
import unittest
from datetime import datetime
from datetime import timedelta
from models.base_model import BaseModel
import json


class TestBaseModel(unittest.TestCase):
    """
    Provides test methods for the `BaseModel` class
    """
    def test_instance_creation(self):
        """Check if a base instance is created properly
        """
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)
        self.assertTrue(hasattr(base, "id"))
        self.assertTrue(hasattr(base, "created_at"))
        self.assertTrue(hasattr(base, "updated_at"))

    def test_instance_creation_extra_attr(self):
        """
        Test adding extra attributes to an instance
        """
        base = BaseModel()
        base.name = "My_First_model"
        base.my_number = 89
        self.assertEqual(base.name, "My_First_model")
        self.assertEqual(base.my_number, 89)

    def test_id_string(self):
        """
        description
        """
        base = BaseModel()
        self.assertTrue(isinstance(base.id, str))

    def test_id_uniqueness(self):
        """Check if id is unique
        """
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)

    def test_time_format(self):
        """
        Check that the time format is changed
        """
        base1 = BaseModel()
        self.assertIsInstance(base1.created_at, datetime)
        self.assertIsInstance(base1.updated_at, datetime)

        # Truncate the microsecond part
        truncated_created_at = base1.created_at.replace(microsecond=0)
        truncated_updated_at = base1.updated_at.replace(microsecond=0)

        self.assertAlmostEqual(truncated_created_at, truncated_updated_at)

    def test_parts_string_representation(self):
        """
        Check if the string representation has specific parts
        """
        base1 = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(base1.id, base1.__dict__)
        self.assertEqual(str(base1), expected_str)

    def test_save_method(self):
        """
        Checks the save method
        """
        base = BaseModel()
        initial_updated_at = base.updated_at
        base.save()
        self.assertNotEqual(base.updated_at, initial_updated_at)

    def test_to_dict_method(self):
        """
        Check the return type of the to_dict method
        """
        base = BaseModel()
        base_dict = base.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertIn("__class__", base_dict)
        self.assertEqual(base_dict["__class__"], "BaseModel")
        self.assertIn("id", base_dict)
        self.assertIn("created_at", base_dict)
        self.assertIn("updated_at", base_dict)

    def test_create_from_empty_dict(self):
        """
        Check the instance created from an empty dictionary
        """
        base = BaseModel(**{})
        self.assertIsInstance(base, BaseModel)
        self.assertTrue(hasattr(base, "id"))
        self.assertTrue(hasattr(base, "created_at"))
        self.assertTrue(hasattr(base, "updated_at"))

        # Check the values
        self.assertIsNotNone(base.id)
        self.assertIsInstance(base.created_at, datetime)
        self.assertIsInstance(base.updated_at, datetime)

        truncated_created_at = base.created_at.replace(microsecond=0)
        truncated_updated_at = base.updated_at.replace(microsecond=0)

        self.assertEqual(truncated_created_at, truncated_updated_at)

    def test_to_dict_datetime_format(self):
        """
        Check if the date format is correctly converted
        _from `datetime` to the correct string format
        """
        base = BaseModel()
        base_dict = base.to_dict()
        self.assertIsInstance(base_dict["created_at"], str)
        self.assertIsInstance(base_dict["updated_at"], str)
        self.assertEqual(
                datetime.strptime(base_dict["created_at"],
                                  "%Y-%m-%dT%H:%M:%S.%f"),
                base.created_at
        )
        self.assertEqual(
                datetime.strptime(base_dict["updated_at"],
                                  "%Y-%m-%dT%H:%M:%S.%f"),
                base.updated_at
        )

    def test_from_dict_method(self):
        """
        Check if previously converted instances are properly
        reloaded when a dictionary is provided as argument
        to BaseModel
        """
        base = BaseModel()
        base_json = base.to_dict()
        new_instance = BaseModel(**base_json)
        self.assertEqual(base.id, new_instance.id)
        self.assertEqual(base.created_at, new_instance.created_at)
        self.assertEqual(base.updated_at, new_instance.updated_at)


if __name__ == "__main__":
    unittest.main()
