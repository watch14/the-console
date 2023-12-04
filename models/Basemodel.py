"""basemodel"""
import uuid
from datetime import datetime
import json
#import models

class BaseModel():
    """BaseModel Class"""

    def __init__(self, *args, **kwargs):
        """Public instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = str(datetime.now())
        self.updated_at = str(datetime.now())

    def __str__(self):
        """return string info"""
        return ('[' + type(self).__name__ + '] (' + str(self.id) +
               ') ' + str(self.__dict__))
    
    def save(self):
        """ save / update """ 
        self.updated_at = str(datetime.now())

    def to_dict(self):
        datetime.strptime(self.created_at, "%Y-%m-%d %H:%M:%S.%f")