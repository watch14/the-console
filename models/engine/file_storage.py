"""FileStorage: serializes and deserializes"""
import json
import models

class FileStorage ():
    """FileStorage Class"""

    def __init__(self):
        """attributes"""
        self.__file_path = "file.json"
        self.__objects = {}