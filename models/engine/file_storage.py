"""FileStorage: serializes and deserializes"""
import json
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
        try:
            with open(FileStorage.__file_path, "r") as f:
                obj_dic = json.load(f)

            for value in obj_dic.values():
                n_cls = value["__class__"]
                del value["__class__"]
                self.new(eval(n_cls)(**value))
        except FileNotFoundError:
            return