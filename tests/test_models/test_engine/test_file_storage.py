#!/usr/bin/python3

import unittest
from models.engine import file_storage

from json import dumps, loads


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def test_all(self):
        """all method"""
        return FileStorage.__objects

    def test_new(self, obj):
        """new method"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            FileStorage.__objects[key] = obj

    def test_save(self):
        """save method"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def test_reload(self):
        """serialize"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except Exception:
            pass
