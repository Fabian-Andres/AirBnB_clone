#!/usr/bin/python3
""" [Review class] """
from models.base_model import BaseModel


class Review(BaseModel):
    """[Review]
        Class inherit from BaseModel:
    Args:
        BaseModel ([class]):
        [BaseModel defines all common attributes/methods for other classes]
    """

    place_id = ""
    user_id = ""
    text = ""
