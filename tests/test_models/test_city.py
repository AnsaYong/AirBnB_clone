#
#/usr/bin/python3
"""
This module provides test cases for the City
class
"""
import unittest
from datetime import datetime
from models.city import City  # Import the City class


class TestCity(unittest.TestCase):
    """Provides test cases/methods to test the
    functionality of the City class
    """
    def test_city_instance_creation(self):
        """Check if a City instance is created properly
        """
        city = City()

        self.assertIsInstance(city, City)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")

    def test_city_attributes(self):
        """Test setting and getting attributes specific to City
        """
        city = City()

        city.name = "New York"
        city.state_id = city.id
        self.assertEqual(city.name, "New York")
        self.assertEqual(city.state_id, city.id)

    def test_city_inherits_base_model_functions(self):
        """Test if City inherits functions from BaseModel
        """
        city = City()

        # Check if City has inherited the to_dict method
        self.assertTrue(hasattr(city, "to_dict"))
        self.assertTrue(callable(getattr(city, "to_dict", None)))

        # Check if City has inherited the save method
        self.assertTrue(hasattr(city, "save"))
        self.assertTrue(callable(getattr(city, "save", None)))

        # Check if City has inherited the __str__ method
        self.assertTrue(hasattr(city, "__str__"))
        self.assertTrue(callable(getattr(city, "__str__", None)))

    def test_city_save_updates_timestamps(self):
        """Test if calling save method updates timestamps
        """
        city = City()
        initial_updated_at = city.updated_at
        city.save()

        self.assertNotEqual(city.updated_at, initial_updated_at)


if __name__ == "__main__":
    unittest.main()
