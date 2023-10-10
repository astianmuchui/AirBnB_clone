#!/usr/bin/python3
import uuid
from datetime import datetime
class BaseModel():

    """
        This is the base model for the HBNB Project
        To be extended by the other classes
    """
    def __str__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    pass

    def save(self):
        self.updated_at = (datetime.now())
    pass

    def to_dict(self):
        pass

