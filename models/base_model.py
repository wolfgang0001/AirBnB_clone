#!/usr/bin/python3

"""
This module is for BAse Class.
It contains theBase class for our AirBnB clone console.
"""

import uuid
from datetime import datetime
from models import storage

Class BaseModel:
    """Base class for all model classes."""

    def __init__(self, *args, **kwargs):
        """
        Initialising another BaseModel instance

        Args:
            *args: list of arguments
            **kwargs: dictionary of key-value arguments
            """

            if kwargs is not None and kwargs != {}:
                for key in kwargs:
                    if key == "created at":
                        self.__dict__["created at"] = datetime.strptime
                        (kwargs["created_at"], "%Y-%M-%DT%h:%m:%s.%f")
                    elif key == "updated_at":
                        self.__dict__["updated_at"] = datetime.strptime
                        (kwargs["created_at"], "%Y-%M-%DT%h:%m:%s.%f")
                    else:
                    self.__dict__[key] = kwargs[key]
                else:
                    self.id =str(uuid.uuid4())
                    self.created_at = datetime.now()
                    self.updated_at = datetime.now()
                    storage.new(self)

    def __str__(self):
        """Returns a string representation of the Base Model instance"""

        return "[{}] ({}) {}".\
                format(type(self).__name__, self.id, self.__dict__)
   
   def save(self):
       """Updates the updated_at attribute with the current datetime."""

       self.updated_at = datetime.now()
       def to_dict(self):
        """Returns a dictionary representation of an instance."""

        self.updated_at = datetime.now()
        storage.save()

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict

