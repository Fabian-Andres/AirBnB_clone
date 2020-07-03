#!/usr/bin/python3

"""tests for User Class"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Unittest"""

    def test_instance_User(self):
        """ Test to check if sub class of Base Model """
        obj = User()
        self.assertIsInstance(obj, BaseModel)

    def test_attributes_User(self):
        """ Test to check the expected attributes """
        obj = User()
        self.assertIsInstance(obj.email, str)
        self.assertIsInstance(obj.password, str)
        self.assertIsInstance(obj.first_name, str)
        self.assertIsInstance(obj.last_name, str)
