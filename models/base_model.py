#!/usr/bin/python3
""" [summary] """
import uuid
import datetime


class BaseModel:

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        
        dictionary = {}

        dictionary["__class__"] = self.__class__.__name__

        for key, value in self.__dict__.items():
            if key == "updated_at":
                dictionary[key] = self.updated_at.isoformat()
            elif key == "created_at":
                dictionary[key] = self.created_at.isoformat()
            else:
                dictionary[key] = value
    
        return dictionary
