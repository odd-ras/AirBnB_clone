#!/usr/bin/python3
"""Module for Review tests."""
import unittest
from datetime import datetime
from models.review import Review
from models.base_model import BaseModel
from models import storage


class TestReview(unittest.TestCase):
    """Define tests for Review class."""

    def test_instance(self):
        obj = Review()
        self.assertIsInstance(obj, Review)
        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(isinstance(obj, BaseModel))

    def test_instance_with_none(self):
        obj = Review(None)
        self.assertNotIn(None, obj.__dict__.values())

    def test_stored_instances(self):
        for _ in range(5):
            obj = Review()
            obj.save()
        objs = storage.all()
        for key in objs:
            self.assertIsInstance(objs[key], (BaseModel, Review))

    def test_attributes(self):
        obj = Review()
        self.assertIsNotNone(obj.id)
        self.assertIsNotNone(obj.created_at)
        self.assertIsNotNone(obj.updated_at)
        self.assertIsNotNone(obj.place_id)
        self.assertIsNotNone(obj.user_id)
        self.assertIsNotNone(obj.text)

    def test_id_is_str(self):
        obj = Review()
        self.assertIsInstance(obj.id, str)

    def test_place_id_is_str(self):
        obj = Review()
        self.assertIsInstance(obj.place_id, str)

    def test_user_id_is_str(self):
        obj = Review()
        self.assertIsInstance(obj.user_id, str)

    def test_text_is_str(self):
        obj = Review()
        self.assertIsInstance(obj.text, str)

    def test_created_at_is_datetime(self):
        obj = Review()
        self.assertIsInstance(obj.created_at, datetime)

    def test_updated_at_is_datetime(self):
        obj = Review()
        self.assertIsInstance(obj.updated_at, datetime)

    def test_id_is_unique(self):
        obj1 = Review()
        obj2 = Review()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_serial_created_at(self):
        obj1 = Review()
        obj2 = Review()
        self.assertNotEqual(obj1.created_at, obj2.created_at)
        obj1_timestamp = obj1.created_at.timestamp()
        obj2_timestamp = obj2.created_at.timestamp()
        self.assertLess(obj1_timestamp, obj2_timestamp)

    def test_serial_updated_at(self):
        obj1 = Review()
        obj2 = Review()
        self.assertNotEqual(obj1.updated_at, obj2.updated_at)
        obj1_timestamp = obj1.updated_at.timestamp()
        obj2_timestamp = obj2.updated_at.timestamp()
        self.assertLess(obj1_timestamp, obj2_timestamp)

    def test_str(self):
        obj = Review()
        obj.id = "ABC"
        obj_sub_str = "[Review] (ABC)"
        self.assertIn(obj_sub_str, obj.__str__())

    def test_to_dict(self):
        obj = Review()
        to_dict_result = obj.to_dict()
        self.assertIsInstance(to_dict_result, dict)

        values = obj.__dict__
        for key in values:
            if key not in ["created_at", "updated_at"]:
                self.assertIn(values[key], to_dict_result.values())

    def test_instance_with_args(self):
        obj = Review("ABC", "124")
        self.assertNotEqual("ABC", obj.id)
        self.assertNotEqual("124", obj.id)
        self.assertNotIn("ABC", obj.__dict__.values())
        self.assertNotIn("124", obj.__dict__.values())

    def test_instance_with_kwargs(self):
        obj = Review(id="ABC", text="Nice")
        self.assertEqual("ABC", obj.id)
        self.assertEqual("Nice", obj.text)

    def test_instance_with_args_kwargs(self):
        obj = Review("ABC", id="124", text="Great")
        self.assertNotEqual("ABC", obj.id)
        self.assertEqual("124", obj.id)
        self.assertEqual("Great", obj.text)
        self.assertNotIn("ABC", obj.__dict__.values())
        self.assertIn("124", obj.__dict__.values())
        self.assertIn("Great", obj.__dict__.values())


if __name__ == "__main__":
    unittest.main()
