#!/usr/bin/python3

"""Test cases for the project's `Amenity` class, that represents a state
(in the geographical sense), that a particular location is in.
"""

import unittest
from models import storage
from models.amenity import Amenity


class TestStorage(unittest.TestCase):
    """Test cases for `Amenity` behavior"""

    def setUp(self):
        """Routine to be performed before every test"""
        self.a = Amenity()

    def tearDown(self):
        """Routine to be performed after every test"""
        storage.all().clear()

    def test_Amenity_is_a_subclass_of_BaseModel(self):
        """The Amenity class must inherit from the BaseModel class"""
        parent = Amenity.__base__.__name__
        self.assertEqual(parent, 'BaseModel')

    def test_a_new_state_has_empty_non_Base_attributes_by_default(self):
        """Non - inherited attributes must be empty"""
        a = self.a
        attrs = {'name'}
        a_dict = a.__dict__
        for k, v in a_dict.items():
            if k in attrs:
                self.assertEqual(v, '')

    def test_new_states_have_unique_ids(self):
        """New Amenities, like new BaseModels should have unique ids"""
        a = self.a
        a2 = Amenity()
        self.assertNotEqual(a.id, a2.id)

    def test_to_dict_stores_Amenity_as_the__class__value(self):
        """An amenity's __dict__'s `__class__` attribute should store
        `Amenity` as the class name
        """
        a = self.a
        a_dict = a.to_dict()
        self.assertEqual(a_dict['__class__'], 'Amenity')

    def test_a_state_instance_is_printed_correctly(self):
        """__str__ should return the correct format for a Amenity"""
        a = self.a
        expected_format = '[{}] ({}) {}'.format('Amenity', a.id, a.__dict__)
        self.assertEqual(a.__str__(), expected_format)
