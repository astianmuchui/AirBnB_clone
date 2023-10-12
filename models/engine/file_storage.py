#!/usr/bin/python3
from json import dumps, loads
class FileStorage():

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
        with open(self.__file_path, "w") as f:
            for key, value in self.__objects.items():
                dumps(value.to_dict(), f)
    pass
