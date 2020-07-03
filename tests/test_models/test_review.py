#!/usr/bin/python3

"""tests for Review Model"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Unittest"""

    def test_instance_Review(self):
        """ Test to check if sub class of Base Model """
        obj = Review()
        self.assertIsInstance(obj, BaseModel)

    def test_attributes_Review(self):
        """ Test to check the expected attributes """
        obj = Review()
        self.assertIsInstance(obj.place_id, str)
        self.assertIsInstance(obj.user_id, str)
        self.assertIsInstance(obj.text, str)
