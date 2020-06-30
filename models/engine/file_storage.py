#!/usr/bin/python3
""" [FileStorage class] """
import json


class FileStorage:
    """[FileStorage]
        Save the information for the aplication in a JSON file
    """

    __file_path = "file.json"
    __objects = {}
    c = ("BaseModel", "User")

    def all(self):
        """returns the dictionary __objects"""
        return type(self).__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        type(self).__objects[obj.__class__.__name__ + "." +
                             str(obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(type(self).__file_path, 'w', encoding="utf-8") as f:
            dict_obj = {}
            for key, value in type(self).__objects.items():
                dict_obj[key] = value.to_dict()
            json.dump(dict_obj, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.amenity import Amenity
        from models.state import State
        from models.review import Review
        try:
            with open(type(self).__file_path, 'r', encoding="utf-8") as f:
                dict_obj = json.load(f)
                for key, value in dict_obj.items():
                    obj = eval(value['__class__'])(**value)
                    type(self).__objects[key] = obj
        except:
            pass

    def find(self, id, class_name):
        """aux function to find a object"""
        for key, value in type(self).__objects.items():
            if id == key.split(".")[1] and class_name == key.split(".")[0]:
                return value
        return None

    def delete(self, id):
        """aux function to delete an object"""
        for key in type(self).__objects.keys():
            if id == key.split(".")[1]:
                break
        del type(self).__objects[key]

    def print_all(self, type_class=None):
        """aux function to print all objects"""
        for key, value in type(self).__objects.items():
            if type_class == key.split(".")[0]:
                print(value)
            elif type_class is None:
                print(value)
