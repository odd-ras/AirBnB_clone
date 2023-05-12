#!/usr/bin/env python3
"""Module for FileStorage class."""
import json


class FileStorage():
    """Define a FileStorage object."""

    __file_path = "objects.json"
    __objects = {}

    def all(self):
        """Get objects dictionary."""
        return FileStorage.__objects

    def new(self, obj):
        """Add a new object to dictionary.

        Attributes:
            obj (object): Object to add
        """
        key = "{:s}.{:s}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Save objects to JSON file."""
        json_str = json.dumps(self.__objects)
        with open(self.__file_path, "w") as file:
            file.write(json_str)

    def reload(self):
        """Reload objects from JSON file."""
        try:
            with open(self.__file_path, "r") as file:
                json_str = file.read()
                objects = json.loads(json_str)
        except FileNotFoundError:
            pass
