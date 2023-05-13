#!/usr/bin/env python3
"""Module for testing FileStorage class."""
import unittest
import json
from models import storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Define tests for FileStorage class."""

    def test_all_type(self):
        objs = storage.all()
        self.assertIsInstance(objs, dict)

    def test_new(self):
        obj = BaseModel()
        key = "{:s}.{:s}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, storage.all().keys())

    def test_new_multiple(self):
        objs = [BaseModel() for _ in range(5)]
        for obj in objs:
            key = "{:s}.{:s}".format(obj.__class__.__name__, obj.id)
            self.assertIn(key, storage.all().keys())

    def test_save(self):
        obj = BaseModel()
        obj.save()
        with open("objects.json", "r") as file:
            dictionary = json.load(file)
            key = "{:s}.{:s}".format(obj.__class__.__name__, obj.id)
            self.assertIn(key, dictionary.keys())

    def test_reload(self):
        objs = [BaseModel() for _ in range(5)]
        for obj in objs:
            obj.save()
        storage.reload()
        for obj in objs:
            key = "{:s}.{:s}".format(obj.__class__.__name__, obj.id)
            self.assertIn(key, storage.all().keys())


if __name__ == "__main__":
    unittest.main()
