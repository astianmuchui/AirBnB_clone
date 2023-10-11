#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel():

    """
        This is the base model for the HBNB Project
        To be extended by the other classes
    """

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            keys = kwargs.keys()

            for key in keys:
                if key == "created_at" or key == "updated_at":
                    kwargs[key] = str(datetime.strptime(kwargs[key], "%Y-%m-%dT%H:%M:%S.%f"))
                if key != "__class__":
                    setattr(self, key, kwargs[key])
    pass

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    pass


    def save(self):
        self.updated_at = (datetime.now())
    pass


    def to_dict(self):
        self.created_at = datetime.isoformat(self.created_at)
        self.updated_at = datetime.isoformat(self.updated_at)
        temp = self.__dict__.copy()
        temp["__class__"] = self.__class__.__name__

        return dict(temp)
    pass
