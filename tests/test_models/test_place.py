#!/usr/bin/python3
"""
This module provides test cases for the `Place` class.
"""
import unittest
from datetime import datetime
from models.place import Place
from models.city import City
from models.user import User
from models.amenity import Amenity


class TestPlace(unittest.TestCase):
    """Provides test methods for the `Place` class
    """
    def setUp(self):
        """Create an instance of class `Place` to use
        for subsequent test cases
        """
        # Create instances of City, User, and Amenity for IDs
        self.city_instance = City()
        self.user_instance = User()
        self.amenity_instance = Amenity()

        # Set IDs for Place attributes
        self.my_place = Place()
        self.my_place.city_id = self.city_instance.id
        self.my_place.user_id = self.user_instance.id
        self.my_place.name = "Bullrush Cottage"
        self.my_place.description = "Spectacular view of Langeberg Mountains"
        self.my_place.number_rooms = 2
        self.my_place.number_bathrooms = 1
        self.my_place.max_guest = 4
        self.my_place.price_by_night = 100
        self.my_place.latitude = 40.7128
        self.my_place.longitude = -74.0060
        self.my_place.amenity_ids = [self.amenity_instance.id]

    def test_instance_creation_place(self):
        """Check if a Place instance is created with
        properties inherited from `BaseModel`
        """
        self.assertIsInstance(self.my_place, Place)

    def test_inheritance_place(self):
        """Check if attributes were correctly inherited
        from `BaseModel`
        """
        self.assertTrue(hasattr(self.my_place, "id"))
        self.assertTrue(hasattr(self.my_place, "created_at"))
        self.assertTrue(hasattr(self.my_place, "updated_at"))

    def test_attributes_place(self):
        """Check attributes of `Place`
        """
        self.assertEqual(self.my_place.user_id, self.user_instance.id)
        self.assertEqual(self.my_place.name, "Bullrush Cottage")
        self.assertEqual(self.my_place.description,
                         "Spectacular view of Langeberg Mountains")
        self.assertEqual(self.my_place.number_rooms, 2)
        self.assertEqual(self.my_place.number_bathrooms, 1)
        self.assertEqual(self.my_place.max_guest, 4)
        self.assertEqual(self.my_place.price_by_night, 100)
        self.assertEqual(self.my_place.latitude, 40.7128)
        self.assertEqual(self.my_place.longitude, -74.0060)
        self.assertEqual(self.my_place.amenity_ids, [self.amenity_instance.id])

    def test_id_string_place(self):
        """Check if Place `id` is a string
        """
        self.assertTrue(isinstance(self.my_place.id, str))

    def test_id_uniqueness_place(self):
        """Check if Place ids are unique
        """
        my_place2 = Place()

        self.assertNotEqual(self.my_place.id, my_place2.id)

    def test_time_format_place(self):
        """Check that the time format is correct
        """
        self.assertIsInstance(self.my_place.created_at, datetime)
        self.assertIsInstance(self.my_place.updated_at, datetime)

    def test_parts_string_representation_place(self):
        """Check if the string representation is correct
        """
        expected_str = "[Place] ({}) {}".format(self.my_place.id,
                                                self.my_place.__dict__)

        self.assertEqual(str(self.my_place), expected_str)

    def test_save_method_place(self):
        """Checks the save method
        """
        initial_updated_at = self.my_place.updated_at
        self.my_place.save()

        self.assertNotEqual(self.my_place.updated_at, initial_updated_at)

    def test_to_dict_method_place(self):
        """Check the return type of the to_dict method, and if
        the dictionary has all the expected attributes for `Place`
        """
        my_place_dict = self.my_place.to_dict()

        self.assertIsInstance(my_place_dict, dict)
        self.assertIn("__class__", my_place_dict)
        self.assertEqual(my_place_dict["__class__"], "Place")
        self.assertIn("id", my_place_dict)
        self.assertIn("created_at", my_place_dict)
        self.assertIn("updated_at", my_place_dict)
        self.assertIn("city_id", my_place_dict)
        self.assertIn("user_id", my_place_dict)
        self.assertIn("name", my_place_dict)
        self.assertIn("description", my_place_dict)
        self.assertIn("number_rooms", my_place_dict)
        self.assertIn("number_bathrooms", my_place_dict)
        self.assertIn("max_guest", my_place_dict)
        self.assertIn("price_by_night", my_place_dict)
        self.assertIn("latitude", my_place_dict)
        self.assertIn("longitude", my_place_dict)
        self.assertIn("amenity_ids", my_place_dict)

    def test_create_from_empty_dict_place(self):
        """Check the instance created from an empty dictionary
        """
        new_place = Place(**{})

        self.assertIsInstance(new_place, Place)
        self.assertTrue(hasattr(new_place, "id"))
        self.assertTrue(hasattr(new_place, "created_at"))
        self.assertTrue(hasattr(new_place, "updated_at"))
        self.assertTrue(hasattr(new_place, "city_id"))
        self.assertTrue(hasattr(new_place, "user_id"))
        self.assertTrue(hasattr(new_place, "name"))
        self.assertTrue(hasattr(new_place, "description"))
        self.assertTrue(hasattr(new_place, "number_rooms"))
        self.assertTrue(hasattr(new_place, "number_bathrooms"))
        self.assertTrue(hasattr(new_place, "max_guest"))
        self.assertTrue(hasattr(new_place, "price_by_night"))
        self.assertTrue(hasattr(new_place, "latitude"))
        self.assertTrue(hasattr(new_place, "longitude"))
        self.assertTrue(hasattr(new_place, "amenity_ids"))

        # Check the values
        self.assertIsNotNone(new_place.id)
        self.assertIsInstance(new_place.created_at, datetime)
        self.assertIsInstance(new_place.updated_at, datetime)

    def test_to_dict_datetime_format_place(self):
        """Check if the date format is correctly converted
        _from `datetime` to the expected string format
        """
        my_place_dict = self.my_place.to_dict()

        self.assertIsInstance(my_place_dict["created_at"], str)
        self.assertIsInstance(my_place_dict["updated_at"], str)
        self.assertEqual(
                datetime.strptime(my_place_dict["created_at"],
                                  "%Y-%m-%dT%H:%M:%S.%f"),
                self.my_place.created_at
        )
        self.assertEqual(
                datetime.strptime(my_place_dict["updated_at"],
                                  "%Y-%m-%dT%H:%M:%S.%f"),
                self.my_place.updated_at
        )

    def test_from_dict_method_place(self):
        """Check if previously converted instances are properly
        reloaded when a dictionary is provided as argument
        to BaseModel
        """
        place_json = self.my_place.to_dict()
        new_instance = Place(**place_json)

        self.assertEqual(self.my_place.id, new_instance.id)
        self.assertEqual(self.my_place.created_at, new_instance.created_at)
        self.assertEqual(self.my_place.updated_at, new_instance.updated_at)
        self.assertEqual(self.my_place.city_id, new_instance.city_id)
        self.assertEqual(self.my_place.user_id, new_instance.user_id)
        self.assertEqual(self.my_place.name, new_instance.name)
        self.assertEqual(self.my_place.description, new_instance.description)
        self.assertEqual(self.my_place.number_rooms, new_instance.number_rooms)
        self.assertEqual(self.my_place.number_bathrooms,
                         new_instance.number_bathrooms)


if __name__ == "__main__":
    unittest.main()
