#!/usr/bin/python3
""" class Review inherited from class BaseModel """

from models.base_model import BaseModel


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""
