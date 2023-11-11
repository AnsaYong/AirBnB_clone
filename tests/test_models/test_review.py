#!/usr/bin/python3
"""
This module provides test cases for the `Review` class.
"""
import unittest
from datetime import datetime
from models.review import Review
from models.place import Place
from models.user import User


class TestReview(unittest.TestCase):
    """Provides test methods for the `Review` class
    """
    def setUp(self):
        """Create an instance of class `Review` to use
        for subsequent test cases
        """
        # Create instances of Place and User for IDs
        place_instance = Place()
        user_instance = User()

        # Set IDs for Review attributes
        self.my_review = Review()
        self.my_review.place_id = place_instance.id
        self.my_review.user_id = user_instance.id
        self.my_review.text = "A wonderful stay with great amenities!"

    def test_instance_creation_review(self):
        """Check if a Review instance is created with
        properties inherited from `BaseModel`
        """
        self.assertIsInstance(self.my_review, Review)

    def test_inheritance_review(self):
        """Check if attributes were correctly inherited
        from `BaseModel`
        """
        self.assertTrue(hasattr(self.my_review, "id"))
        self.assertTrue(hasattr(self.my_review, "created_at"))
        self.assertTrue(hasattr(self.my_review, "updated_at"))

    def test_attributes_review(self):
        """Check attributes of `Review`
        """
        self.assertEqual(self.my_review.place_id, self.my_review.place_id)
        self.assertEqual(self.my_review.user_id, self.my_review.user_id)
        self.assertEqual(self.my_review.text,
                         "A wonderful stay with great amenities!")

    def test_id_string_review(self):
        """Check if Review `id` is a string
        """
        self.assertTrue(isinstance(self.my_review.id, str))

    def test_id_uniqueness_review(self):
        """Check if Review ids are unique
        """
        my_review2 = Review()

        self.assertNotEqual(self.my_review.id, my_review2.id)

    def test_time_format_review(self):
        """Check that the time format is correct
        """
        self.assertIsInstance(self.my_review.created_at, datetime)
        self.assertIsInstance(self.my_review.updated_at, datetime)

    def test_parts_string_representation_review(self):
        """Check if the string representation is correct
        """
        expected_str = "[Review] ({}) {}".format(self.my_review.id,
                                                 self.my_review.__dict__)

        self.assertEqual(str(self.my_review), expected_str)

    def test_save_method_review(self):
        """Checks the save method
        """
        initial_updated_at = self.my_review.updated_at
        self.my_review.save()

        self.assertNotEqual(self.my_review.updated_at, initial_updated_at)

    def test_to_dict_method_review(self):
        """Check the return type of the to_dict method, and if
        the dictionary has all the expected attributes for `Review`
        """
        my_review_dict = self.my_review.to_dict()

        self.assertIsInstance(my_review_dict, dict)
        self.assertIn("__class__", my_review_dict)
        self.assertEqual(my_review_dict["__class__"], "Review")
        self.assertIn("id", my_review_dict)
        self.assertIn("created_at", my_review_dict)
        self.assertIn("updated_at", my_review_dict)
        self.assertIn("place_id", my_review_dict)
        self.assertIn("user_id", my_review_dict)
        self.assertIn("text", my_review_dict)

    def test_create_from_empty_dict_review(self):
        """Check the instance created from an empty dictionary
        """
        new_review = Review(**{})

        self.assertIsInstance(new_review, Review)
        self.assertTrue(hasattr(new_review, "id"))
        self.assertTrue(hasattr(new_review, "created_at"))
        self.assertTrue(hasattr(new_review, "updated_at"))
        self.assertTrue(hasattr(new_review, "place_id"))
        self.assertTrue(hasattr(new_review, "user_id"))
        self.assertTrue(hasattr(new_review, "text"))

        # Check the values
        self.assertIsNotNone(new_review.id)
        self.assertIsInstance(new_review.created_at, datetime)
        self.assertIsInstance(new_review.updated_at, datetime)

    def test_to_dict_datetime_format_review(self):
        """Check if the date format is correctly converted
        _from `datetime` to the expected string format
        """
        my_review_dict = self.my_review.to_dict()

        self.assertIsInstance(my_review_dict["created_at"], str)
        self.assertIsInstance(my_review_dict["updated_at"], str)
        self.assertEqual(
                datetime.strptime(my_review_dict["created_at"],
                                  "%Y-%m-%dT%H:%M:%S.%f"),
                self.my_review.created_at
        )
        self.assertEqual(
                datetime.strptime(my_review_dict["updated_at"],
                                  "%Y-%m-%dT%H:%M:%S.%f"),
                self.my_review.updated_at
        )

    def test_from_dict_method_review(self):
        """Check if previously converted instances are properly
        reloaded when a dictionary is provided as an argument
        to BaseModel
        """
        review_json = self.my_review.to_dict()
        new_instance = Review(**review_json)

        self.assertEqual(self.my_review.id, new_instance.id)
        self.assertEqual(self.my_review.created_at, new_instance.created_at)
        self.assertEqual(self.my_review.updated_at, new_instance.updated_at)
        self.assertEqual(self.my_review.place_id, new_instance.place_id)
        self.assertEqual(self.my_review.user_id, new_instance.user_id)
        self.assertEqual(self.my_review.text, new_instance.text)


if __name__ == "__main__":
    unittest.main()
