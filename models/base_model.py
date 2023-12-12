#!/usr/bin/python3
"""BaseModel"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """BaseModel Class"""

    def __init__(self, *args, **kwargs):
        """Public instance attributes"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        time_form = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at ":
                    self.created_at = datetime.strptime(value, time_form)
                if key == "updated_at ":
                    self.updated_at = datetime.strptime(value, time_form)
                if key == "id":
                    self.id = value
        models.storage.new(self)

    def __str__(self):
        """return string info"""
        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)

    def save(self):
        """ save / update """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """return a dictionary of the instance"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = type(self).__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
