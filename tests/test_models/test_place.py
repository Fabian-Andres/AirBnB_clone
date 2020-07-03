#!/usr/bin/python3

"""tests for Place Model"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Unittest"""

    def test_instance_Place(self):
        """ Test to check if sub class of Base Model """
        obj = Place()
        self.assertIsInstance(obj, BaseModel)

    def test_attributes_Place(self):
        """ Test to check the expected attributes """
        obj = Place()
        self.assertIsInstance(obj.city_id, str)
        self.assertIsInstance(obj.user_id, str)
        self.assertIsInstance(obj.name, str)
        self.assertIsInstance(obj.description, str)
        self.assertIsInstance(obj.number_rooms, int)
        self.assertIsInstance(obj.number_bathrooms, int)
        self.assertIsInstance(obj.max_guest, int)
        self.assertIsInstance(obj.price_by_night, int)
        self.assertIsInstance(obj.latitude, float)
        self.assertIsInstance(obj.longitude, float)
        self.assertIsInstance(obj.amenity_ids, list)
