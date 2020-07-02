#!/usr/bin/python3

"""tests for City Class"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Unittest"""

    def test_id_city(self):
        """Test for id attribute"""
        obj = City()
        self.assertEqual(str(type(obj.id)), "<class 'str'>")

    def test_create_at_city(self):
        """Test for create_at attribute"""
        obj = City()
        self.assertEqual(str(type(obj.created_at)),
                         "<class 'datetime.datetime'>")

    def test_update_at_city(self):
        """Test for updated_at attribute"""
        obj = City()
        self.assertEqual(str(type(obj.updated_at)),
                         "<class 'datetime.datetime'>")
        first_value = obj.updated_at
        obj.save()
        self.assertFalse(first_value == obj.updated_at)

    def test_str_city(self):
        """Test for str method"""
        obj = City()
        self.assertEqual(obj.__str__(),
                         "[{}] ({}) {}".format(obj.__class__.__name__,
                                               obj.id, obj.__dict__))

    def test_to_dict_city(self):
        """Test for dict method"""
        obj = City()
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

    def test_dict_to_obj_city(self):
        """Test for create an instance with a
        dictionary representation"""
        obj = City()
        obj.name = "Manuel"
        obj.awesome = 100
        my_dict = obj.to_dict()

        new_obj = City(**my_dict)
        self.assertFalse(obj is new_obj)
        self.assertEqual(obj.id, new_obj.id)
        self.assertEqual(obj.updated_at, new_obj.updated_at)
        self.assertEqual(obj.name, new_obj.name)
        self.assertEqual(obj.created_at, new_obj.created_at)
        self.assertEqual(obj.awesome, new_obj.awesome)
        self.assertEqual(type(obj), type(new_obj))
