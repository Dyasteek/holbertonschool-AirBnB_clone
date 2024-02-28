#!/usr/bin/python3
"""Base model for all others classes"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Base class with all common attributes and methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initializates the BaseModel instance"""
        if len(kwargs) is not 0:
            for key in kwargs:
                if key != "__class__":
                    if key == "updated_at" or key == "created_at":
                        setattr(self, key, datetime.
                                strptime(kwargs[key], "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, kwargs[key])

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """String representation of the BaseModel instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates the date of the attribute updated_at"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the BaseModel instance"""
        self_dict = {}
        for key in self.__dict__:
            self_dict[key] = self.__dict__[key]
        self_dict["__class__"] = self.__class__.__name__
        self_dict["created_at"] = self.created_at.strftime(
            "%Y-%m-%dT%H:%M:%S.%f")
        self_dict["updated_at"] = self.updated_at.strftime(
            "%Y-%m-%dT%H:%M:%S.%f")
        return self_dict
