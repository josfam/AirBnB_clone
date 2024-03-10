#!/usr/bin/python3

"""Test cases for the project's `User` class, that represents a user of the
application
"""

import unittest
from models import storage
from models.user import User


class TestStorage(unittest.TestCase):
    """Test cases for `User` behavior"""

    def tearDown(self):
        """Routine to be performed after every test"""
        storage.all().clear()

    def test_User_is_a_subclass_of_BaseModel(self):
        """The User class must inherit from the BaseModel class"""
        parent = User.__base__.__name__
        self.assertEqual(parent, 'BaseModel')

    def test_a_new_user_has_empty_non_Base_attributes_by_default(self):
        """Non - inherited attributes must be empty"""
        u = User()
        attrs = {'email', 'password', 'first_name', 'last_name'}
        u_dict = u.__dict__
        for k, v in u_dict.items():
            if k in attrs:
                self.assertEqual(v, '')

    def test_new_users_have_unique_ids(self):
        """New Users, like new BaseModels should have unique ids"""
        u = User()
        u2 = User()
        self.assertNotEqual(u.id, u2.id)

    def test_to_dict_stores_User_as_the__class__value(self):
        """A user's __dict__ __class__ attribute should store
        `User` as the class name
        """
        u = User()
        u_dict = u.to_dict()
        self.assertEqual(u_dict['__class__'], 'User')

    def test_a_user_instance_is_printed_correctly(self):
        """__str__ should return the correct format for a User"""
        u = User()
        expected_format = '[{}] ({}) {}'.format('User', u.id, u.__dict__)
        self.assertEqual(u.__str__(), expected_format)
