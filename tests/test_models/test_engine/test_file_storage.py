#!/usr/bin/python3

"""tests!"""
import unittest
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """Unittest"""

    def test_create_instance(self):
        """ Test create instance"""
        store = FileStorage()
        self.assertIsInstance(store, FileStorage)

    def test_attributes_file_storage(self):
        """ Test if spected attributes exist"""
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(type(FileStorage._FileStorage__file_path) is str)

        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertTrue(type(FileStorage._FileStorage__objects) is dict)

    def test_methods_file_storage(self):
        """ Test if spected methods exist"""
        self.assertTrue(hasattr(FileStorage, "all"))
        self.assertTrue(hasattr(FileStorage, "new"))
        self.assertTrue(hasattr(FileStorage, "save"))
        self.assertTrue(hasattr(FileStorage, "reload"))

    def test_all(self):
        """Test for all method"""
        all = storage.all()
        self.assertIsInstance(all, dict)

    def test_new(self):
        """ Test new method"""
        obj = BaseModel()
        storage.new(obj)
        self.assertTrue(("BaseModel" + "." + str(obj.id))
                        in storage.all())
        self.assertTrue(
            storage.all()[("BaseModel" + "." + str(obj.id))] == obj)

    def test_save_reload_file_storage(self):
        """ Check save / reload method"""
        obj = BaseModel()
        obj.name = "Manuel-12345"
        obj.age = 26

        storage.save()
        FileStorage._FileStorage__objects = {}
        storage.reload()

        self.assertTrue(
            storage.all()["BaseModel" + "." +
                          str(obj.id)].name == "Manuel-12345")
        self.assertTrue(
            storage.all()["BaseModel" + "." + str(obj.id)].age == 26)
