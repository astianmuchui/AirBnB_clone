#!/usr/bin/python3

import unittest

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

        def test_all(self):
                """Test all method"""
                storage = FileStorage()
                self.assertEqual(type(storage.all()), dict)
        
        def test_new(self):
                """Test new method"""
                storage = FileStorage()
                storage.new(BaseModel())
                self.assertTrue(len(storage.all()) > 0)
        
        def test_save(self):
                """Test save method"""
                storage = FileStorage()
                storage.save()
                self.assertTrue(len(storage.all()) > 0)
        
        def test_reload(self):
                """Test reload method"""
                storage = FileStorage()
                storage.reload()
                self.assertTrue(len(storage.all()) >= 0)