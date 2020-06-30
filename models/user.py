#!/usr/bin/python3
""" [User class] """
from models.base_model import BaseModel


class User(BaseModel):
    """[User]
        Class inherit from BaseModel:
    Args:
        BaseModel ([class]):
        [BaseModel defines all common attributes/methods for other classes]
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
