#!/usr/bin/python3

"""tests!"""
import unittest
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """Unittest"""

    def test_id(self):
        """Test for id attribute"""
        id_list = []
        for i in range(100):
            obj = BaseModel()
            self.assertTrue(obj.id not in id_list)
            id_list.append(obj.id)

        self.assertEqual(str(type(obj.id)), "<class 'str'>")

    def test_create_at(self):
        """Test for create_at attribute"""
        obj = BaseModel()
        self.assertEqual(str(type(obj.created_at)),
                         "<class 'datetime.datetime'>")

    def test_update_at(self):
        """Test for updated_at attribute"""
        obj = BaseModel()
        self.assertEqual(str(type(obj.updated_at)),
                         "<class 'datetime.datetime'>")
        first_value = obj.updated_at
        obj.save()
        self.assertFalse(first_value == obj.updated_at)

    def test_str(self):
        """Test for str method"""
        obj = BaseModel()
        self.assertEqual(obj.__str__(),
                         "[{}] ({}) {}".format(obj.__class__.__name__,
                                               obj.id, obj.__dict__))

    def test_to_dict(self):
        """Test for dict method"""
        obj = BaseModel()
        my_dict = obj.to_dict()
        self.assertTrue("__class__" in my_dict)
        self.assertTrue(str(type(my_dict["created_at"])) == "<class 'str'>")
        self.assertTrue(str(type(my_dict["updated_at"])) == "<class 'str'>")
        obj.name = "Manuel"
        obj.age = 26
        my_dict = obj.to_dict()
        self.assertTrue(str(type(my_dict["age"])) == "<class 'int'>")
        self.assertEqual(my_dict["age"], 26)
        self.assertTrue(str(type(my_dict["name"])) == "<class 'str'>")
        self.assertEqual(my_dict["name"], "Manuel")
