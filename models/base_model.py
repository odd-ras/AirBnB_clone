#!/usr/bin/env python3
"""Module containing the class BaseModel."""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """Defines all common attributes/methods for other classes.

    Attributes:
        id (str): A unique ID for instance
        created_at (str): A datetime object of instance created time
        updated_at (str): A datetime object of instance updated time
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel object."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if kwargs is None:
            kwargs = {}

        for key in kwargs:
            if key != "__class__":
                value = kwargs[key]
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)

        if kwargs == {}:
            storage.new(self)

    def __str__(self):
        """Informal string representation of instance."""
        return "[{:s}] ({:s}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def save(self):
        """Update the attribute updated_at with the current datetime."""
        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """Get __dict__ dictionary of key/value pairs.

        Returns:
            dict: A dictionary containing all keys/values of __dict__
            of the instance
        """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
