"""FileStorage: serializes and deserializes"""
import json
import os
import models

class FileStorage ():
    """FileStorage Class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns __objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """set obj"""
        k_o = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[k_o] = obj

    def save(self):
        """Sereialize JSON"""
        obj_dic = {}
        for key in FileStorage.__objects.keys():
            obj = FileStorage.__objects[key]
            obj_dic[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dic, f)

    def reload(self):
        """Deserialize JSON"""
        if (os.path.isfile(FileStorage.__file_path)):
            with open(FileStorage.__file_path, "r") as f:
                de_json = json.load(f)
                for key, value in de_json.items():
                    FileStorage.__objects[key] = eval(
                        value['__class__'])(**value)
                    

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
    my_new_model = BaseModel(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))

    print("--")
    print(my_model is my_new_model)