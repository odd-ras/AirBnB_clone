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
        FileStorage.__objects[key] = obj

    def save(self):
        """Save objects to JSON file."""
        dictionary = {key: value.to_dict() for key,
                      value in FileStorage.__objects.items()}

        with open(FileStorage.__file_path, "w") as file:
            json.dump(dictionary, file)

    def reload(self):
        """Reload objects from JSON file."""
        with open(FileStorage.__file_path, "r") as file:
            try:
                FileStorage.__objects = json.load(file)
            except FileNotFoundError as error:
                print("oops an error occurred:", error)
