#!/usr/bin/python3

"""tests for Amenity Class"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Unittest"""

    def test_instance_Amenity(self):
        """ Test to check if sub class of Base Model """
        obj = Amenity()
        self.assertIsInstance(obj, BaseModel)

    def test_attributes_Amenity(self):
        """ Test to check the expected attributes """
        obj = Amenity()
        self.assertIsInstance(obj.name, str)
