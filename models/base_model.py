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


if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    print(my_model.id)
    print(my_model)
    print(type(my_model.created_at))
    print("--")
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

    print("--")
    print("--")

    my_new_model = BaseModel(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))

    print("--")
    print("--")
    
    print(my_model is my_new_model)