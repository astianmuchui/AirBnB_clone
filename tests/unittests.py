from models.base_model import BaseModel
import unittest
from datetime import datetime

my_model = BaseModel()
class Test(unittest.TestCase):
    def test_instance(self):
        self.assertIsNotNone(my_model)
        self.assertIsInstance(my_model, BaseModel)
    pass

    def test_str(self):
        self.assertEqual(str(my_model), "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__))
        self.assertIsInstance(str(my_model), str)
        self.assertIsNotNone(str(my_model))
    pass

    def test_save(self):
        self.assertNotEqual(my_model.created_at, my_model.updated_at)
        self.assertIsInstance(my_model.updated_at, datetime)
        self.assertIsInstance(my_model.created_at, datetime)
    pass

    def test_dict(self):
        self.assertIsNotNone(my_model.to_dict())
    pass