#!/usr/bin/python3
import json
import os
from models.user import User
from models.base_model import BaseModel

class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects
    pass

    def new(self, obj):
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj
    pass

    def save(self):
        new = {key: value for key, value in self.__objects.items()}

        with open(self.__file_path, "w") as f:
            json.dump(new, f)
    pass

    def reload(self):

        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as f:
                new = json.load(f)
                for key, value in new.items():
                    self.__objects[key] = eval(value["__class__"])(**value)
    pass

