#!/usr/bin/python3

"""Test cases for the project's base class, `BaseModel`"""

import unittest
from datetime import datetime
from models.base_model import BaseModel as BM


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel behaviour"""

    def test_a_new_base_must_have_a_unique_id(self):
        b = BM()
        b2 = BM()
        self.assertIsInstance(b.id, str)
        self.assertNotEqual(b.id, b2.id)

    def test_creation_time_must_be_earlier_than_update_time(self):
        b = BM()
        self.assertIsInstance(b.created_at, datetime)
        self.assertIsInstance(b.updated_at, datetime)
        self.assertLessEqual(b.created_at, b.updated_at)

    def test_save_changes_only_update_time(self):
        b = BM()
        first_creation = b.created_at
        first_update = b.updated_at
        b.save()
        self.assertEqual(first_creation, b.created_at)
        self.assertLessEqual(first_update, b.updated_at)

    def test_to_dict_adds_a_new__class__key(self):
        b = BM()
        old_attrs = b.__dict__.keys()
        self.assertFalse('__class__' in old_attrs)
        new_attrs = b.to_dict().keys()
        self.assertTrue('__class__' in new_attrs)

    def test_to_dict_makes_dates_into_iso_format(self):
        b = BM()
        created_iso = b.created_at.isoformat()
        updated_iso = b.updated_at.isoformat()
        b_dict = b.to_dict()
        self.assertEqual(b_dict['created_at'], created_iso)
        self.assertEqual(b_dict['updated_at'], updated_iso)
