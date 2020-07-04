#!/usr/bin/python3
""" [Test console] """

from unittest.mock import patch
from io import StringIO
import unittest
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """Unittest"""
    classes = ("BaseModel", "User", "Place",
               "City", "Amenity", "Review", "State")

    def test_help(self):
        """ Check help command"""
        m1 = "\nDocumented commands (type help <topic>):\n"
        m2 = "========================================\n"
        m3 = "EOF  all  count  create  destroy  help  quit  show  update\n\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        self.assertEqual(f.getvalue(), m1 + m2 + m3)

    def test_quit(self):
        """ Test quit / EOF functionality """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
        self.assertTrue(f.getvalue() == "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
        self.assertTrue(f.getvalue() == "")

    def test_empty_line(self):
        """ empty line + ENTER shouldn’t execute anything """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
        self.assertTrue(f.getvalue() == "")

    def test_create(self):
        """ Test create functionality """
        for elem in TestConsole.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create " + elem)
            self.assertIn(elem + "." +
                          str(f.getvalue()[:-1]), storage.all())

    def test_show(self):
        """ Test show functionality """
        for elem in TestConsole.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                obj = globals()[elem]()
                HBNBCommand().onecmd("show " + elem + " " + str(obj.id))
            self.assertEqual(obj.__str__(), f.getvalue()[:-1])

    def test_show_dot_format(self):
        """ Test show functionality with dot format """
        for elem in TestConsole.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                obj = globals()[elem]()
                HBNBCommand().onecmd(elem + "." + "show(" + str(obj.id) + ")")
            self.assertEqual(obj.__str__(), f.getvalue()[:-1])

    def test_destroy(self):
        """ Test destroy functionality """
        for elem in TestConsole.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                obj = globals()[elem]()
                HBNBCommand().onecmd("destroy " + elem + " " + str(obj.id))
            self.assertTrue(f.getvalue() == "")
            self.assertNotIn(elem + "." + str(obj.id), storage.all())

    def test_destroy_dot_format(self):
        """ Test destroy functionality with dot format """
        for elem in TestConsole.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                obj = globals()[elem]()
                HBNBCommand().onecmd(elem + "." + "destroy(" + str(obj.id) + ")")
            self.assertTrue(f.getvalue() == "")
            self.assertNotIn(elem + "." + str(obj.id), storage.all())

    def test_all(self):
        """ Test all functionality """
        for elem in TestConsole.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("all " + elem)
            some_elem = ""
            for value in storage.all().values():
                if value.__class__.__name__ == elem:
                    some_elem += value.__str__() + "\n"
            self.assertEqual(f.getvalue(), some_elem)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
        all_elem = ""
        for elm in storage.all().values():
            all_elem += elm.__str__() + "\n"
        self.assertEqual(f.getvalue(), all_elem)

    def test_all_dot_format(self):
        """ Test all functionality with dot format """
        for elem in TestConsole.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(elem + "." + "all()")
            some_elem = ""
            for value in storage.all().values():
                if value.__class__.__name__ == elem:
                    some_elem += value.__str__() + "\n"
            self.assertEqual(f.getvalue(), some_elem)

    def test_update(self):
        """ Test update functionality """
        for elem in TestConsole.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                obj = globals()[elem]()
                HBNBCommand().onecmd("update " + elem + " " + str(obj.id) + " Name" + " Manuel")
            self.assertTrue(f.getvalue() == "")
            self.assertEqual(obj.Name, "Manuel")

    def test_count_dot_format(self):
        """ Test count functionality with dot format """
        FileStorage._FileStorage__objects = {}

        for elem in TestConsole.classes:
            obj = globals()[elem]()
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(elem + "." + "count()")
            self.assertEqual(f.getvalue()[:-1], "1")

            obj = globals()[elem]()
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(elem + "." + "count()")
            self.assertEqual(f.getvalue()[:-1], "2")

        for elem in TestConsole.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("count " + elem)
            self.assertEqual(f.getvalue()[:-1], "2")

            obj = globals()[elem]()
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("count " + elem)
            self.assertEqual(f.getvalue()[:-1], "3")
