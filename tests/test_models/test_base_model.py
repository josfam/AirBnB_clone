#!/usr/bin/python3

"""Test cases for the project's base class, `BaseModel`"""

import unittest
from datetime import datetime
from models.base_model import BaseModel as BM
from models import storage
import os


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel behaviour"""

    def setUp(self):
        self.b = BM()

    def tearDown(self):
        storage.all().clear()

    def test_a_new_base_must_have_a_unique_id(self):
        b = self.b
        b2 = BM()
        self.assertIsInstance(b.id, str)
        self.assertNotEqual(b.id, b2.id)

    def test_creation_time_must_be_earlier_than_update_time(self):
        b = self.b
        self.assertIsInstance(b.created_at, datetime)
        self.assertIsInstance(b.updated_at, datetime)
        self.assertLessEqual(b.created_at, b.updated_at)

    def test_save_changes_only_update_time(self):
        b = self.b
        first_creation = b.created_at
        first_update = b.updated_at
        b.save()
        # remove the generated json file
        if os.path.exists("file.json"):
            os.remove("file.json")
        self.assertEqual(first_creation, b.created_at)
        self.assertLessEqual(first_update, b.updated_at)

    def test_to_dict_adds_a_new__class__key(self):
        b = self.b
        old_attrs = b.__dict__.keys()
        self.assertFalse('__class__' in old_attrs)
        new_attrs = b.to_dict().keys()
        self.assertTrue('__class__' in new_attrs)

    def test_to_dict_makes_dates_into_iso_format(self):
        b = self.b
        created_iso = b.created_at.isoformat()
        updated_iso = b.updated_at.isoformat()
        b_dict = b.to_dict()
        self.assertEqual(b_dict['created_at'], created_iso)
        self.assertEqual(b_dict['updated_at'], updated_iso)

    def test_a_base_from_a_dict_is_a_base_instance(self):
        b = self.b
        b_dict = b.to_dict()
        b1 = BM(b_dict)
        self.assertIsInstance(b1, BM)

    def test_a_base_from_a_dict_has_no__class__key(self):
        b = self.b
        b_dict = b.to_dict()
        b1 = BM(b_dict)
        self.assertTrue('__class__' not in b1.__dict__.keys())

    def test_a_base_from_a_dict_turns_string_times_to_datetime_times(self):
        b = self.b
        self.assertIsInstance(b.created_at, datetime)
        self.assertIsInstance(b.updated_at, datetime)
        b_dict = b.to_dict()
        self.assertIsInstance(b_dict['created_at'], str)
        self.assertIsInstance(b_dict['updated_at'], str)
        b1 = BM(b_dict)
        self.assertIsInstance(b1.created_at, datetime)
        self.assertIsInstance(b1.updated_at, datetime)
