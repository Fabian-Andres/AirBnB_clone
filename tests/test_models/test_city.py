#!/usr/bin/python3

"""tests for City Class"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Unittest"""

    def test_instance_City(self):
        """ Test to check if sub class of Base Model """
        obj = City()
        self.assertIsInstance(obj, BaseModel)

    def test_attributes_City(self):
        """ Test to check the expected attributes """
        obj = City()
        self.assertIsInstance(obj.name, str)
        self.assertIsInstance(obj.state_id, str)
