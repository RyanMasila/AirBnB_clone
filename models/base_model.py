#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
"""BaseModel defines all common attributes/methods for other classes"""


class BaseModel:
    """Represents BaseModel"""
    def __init__(self, *args, **kwargs):
        """Initializing a BaseModel
        Args:
            *args (any): Unused.
            **kwargs (dict): key/value paires of attributes
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__ = v
        else:
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current day time."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance"""
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance"""
        clName = self.__class__.__name__
        return "[{}] ({}) {}".format(clName, self.id, self.__dict__)
