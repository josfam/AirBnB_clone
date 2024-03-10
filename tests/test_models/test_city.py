#!/usr/bin/python3

"""Test cases for the project's `City` class, that represents a city
(in the geographical sense), that a particular location is in.
"""

import unittest
from models import storage
from models.city import City


class TestStorage(unittest.TestCase):
    """Test cases for `City` behavior"""

    def setUp(self):
        """Routine to be performed before every test"""
        self.c = City()

    def tearDown(self):
        """Routine to be performed after every test"""
        storage.all().clear()

    def test_City_is_a_subclass_of_BaseModel(self):
        """The City class must inherit from the BaseModel class"""
        parent = City.__base__.__name__
        self.assertEqual(parent, 'BaseModel')

    def test_a_new_city_has_empty_non_Base_attributes_by_default(self):
        """Non - inherited attributes must be empty"""
        c = self.c
        attrs = {'name', 'state_id'}
        c_dict = c.__dict__
        for k, v in c_dict.items():
            if k in attrs:
                self.assertEqual(v, '')

    def test_new_cities_have_unique_ids(self):
        """New Cities, like new BaseModels should have unique ids"""
        c = self.c
        c2 = City()
        self.assertNotEqual(c.id, c2.id)

    def test_to_dict_stores_City_as_the__class__value(self):
        """A city's __dict__'s `__class__` attribute should store
        `City` as the class name
        """
        c = self.c
        c_dict = c.to_dict()
        self.assertEqual(c_dict['__class__'], 'City')

    def test_a_state_instance_is_printed_correctly(self):
        """__str__ should return the correct format for a City"""
        c = self.c
        expected_format = '[{}] ({}) {}'.format('City', c.id, c.__dict__)
        self.assertEqual(c.__str__(), expected_format)
