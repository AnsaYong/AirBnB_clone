#!/usr/bin/python3
"""
This module provides test cases for the `State` class.
"""
import unittest
from datetime import datetime
from datetime import timedelta
from models.state import State
import json


class TestBaseModel(unittest.TestCase):
    """Provides test methods for the `State` class
    """
    def setUp(self):
        """Create an instance of class `State` to use
        for subsequent test cases
        """
        self.my_state = State()
        self.my_state.name = "Alabama"

    def test_instance_creation_state(self):
        """Check if a state instance is created with
        properties inherited from `BaseModel`
        """
        self.assertIsInstance(self.my_state, State)

    def test_inheritance_state(self):
        """Check if attributes were correctly inherited
        from `BaseModel`
        """
        self.assertTrue(hasattr(self.my_state, "id"))
        self.assertTrue(hasattr(self.my_state, "created_at"))
        self.assertTrue(hasattr(self.my_state, "updated_at"))

    def test_attributes_state(self):
        """Check attributes of `State`
        """
        self.assertEqual(self.my_state.name, "Alabama")

    def test_id_string_state(self):
        """Check if state `id` is a string
        """
        self.assertTrue(isinstance(self.my_state.id, str))

    def test_id_uniqueness_state(self):
        """Check if state ids are unique
        """
        my_state2 = State()

        self.assertNotEqual(self.my_state.id, my_state2.id)

    def test_time_format_state(self):
        """Check that the time format is correct
        """
        self.assertIsInstance(self.my_state.created_at, datetime)
        self.assertIsInstance(self.my_state.updated_at, datetime)

    def test_parts_string_representation_state(self):
        """Check if the string representation is correct
        """
        expected_str = "[State] ({}) {}".format(self.my_state.id,
                                                self.my_state.__dict__)

        self.assertEqual(str(self.my_state), expected_str)

    def test_save_method_state(self):
        """Checks the save method
        """
        initial_updated_at = self.my_state.updated_at
        self.my_state.save()

        self.assertNotEqual(self.my_state.updated_at, initial_updated_at)

    def test_to_dict_method_state(self):
        """Check the return type of the to_dict method, and if
        the dictionary has all the expected attributes for `State`
        """
        my_state_dict = self.my_state.to_dict()

        self.assertIsInstance(my_state_dict, dict)
        self.assertIn("__class__", my_state_dict)
        self.assertEqual(my_state_dict["__class__"], "State")
        self.assertIn("id", my_state_dict)
        self.assertIn("created_at", my_state_dict)
        self.assertIn("updated_at", my_state_dict)
        self.assertIn("name", my_state_dict)

    def test_create_from_empty_dict_state(self):
        """Check the instance created from an empty dictionary
        """
        new_state = State(**{})

        self.assertIsInstance(new_state, State)
        self.assertTrue(hasattr(new_state, "id"))
        self.assertTrue(hasattr(new_state, "created_at"))
        self.assertTrue(hasattr(new_state, "updated_at"))
        self.assertTrue(hasattr(new_state, "name"))

        # Check the values
        self.assertIsNotNone(new_state.id)
        self.assertIsInstance(new_state.created_at, datetime)
        self.assertIsInstance(new_state.updated_at, datetime)

    def test_to_dict_datetime_format_state(self):
        """Check if the date format is correctly converted
        _from `datetime` to the expected string format
        """
        my_state_dict = self.my_state.to_dict()

        self.assertIsInstance(my_state_dict["created_at"], str)
        self.assertIsInstance(my_state_dict["updated_at"], str)
        self.assertEqual(
                datetime.strptime(my_state_dict["created_at"],
                                  "%Y-%m-%dT%H:%M:%S.%f"),
                self.my_state.created_at
        )
        self.assertEqual(
                datetime.strptime(my_state_dict["updated_at"],
                                  "%Y-%m-%dT%H:%M:%S.%f"),
                self.my_state.updated_at
        )

    def test_from_dict_method_state(self):
        """Check if previously converted instances are properly
        reloaded when a dictionary is provided as argument
        to BaseModel
        """
        state_json = self.my_state.to_dict()
        new_instance = State(**state_json)

        self.assertEqual(self.my_state.id, new_instance.id)
        self.assertEqual(self.my_state.created_at, new_instance.created_at)
        self.assertEqual(self.my_state.updated_at, new_instance.updated_at)


if __name__ == "__main__":
    unittest.main()
