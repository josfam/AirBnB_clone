#!/usr/bin/python3

"""Test cases for the project's `Place` class, that represents
a place that a user of the application can book and, therefore, live in.
"""

import unittest
from models import storage
from models.place import Place


class TestStorage(unittest.TestCase):
    """Test cases for `Place` behavior"""

    def setUp(self):
        """Routine to be performed before every test"""
        self.p = Place()

    def tearDown(self):
        """Routine to be performed after every test"""
        storage.all().clear()

    def test_Place_is_a_subclass_of_BaseModel(self):
        """The Place class must inherit from the BaseModel class"""
        parent = Place.__base__.__name__
        self.assertEqual(parent, 'BaseModel')

    def test_a_new_place_has_correct_non_BaseModel_default_values(self):
        """Non - inherited attributes must have correct default values"""
        p = self.p
        defaults = {
            'city_id': "",
            'user_id': "",
            'name': "",
            'description': "",
            'number_rooms': 0,
            'number_bathrooms': 0,
            'max_guest': 0,
            'price_by_night': 0,
            'latitude': 0.0,
            'longitude': 0.0,
            'amenity_ids': [],
        }
        p_dict = p.__dict__
        for k, v in p_dict.items():
            if k in defaults:
                self.assertEqual(v, defaults[k])

    def test_new_places_have_unique_ids(self):
        """New Places, like new BaseModels should have unique ids"""
        p = self.p
        p2 = Place()
        self.assertNotEqual(p.id, p2.id)

    def test_to_dict_stores_Place_as_the__class__value(self):
        """A place's __dict__'s `__class__` attribute should store
        `Place` as the class name
        """
        p = self.p
        p_dict = p.to_dict()
        self.assertEqual(p_dict['__class__'], 'Place')

    def test_a_state_instance_is_printed_correctly(self):
        """__str__ should return the correct format for a Place"""
        p = self.p
        expected_format = '[{}] ({}) {}'.format('Place', p.id, p.__dict__)
        self.assertEqual(p.__str__(), expected_format)
