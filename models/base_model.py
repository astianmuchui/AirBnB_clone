#!/usr/bin/python3

import uuid
from datetime import datetime
class BaseModel():

    """
        This is the base model for the HBNB Project
        To be extended by the other classes
    """

    def __str__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs is not None:
            pass
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

        return temp
    pass
