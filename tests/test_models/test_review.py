#!/usr/bin/python3

"""Test cases for the project's `Review` class, that represents a review of a
person's experience in the place that they lived in
"""

import unittest
from models import storage
from models.review import Review


class TestStorage(unittest.TestCase):
    """Test cases for `Review` behavior"""

    def setUp(self):
        """Routine to be performed before every test"""
        self.r = Review()

    def tearDown(self):
        """Routine to be performed after every test"""
        storage.all().clear()

    def test_Review_is_a_subclass_of_BaseModel(self):
        """The Review class must inherit from the BaseModel class"""
        parent = Review.__base__.__name__
        self.assertEqual(parent, 'BaseModel')

    def test_a_new_review_has_correct_non_BaseModel_default_values(self):
        """Non - inherited attributes must have correct default values"""
        r = self.r
        defaults = {
            'place_id': "",
            'user_id': "",
            'text': "",
        }
        r_dict = r.__dict__
        for k, v in r_dict.items():
            if k in defaults:
                self.assertEqual(v, defaults[k])

    def test_new_reviews_have_unique_ids(self):
        """New Reviews, like new BaseModels should have unique ids"""
        r = self.r
        r2 = Review()
        self.assertNotEqual(r.id, r2.id)

    def test_to_dict_stores_Review_as_the__class__value(self):
        """A review's __dict__'s `__class__` attribute should store
        `Review` as the class name
        """
        r = self.r
        r_dict = r.to_dict()
        self.assertEqual(r_dict['__class__'], 'Review')

    def test_a_review_instance_is_printed_correctly(self):
        """__str__ should return the correct format for a Review"""
        r = self.r
        expected_format = '[{}] ({}) {}'.format('Review', r.id, r.__dict__)
        self.assertEqual(r.__str__(), expected_format)
