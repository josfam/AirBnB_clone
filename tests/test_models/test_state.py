#!/usr/bin/python3

"""Test cases for the project's `State` class, that represents a state
(in the geographical sense), that a particular location is in.
"""

import unittest
from models import storage
from models.state import State


class TestStorage(unittest.TestCase):
    """Test cases for `State` behavior"""

    def setUp(self):
        """Routine to be performed before every test"""
        self.s = State()

    def tearDown(self):
        """Routine to be performed after every test"""
        storage.all().clear()

    def test_State_is_a_subclass_of_BaseModel(self):
        """The State class must inherit from the BaseModel class"""
        parent = State.__base__.__name__
        self.assertEqual(parent, 'BaseModel')

    def test_a_new_state_has_empty_non_Base_attributes_by_default(self):
        """Non - inherited attributes must be empty"""
        s = self.s
        attrs = {'name'}
        s_dict = s.__dict__
        for k, v in s_dict.items():
            if k in attrs:
                self.assertEqual(v, '')

    def test_new_states_have_unique_ids(self):
        """New States, like new BaseModels should have unique ids"""
        s = self.s
        s2 = State()
        self.assertNotEqual(s.id, s2.id)

    def test_to_dict_stores_State_as_the__class__value(self):
        """A state's __dict__'s `__class__` attribute should store
        `State` as the class name
        """
        s = self.s
        s_dict = s.to_dict()
        self.assertEqual(s_dict['__class__'], 'State')

    def test_a_user_instance_is_printed_correctly(self):
        """__str__ should return the correct format for a State"""
        s = self.s
        expected_format = '[{}] ({}) {}'.format('State', s.id, s.__dict__)
        self.assertEqual(s.__str__(), expected_format)
