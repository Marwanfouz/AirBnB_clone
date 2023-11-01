#!/usr/bin/python3
"""Define the BaseModel class."""

import uuid
from datetime import datetime
import models


class BaseModel:
    """Represents the BaseModel of the HBnB project."""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """String representation of the BaseModel class."""
        s = "[{}] ({}) {}"
        return s.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        to_my_dict = self.__dict__.copy()
        to_my_dict['__class__'] = self.__class__.__name__
        to_my_dict['created_at'] = self.created_at.isoformat()
        to_my_dict['updated_at'] = self.updated_at.isoformat()
        return to_my_dict
