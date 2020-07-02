#!/usr/bin/python3
""" [Test console] """

from unittest.mock import patch
from io import StringIO
import unittest
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Unittest"""

    def test_calls(self):
        """ call the commands"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
        self.assertEqual(f.getvalue(
        ), "Prints the string representation of an\n\
        instance based on the class name and id\n")

        """ call the commands"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")

    def test_empty_line(self):
        """ empty line + ENTER shouldn’t execute anything """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
        self.assertTrue(f.getvalue() == "")
