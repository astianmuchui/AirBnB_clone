#!/usr/bin/python3
import json
import os
from models.user import User
from models.base_model import BaseModel

class FileStorage:

    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}
    pass

    def all(self):
        return self.__objects
    pass

    def new(self, obj):
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj
    pass

    def save(self):
        obj_t = {}
        for k, ob in self.__objects.items():
            obj_t[k] = ob.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(obj_t, file)
    pass

    def reload(self):

        objects = {
            'BaseModel': BaseModel,
            # 'State': State,
            # 'City': City,
            # 'Amenity': Amenity,
            # 'Place': Place,
            # 'Review': Review,
            'User': User
        }
        if os.path.exists(self.__file_path) and os.path.getsize(self.__file_path) > 0:
            with open(self.__file_path, "r") as file:
                self.__objects = json.load(file)
        else:
            pass
    pass

