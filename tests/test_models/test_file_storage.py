#!/usr/bin/python3

"""Test cases for the project's file storage class, `FileStorage`"""

import unittest
from models import storage
from models.base_model import BaseModel as BM


class TestStorage(unittest.TestCase):
    """Test cases for TestStorage behavior"""

    def tearDown(self):
        """Routine to be performed after every test"""
        storage.all().clear()

    def test_storage_has_no_objects_if_no_objects_have_been_created(self):
        """Storage must be empty if nothing has been stored yet"""
        self.assertTrue(len(storage.all()) == 0)

    def test_new_base_objects_are_stored_upon_creation(self):
        """Newly created Base objects are instantly stored"""
        self.assertTrue(len(storage.all()) == 0)
        b = BM()
        self.assertTrue(len(storage.all()) == 1)
        b1 = BM()
        b2 = BM()
        self.assertTrue(len(storage.all()) == 3)

    def test_objects_are_stored_with_the_correct_format(self):
        """Base objects are correctly represented in the storage dictionary"""
        b = BM()
        id = b.id
        name = 'BaseModel'
        obj_dict = storage.all()
        for key, value in obj_dict.items():
            self.assertEqual(key, '{}.{}'.format(name, id))
            self.assertIs(value, b)
