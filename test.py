#!/usr/bin/python3

from models import storage
from models.base_model import BaseModel
import json

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model)
my_model.save()
new = {key: value for key, value in storage.all()}
with open("file.json", "w") as f:
    json.dump(new, f)

print("All objects: {}".format(storage.all()))
