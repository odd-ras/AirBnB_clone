#!/usr/bin/env python3
"""Module containing the class BaseModel."""
import uuid
from datetime import datetime


class BaseModel():
    """Defines all common attributes/methods for other classes.

    Attributes:
        id (str): A unique ID for instance
        created_at (str): A datetime object of instance created time
        updated_at (str): A datetime object of instance updated time
    """

    def __init__(self):
        """Initialize a new BaseModel object."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

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

    def to_dict(self):
        """Get __dict__ dictionary of key/value pairs.

        Returns:
            dict: A dictionary containing all keys/values of __dict__
            of the instance
        """
        dictionary = self.__dict__
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = datetime.isoformat(dictionary["created_at"])
        dictionary["updated_at"] = datetime.isoformat(dictionary["updated_at"])
        return dictionary
