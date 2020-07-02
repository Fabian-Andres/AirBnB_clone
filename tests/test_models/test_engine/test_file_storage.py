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
        """ Test new method"""
        obj = BaseModel()
        storage.new(obj)
        self.assertTrue(("BaseModel" + "." + str(obj.id)) in storage.all())
        self.assertTrue(
            storage.all()[("BaseModel" + "." + str(obj.id))] == obj)

    def test_data_file_storage(self):
        """ Check that the Class / instance has the spected attributes """
        # print(FileStorage.__dict__)
        self.assertTrue(FileStorage._FileStorage__file_path is not None)
        self.assertTrue(type(FileStorage._FileStorage__file_path) is str)

        self.assertTrue(FileStorage._FileStorage__objects is not None)
        self.assertTrue(type(FileStorage._FileStorage__objects) is dict)

    def test_save_file_storage(self):
        """ Check save method"""
        self.assertTrue("save" in dir(storage))

    def test_reload_file_storage(self):
        """ Check reload method"""
        self.assertTrue("reload" in dir(storage))
