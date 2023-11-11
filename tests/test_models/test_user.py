#!/usr/bin/python3
"""
This module provides test cases for the `User` class.
"""
import unittest
from datetime import datetime
from datetime import timedelta
from models.user import User
import json


class TestBaseModel(unittest.TestCase):
    """Provides test methods for the `User` class
    """
    def setUp(self):
        """Create two users of class `User` to user
        for subsequent test cases
        """
        self.user1 = User()
        self.user1.first_name = "Betty"
        self.user1.last_name = "Bar"
        self.user1.email = "betty@mail.com"
        self.user1.password = "root"

        self.user2 = User()
        self.user2.first_name = "William"
        self.user2.email = "william@mail.com"
        self.user2.password = "bingo!"

    def test_instance_creation_user(self):
        """Check if a user instance is created with
        properties inherited from `BaseModel`
        """
        self.assertIsInstance(self.user1, User)
        self.assertIsInstance(self.user2, User)

    def test_inheritance_user(self):
        """Check if attributes were correctly inherited
        from `BaseModel`
        """
        self.assertTrue(hasattr(self.user1, "id"))
        self.assertTrue(hasattr(self.user1, "created_at"))
        self.assertTrue(hasattr(self.user1, "updated_at"))

        self.assertTrue(hasattr(self.user2, "id"))
        self.assertTrue(hasattr(self.user2, "created_at"))
        self.assertTrue(hasattr(self.user2, "updated_at"))

    def test_attributes_user(self):
        """Check attributes of `User`
        """
        self.assertEqual(self.user1.first_name, "Betty")
        self.assertEqual(self.user1.last_name, "Bar")
        self.assertEqual(self.user1.email, "betty@mail.com")
        self.assertEqual(self.user1.password, "root")

        self.assertEqual(self.user2.first_name, "William")
        self.assertEqual(self.user2.last_name, "")
        self.assertEqual(self.user2.email, "william@mail.com")
        self.assertEqual(self.user2.password, "bingo!")

    def test_id_string_user(self):
        """Check if user `id` is a string
        """
        self.assertTrue(isinstance(self.user1.id, str))
        self.assertTrue(isinstance(self.user2.id, str))

    def test_id_uniqueness_user(self):
        """Check if user ids are unique
        """
        self.assertNotEqual(self.user1.id, self.user2.id)

    def test_time_format_user(self):
        """Check that the time format is correct
        """
        self.assertIsInstance(self.user1.created_at, datetime)
        self.assertIsInstance(self.user1.updated_at, datetime)

    def test_parts_string_representation_user(self):
        """Check if the string representation is correct
        """
        expected_str = "[User] ({}) {}".format(self.user1.id,
                                               self.user1.__dict__)

        self.assertEqual(str(self.user1), expected_str)

    def test_save_method_user(self):
        """Checks the save method
        """
        initial_updated_at = self.user1.updated_at
        self.user1.save()

        self.assertNotEqual(self.user1.updated_at, initial_updated_at)

    def test_to_dict_method_user(self):
        """Check the return type of the to_dict method, and if
        the dictionary has all the expected attributes for `User`
        """
        user1_dict = self.user1.to_dict()

        self.assertIsInstance(user1_dict, dict)
        self.assertIn("__class__", user1_dict)
        self.assertEqual(user1_dict["__class__"], "User")
        self.assertIn("id", user1_dict)
        self.assertIn("created_at", user1_dict)
        self.assertIn("updated_at", user1_dict)
        self.assertIn("email", user1_dict)
        self.assertIn("password", user1_dict)
        self.assertIn("first_name", user1_dict)
        self.assertIn("last_name", user1_dict)

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
        user1_dict = self.user1.to_dict()

        self.assertIsInstance(user1_dict["created_at"], str)
        self.assertIsInstance(user1_dict["updated_at"], str)
        self.assertEqual(
                datetime.strptime(user1_dict["created_at"],
                                  "%Y-%m-%dT%H:%M:%S.%f"),
                self.user1.created_at
        )
        self.assertEqual(
                datetime.strptime(user1_dict["updated_at"],
                                  "%Y-%m-%dT%H:%M:%S.%f"),
                self.user1.updated_at
        )

    def test_from_dict_method_user(self):
        """Check if previously converted instances are properly
        reloaded when a dictionary is provided as argument
        to BaseModel
        """
        user1_json = self.user1.to_dict()
        new_instance = User(**user1_json)

        self.assertEqual(self.user1.id, new_instance.id)
        self.assertEqual(self.user1.created_at, new_instance.created_at)
        self.assertEqual(self.user1.updated_at, new_instance.updated_at)


if __name__ == "__main__":
    unittest.main()
