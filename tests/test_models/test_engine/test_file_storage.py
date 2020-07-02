#!/usr/bin/python3

"""tests!"""
import unittest
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """Unittest"""

    def test_all(self):
        """Test for all method"""
        all = storage.all()
        self.assertEqual(str(type(all)), "<class 'dict'>")

    def test_new(self):
        obj = BaseModel()
        storage.new(obj)
        self.assertTrue(("BaseModel" + "." + str(obj.id)) in storage.all())
        self.assertTrue(
            storage.all()[("BaseModel" + "." + str(obj.id))] == obj)
