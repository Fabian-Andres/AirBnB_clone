#!/usr/bin/python3
""" [FileStorage class] """
import json


class FileStorage:

    __file_path = "file.json"
    __objects = {}

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
            print(FileStorage.__objects)

    def reload(self):
        from models.base_model import BaseModel
        try:
            with open(type(self).__file_path, 'r', encoding="utf-8") as f:
                dict_obj = json.load(f)
                for key, value in dict_obj.items():
                    obj = BaseModel(**value)
                    type(self).__objects[key] = obj
            print(type(self).__objects)
        except:
            pass
