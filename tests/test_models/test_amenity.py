#!/usr/bin/python3
"""
This module provides test cases for the `Amenity` class.
"""
import unittest
from datetime import datetime
from models.amenity import Amenity


class TestBaseModel(unittest.TestCase):
    """
    Provides test methods for the `Amenity` class
    """
    def setUp(self):
        """Create an instance of class `Amenity` to use
        for subsequent test cases
        """
        self.my_amenity = Amenity()
        self.my_amenity.name = "Swimming Pool"

    def test_instance_creation_amenity(self):
        """Check if an Amenity instance is created with
        properties inherited from `BaseModel`
        """
        self.assertIsInstance(self.my_amenity, Amenity)

    def test_inheritance_amenity(self):
        """Check if attributes were correctly inherited
        from `BaseModel`
        """
        self.assertTrue(hasattr(self.my_amenity, "id"))
        self.assertTrue(hasattr(self.my_amenity, "created_at"))
        self.assertTrue(hasattr(self.my_amenity, "updated_at"))

    def test_attributes_amenity(self):
        """Check attributes of `Amenity`
        """
        self.assertEqual(self.my_amenity.name, "Swimming Pool")

    def test_id_string_amenity(self):
        """Check if Amenity `id` is a string
        """
        self.assertTrue(isinstance(self.my_amenity.id, str))

    def test_id_uniqueness_amenity(self):
        """Check if Amenity ids are unique
        """
        my_amenity2 = Amenity()

        self.assertNotEqual(self.my_amenity.id, my_amenity2.id)

    def test_time_format_amenity(self):
        """Check that the time format is correct
        """
        self.assertIsInstance(self.my_amenity.created_at, datetime)
        self.assertIsInstance(self.my_amenity.updated_at, datetime)

    def test_parts_string_representation_amenity(self):
        """Check if the string representation is correct
        """
        expected_str = "[Amenity] ({}) {}".format(self.my_amenity.id,
                                                  self.my_amenity.__dict__)

        self.assertEqual(str(self.my_amenity), expected_str)

    def test_save_method_amenity(self):
        """Checks the save method
        """
        initial_updated_at = self.my_amenity.updated_at
        self.my_amenity.save()

        self.assertNotEqual(self.my_amenity.updated_at, initial_updated_at)

    def test_to_dict_method_amenity(self):
        """Check the return type of the to_dict method, and if
        the dictionary has all the expected attributes for `Amenity`
        """
        my_amenity_dict = self.my_amenity.to_dict()

        self.assertIsInstance(my_amenity_dict, dict)
        self.assertIn("__class__", my_amenity_dict)
        self.assertEqual(my_amenity_dict["__class__"], "Amenity")
        self.assertIn("id", my_amenity_dict)
        self.assertIn("created_at", my_amenity_dict)
        self.assertIn("updated_at", my_amenity_dict)
        self.assertIn("name", my_amenity_dict)

    def test_create_from_empty_dict_amenity(self):
        """Check the instance created from an empty dictionary
        """
        new_amenity = Amenity(**{})

        self.assertIsInstance(new_amenity, Amenity)
        self.assertTrue(hasattr(new_amenity, "id"))
        self.assertTrue(hasattr(new_amenity, "created_at"))
        self.assertTrue(hasattr(new_amenity, "updated_at"))
        self.assertTrue(hasattr(new_amenity, "name"))

        # Check the values
        self.assertIsNotNone(new_amenity.id)
        self.assertIsInstance(new_amenity.created_at, datetime)
        self.assertIsInstance(new_amenity.updated_at, datetime)

    def test_to_dict_datetime_format_amenity(self):
        """Check if the date format is correctly converted
        _from `datetime` to the expected string format
        """
        my_amenity_dict = self.my_amenity.to_dict()

        self.assertIsInstance(my_amenity_dict["created_at"], str)
        self.assertIsInstance(my_amenity_dict["updated_at"], str)
        self.assertEqual(
                datetime.strptime(my_amenity_dict["created_at"],
                                  "%Y-%m-%dT%H:%M:%S.%f"),
                self.my_amenity.created_at
        )
        self.assertEqual(
                datetime.strptime(my_amenity_dict["updated_at"],
                                  "%Y-%m-%dT%H:%M:%S.%f"),
                self.my_amenity.updated_at
        )

    def test_from_dict_method_amenity(self):
        """Check if previously converted instances are properly
        reloaded when a dictionary is provided as argument
        to BaseModel
        """
        amenity_json = self.my_amenity.to_dict()
        new_instance = Amenity(**amenity_json)

        self.assertEqual(self.my_amenity.id, new_instance.id)
        self.assertEqual(self.my_amenity.created_at, new_instance.created_at)
        self.assertEqual(self.my_amenity.updated_at, new_instance.updated_at)


if __name__ == "__main__":
    unittest.main()
