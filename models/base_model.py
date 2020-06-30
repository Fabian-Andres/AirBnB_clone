#!/usr/bin/python3
""" [BaseModel class] """
import uuid
import datetime
from models import storage


class BaseModel:
    """[BaseModel]
        BaseModel defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """Init"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                elif key == "updated_at" or key == "created_at":
                    setattr(self, key, datetime.datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        """print: [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values """
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

    def update(self, name, value):
        """set with the current datetime"""
        setattr(self, name, value)
        self.save()
