"""FileStorage: serializes and deserializes"""
import json
import os
import models

class FileStorage ():
    """FileStorage Class"""

    def __init__(self):
        """attributes"""
        self.__file_path = "file.json"
        self.__objects = {}

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