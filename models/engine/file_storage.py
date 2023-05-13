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
        dictionary = {}
        for key in FileStorage.__objects:
            dictionary[key] = FileStorage.__objects[key].to_dict()

        with open(FileStorage.__file_path, "w") as file:
            json.dump(dictionary, file)

    def reload(self):
        """Reload objects from JSON file."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        models = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
        }

        try:
            with open(FileStorage.__file_path, "r") as file:
                objects = json.load(file)
                for key in objects:
                    model_name = key.split(".")[0]
                    model = models[model_name]
                    objects[key] = model(**objects[key])
                FileStorage.__objects = objects
        except FileNotFoundError as error:
            return
