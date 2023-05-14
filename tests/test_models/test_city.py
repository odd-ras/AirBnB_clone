#!/usr/bin/python3
"""Module for City tests."""
import os
import unittest
from datetime import datetime
from models.city import City
from models.base_model import BaseModel
from models import storage

objects_path = os.path.join(os.path.abspath("objects.json"))


class TestCity(unittest.TestCase):
    """Define tests for City class."""

    def test_instance(self):
        obj = City()
        self.assertIsInstance(obj, City)
        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(isinstance(obj, BaseModel))

    def test_instance_with_none(self):
        obj = City(None)
        self.assertNotIn(None, obj.__dict__.values())

    def test_stored_instances(self):
        for _ in range(5):
            obj = City()
            obj.save()
        objs = storage.all()
        for key in objs:
            self.assertIsInstance(objs[key], (BaseModel, City))

    def test_attributes(self):
        obj = City()
        self.assertIsNotNone(obj.id)
        self.assertIsNotNone(obj.created_at)
        self.assertIsNotNone(obj.updated_at)
        self.assertIsNotNone(obj.state_id)
        self.assertIsNotNone(obj.name)

    def test_id_is_str(self):
        obj = City()
        self.assertIsInstance(obj.id, str)

    def test_state_id_is_str(self):
        obj = City()
        self.assertIsInstance(obj.state_id, str)

    def test_name_is_str(self):
        obj = City()
        self.assertIsInstance(obj.name, str)

    def test_created_at_is_datetime(self):
        obj = City()
        self.assertIsInstance(obj.created_at, datetime)

    def test_updated_at_is_datetime(self):
        obj = City()
        self.assertIsInstance(obj.updated_at, datetime)

    def test_id_is_unique(self):
        obj1 = City()
        obj2 = City()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_serial_created_at(self):
        obj1 = City()
        obj2 = City()
        self.assertNotEqual(obj1.created_at, obj2.created_at)
        obj1_timestamp = obj1.created_at.timestamp()
        obj2_timestamp = obj2.created_at.timestamp()
        self.assertLess(obj1_timestamp, obj2_timestamp)

    def test_serial_updated_at(self):
        obj1 = City()
        obj2 = City()
        self.assertNotEqual(obj1.updated_at, obj2.updated_at)
        obj1_timestamp = obj1.updated_at.timestamp()
        obj2_timestamp = obj2.updated_at.timestamp()
        self.assertLess(obj1_timestamp, obj2_timestamp)

    def test_str(self):
        obj = City()
        obj.id = "ABC"
        obj_sub_str = "[City] (ABC)"
        self.assertIn(obj_sub_str, obj.__str__())

    def test_to_dict(self):
        obj = City()
        to_dict_result = obj.to_dict()
        self.assertIsInstance(to_dict_result, dict)

        values = obj.__dict__
        for key in values:
            if key not in ["created_at", "updated_at"]:
                self.assertIn(values[key], to_dict_result.values())

    def test_instance_with_args(self):
        obj = City("ABC", "124")
        self.assertNotEqual("ABC", obj.id)
        self.assertNotEqual("124", obj.id)
        self.assertNotIn("ABC", obj.__dict__.values())
        self.assertNotIn("124", obj.__dict__.values())

    def test_instance_with_kwargs(self):
        obj = City(id="ABC", name="Nice Place")
        self.assertEqual("ABC", obj.id)
        self.assertEqual("Nice Place", obj.name)

    def test_instance_with_args_kwargs(self):
        obj = City("ABC", id="124", name="Great City")
        self.assertNotEqual("ABC", obj.id)
        self.assertEqual("124", obj.id)
        self.assertEqual("Great City", obj.name)
        self.assertNotIn("ABC", obj.__dict__.values())
        self.assertIn("124", obj.__dict__.values())
        self.assertIn("Great City", obj.__dict__.values())

    def tearDown(self):
        try:
            os.remove(objects_path)
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    unittest.main()
