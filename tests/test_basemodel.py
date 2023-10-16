from models.base_model import BaseModel
import unittest
from datetime import datetime

my_model = BaseModel()
class Test(unittest.TestCase):

    def test_id(self):
        self.assertEqual(type(my_model.id), str)

    def test_created_at(self):
        self.assertEqual(type(my_model.created_at), datetime)

    def test_updated_at(self):
        self.assertEqual(type(my_model.updated_at), datetime)

    def test_str(self):
        self.assertEqual(str(my_model), "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__))

    def test_save(self):
        my_model.save()
        self.assertNotEqual(my_model.created_at, my_model.updated_at)

    def test_to_dict(self):
        my_model_dict = my_model.to_dict()
        self.assertEqual(type(my_model_dict), dict)
        self.assertTrue('__class__' in my_model_dict)
        self.assertEqual(type(my_model_dict['created_at']), str)
        self.assertEqual(type(my_model_dict['updated_at']), str)
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')
