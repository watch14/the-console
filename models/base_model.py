"""basemodel"""
import uuid
from datetime import datetime


class BaseModel():
    """BaseModel Class"""

    def __init__(self, *args, **kwargs):
        """Public instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """return string info"""
        return ('[' + type(self).__name__ + '] (' + str(self.id) +
               ') ' + str(self.__dict__))
    
    def save(self):
        """ save / update """ 
        self.updated_at = str(datetime.now())

    def to_dict(self):
        """return a dictionary of the instance"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = type(self).__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict