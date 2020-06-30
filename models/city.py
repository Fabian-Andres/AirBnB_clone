#!/usr/bin/python3
""" [City class] """
from models.base_model import BaseModel


class City(BaseModel):
    """[City]
        Class inherit from BaseModel:
    Args:
        BaseModel ([class]):
        [BaseModel defines all common attributes/methods for other classes]
    """

    state_id = ""
    name = ""
