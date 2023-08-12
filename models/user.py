#!/usr/bin/python3

""" add by mr-you """
from models.base_model import BaseModel


class User(BaseModel):
    """ User class inherited BaseModel class"""
    email = ""
    password = ""
    frist_name = ""
    last_name = ""
