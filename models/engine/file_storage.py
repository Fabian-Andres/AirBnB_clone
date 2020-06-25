#!/usr/bin/python3
""" [FileStorage class] """
import json

class FileStorage:

    __file_path = "file.json"
    __objects = {}
        
    def all(self):
        return type(self).__objects

    def new(self, obj):
        type(self).__objects[obj.id] = obj.to_dict()

    def save(self):
        with open(type(self).__file_path, 'w', encoding="utf-8") as f:
            json.dump(type(self).__objects, f)
    
    def reload(self): 
        try:
            with open(type(self).__file_path, 'r', encoding="utf-8") as f:
                type(self).__objects = json.load(f)
        except:
            pass
          