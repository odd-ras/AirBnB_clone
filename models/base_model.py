#!/usr/bin/env python3
"""Module containing the class BaseModel."""
import uuid
import datetime


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
        self.created_at = datetime.datetime()
        self.updated_at = datetime.datetime()

    def __str__(self):
        """Informal string representation of instance."""
        return "[{:s}] ({:s}) {:s}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )
