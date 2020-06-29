#!/usr/bin/python3
""" [FileStorage class] """
import json


class FileStorage:

    __file_path = "file.json"
    __objects = {}
    c = ("BaseModel", "User")

    def all(self):
        return type(self).__objects

    def new(self, obj):
        type(self).__objects[obj.__class__.__name__ + "." +
                             str(obj.id)] = obj

    def save(self):
        with open(type(self).__file_path, 'w', encoding="utf-8") as f:
            dict_obj = {}
            for key, value in type(self).__objects.items():
                dict_obj[key] = value.to_dict()
            json.dump(dict_obj, f)

    def reload(self):
        from models.base_model import BaseModel
        from models.user import User
        try:
            with open(type(self).__file_path, 'r', encoding="utf-8") as f:
                dict_obj = json.load(f)
                for key, value in dict_obj.items():
                    obj = eval(value['__class__'])(**value)
                    type(self).__objects[key] = obj
        except ValueError:
            pass

    def find(self, id):
        for key, value in type(self).__objects.items():
            if id == key.split(".")[1]:
                return value
        return None

    def delete(self, id):
        for key in type(self).__objects.keys():
            if id == key.split(".")[1]:
                break
        del type(self).__objects[key]

    def print_all(self, type_class=None):
        for key, value in type(self).__objects.items():
            if type_class == key.split(".")[0]:
                print(value)
            elif type_class == None:
                print(value)
