#!/usr/bin/python3
"""
This module provides test cases for the `User` class.
"""
import unittest
from datetime import datetime
from datetime import timedelta
from models.user import User
import json


class TestUser(unittest.TestCase):
    """Provides test methods for the `User` class
    """
    def setUp(self):
        """Create two users of class `User` to user
        for subsequent test cases
        """
        self.user = User()
        self.user.first_name = "Betty"
        self.user.last_name = "Bar"
        self.user.email = "betty@mail.com"
        self.user.password = "root"

    def test_instance_creation_user(self):
        """Check if a user instance is created with
        properties inherited from `BaseModel`
        """
        self.assertIsInstance(self.user, User)

    def test_inheritance_user(self):
        """Check if attributes were correctly inherited
        from `BaseModel`
        """
        self.assertTrue(hasattr(self.user, "id"))
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))

    def test_attributes_user(self):
        """Check attributes of `User`
        """
        self.assertEqual(self.user.first_name, "Betty")
        self.assertEqual(self.user.last_name, "Bar")
        self.assertEqual(self.user.email, "betty@mail.com")
        self.assertEqual(self.user.password, "root")

    def test_id_string_user(self):
        """Check if user `id` is a string
        """
        self.assertTrue(isinstance(self.user.id, str))

    def test_id_uniqueness_user(self):
        """Check if user ids are unique
        """
        new_user = User()
        new_user.first_name = "william"
        new_user.last_name = "Thomas"
        new_user.password = "bingo!"
        new_user.email = "william@mail.com"

        self.assertNotEqual(self.user.id, new_user.id)
        self.assertEqual(new_user.first_name, "william")
        self.assertEqual(new_user.last_name, "Thomas")
        self.assertEqual(new_user.password, "bingo!")
        self.assertEqual(new_user.email, "william@mail.com")

    def test_time_format_user(self):
        """Check that the time format is correct
        """
        self.assertIsInstance(self.user.created_at, datetime)
        self.assertIsInstance(self.user.updated_at, datetime)

    def test_parts_string_representation_user(self):
        """Check if the string representation is correct
        """
        expected_str = "[User] ({}) {}".format(self.user.id,
                                               self.user.__dict__)

        self.assertEqual(str(self.user), expected_str)

    def test_save_method_user(self):
        """Checks the save method
        """
        initial_updated_at = self.user.updated_at
        self.user.save()

        self.assertNotEqual(self.user.updated_at, initial_updated_at)

    def test_to_dict_method_user(self):
        """Check the return type of the to_dict method, and if
        the dictionary has all the expected attributes for `User`
        """
        user_dict = self.user.to_dict()

        self.assertIsInstance(user_dict, dict)
        self.assertIn("__class__", user_dict)
        self.assertEqual(user_dict["__class__"], "User")
        self.assertIn("id", user_dict)
        self.assertIn("created_at", user_dict)
        self.assertIn("updated_at", user_dict)
        self.assertIn("email", user_dict)
        self.assertIn("password", user_dict)
        self.assertIn("first_name", user_dict)
        self.assertIn("last_name", user_dict)

    def test_create_from_empty_dict_user(self):
        """Check the instance created from an empty dictionary
        """
        new_user = User(**{})

        self.assertIsInstance(new_user, User)
        self.assertTrue(hasattr(new_user, "id"))
        self.assertTrue(hasattr(new_user, "created_at"))
        self.assertTrue(hasattr(new_user, "updated_at"))
        self.assertTrue(hasattr(new_user, "email"))
        self.assertTrue(hasattr(new_user, "password"))
        self.assertTrue(hasattr(new_user, "first_name"))
        self.assertTrue(hasattr(new_user, "last_name"))

        # Check the values
        self.assertIsNotNone(new_user.id)
        self.assertIsInstance(new_user.created_at, datetime)
        self.assertIsInstance(new_user.updated_at, datetime)

    def test_to_dict_datetime_format_user(self):
        """Check if the date format is correctly converted
        _from `datetime` to the expected string format
        """
        user_dict = self.user.to_dict()

        self.assertIsInstance(user_dict["created_at"], str)
        self.assertIsInstance(user_dict["updated_at"], str)
        self.assertEqual(
                datetime.strptime(user_dict["created_at"],
                                  "%Y-%m-%dT%H:%M:%S.%f"),
                self.user.created_at
        )
        self.assertEqual(
                datetime.strptime(user_dict["updated_at"],
                                  "%Y-%m-%dT%H:%M:%S.%f"),
                self.user.updated_at
        )

    def test_from_dict_method_user(self):
        """Check if previously converted instances are properly
        reloaded when a dictionary is provided as argument
        to BaseModel
        """
        user_json = self.user.to_dict()
        new_instance = User(**user_json)

        self.assertEqual(self.user.id, new_instance.id)
        self.assertEqual(self.user.created_at, new_instance.created_at)
        self.assertEqual(self.user.updated_at, new_instance.updated_at)


if __name__ == "__main__":
    unittest.main()
