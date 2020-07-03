#!/usr/bin/python3

"""tests for State Class"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Unittest"""

    def test_instance_State(self):
        """ Test to check if sub class of Base Model """
        obj = State()
        self.assertIsInstance(obj, BaseModel)

    def test_attributes_State(self):
        """ Test to check the expected attributes """
        obj = State()
        self.assertIsInstance(obj.name, str)
