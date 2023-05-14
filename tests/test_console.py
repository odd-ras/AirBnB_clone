#!/usr/bin/env python3
"""Module for testing console."""
import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch

objects_path = os.path.join(os.path.abspath("objects.json"))


class TestHBNBCommand_Help(unittest.TestCase):
    """Define unit tests forconsole help commands."""

    def test_prompt_str(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip().strip())

    def test_help_EOF(self):
        message = "Exit gracefully."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(message, output.getvalue().strip().strip())

    def test_help_quit(self):
        message = "Quit command to exit the program."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(message, output.getvalue().strip().strip())

    def test_help_create(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertNotIn("*** No help", output.getvalue().strip().strip())

    def test_help_show(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertNotIn("*** No help", output.getvalue().strip().strip())

    def test_help_destroy(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertNotIn("*** No help", output.getvalue().strip().strip())

    def test_help_all(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertNotIn("*** No help", output.getvalue().strip().strip())

    def test_help_count(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertNotIn("*** No help", output.getvalue().strip().strip())

    def tearDown(self):
        try:
            os.remove(os.path.join(os.path.abspath("objects.json")))
        except FileNotFoundError:
            pass


class TestHBNBCommand_Execute(unittest.TestCase):
    """Defin unit tests for console commands execution."""

    def test_quit(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_create(self):
        command = "create BaseModel"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(command)
            self.assertIsInstance(output.getvalue().strip(), str)
            self.assertNotEqual(output.getvalue().strip(), "")
            self.assertNotEqual(output.getvalue().strip(), "\n")
            self.assertGreater(len(output.getvalue().strip()), 0)

    def test_create_method(self):
        command = "BaseModel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(command)
            self.assertIsInstance(output.getvalue().strip(), str)
            self.assertNotEqual(output.getvalue().strip(), "")
            self.assertNotEqual(output.getvalue().strip(), "\n")
            self.assertGreater(len(output.getvalue().strip()), 0)

    def test_show(self):
        command = "create BaseModel"
        instance_id = ""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(command)
            instance_id = output.getvalue().strip()
            self.assertIsInstance(instance_id, str)
        command = f"show BaseModel {instance_id}"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(command)
            self.assertIsInstance(output.getvalue().strip(), str)
            self.assertNotEqual(output.getvalue().strip(), "")
            self.assertNotEqual(output.getvalue().strip(), "\n")
            self.assertIn(instance_id, output.getvalue().strip())

    def test_show_method(self):
        command = "BaseModel.create()"
        instance_id = ""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(command)
            instance_id = output.getvalue().strip()
            self.assertIsInstance(instance_id, str)
        command = f"BaseModel.show({instance_id})"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(command)
            self.assertIsInstance(output.getvalue().strip(), str)
            self.assertNotEqual(output.getvalue().strip(), "")
            self.assertNotEqual(output.getvalue().strip(), "\n")
            self.assertIn(instance_id, output.getvalue().strip())

    def test_update(self):
        command = "create BaseModel"
        instance_id = ""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(command)
            instance_id = output.getvalue().strip()
            self.assertIsInstance(output.getvalue().strip(), str)
            self.assertNotEqual(output.getvalue().strip(), "")
            self.assertNotIn("**", output.getvalue().strip())
        command = f"update BaseModel {instance_id} name Michael"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(command)
            self.assertEqual("", output.getvalue().strip())

    def test_update_method(self):
        command = "User.create()"
        instance_id = ""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(command)
            instance_id = output.getvalue().strip()
            self.assertIsInstance(output.getvalue().strip(), str)
            self.assertNotEqual(output.getvalue().strip(), "")
            self.assertNotIn("**", output.getvalue().strip())
        command = f"User.update({instance_id}, first_name, Michael)"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(command)
            self.assertEqual("", output.getvalue().strip())

    def test_update_method_dict(self):
        command = "BaseModel.create()"
        instance_id = ""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(command)
            instance_id = output.getvalue().strip()
            self.assertIsInstance(output.getvalue().strip(), str)
            self.assertNotEqual(output.getvalue().strip(), "")
            self.assertNotIn("**", output.getvalue().strip())
        update_dict = {"first_name": "Michael"}
        command = f"BaseModel.update({instance_id}, {update_dict})"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(command)
            self.assertEqual("", output.getvalue().strip())

    def test_update_method_dict_multiple(self):
        command = "User.create()"
        instance_id = ""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(command)
            instance_id = output.getvalue().strip()
            self.assertIsInstance(output.getvalue().strip(), str)
            self.assertNotEqual(output.getvalue().strip(), "")
            self.assertNotIn("**", output.getvalue().strip())
        update_dict = {"first_name": "Michael", "last_name": "Peter"}
        command = f"User.update({instance_id}, {update_dict})"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(command)
            self.assertEqual("", output.getvalue().strip())

    def test_destroy(self):
        command = "create BaseModel"
        instance_id = ""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(command)
            instance_id = output.getvalue().strip()
            self.assertIsInstance(output.getvalue().strip(), str)
            self.assertNotEqual(output.getvalue().strip(), "")
            self.assertNotIn("**", output.getvalue().strip())
        command = f"destroy BaseModel {instance_id}"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(command)
            self.assertEqual("", output.getvalue().strip())
        command = f"show BaseModel {instance_id}"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(command)
            self.assertEqual("** no instance found **",
                             output.getvalue().strip())

    def test_destroy_method(self):
        command = "BaseModel.create()"
        instance_id = ""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(command)
            instance_id = output.getvalue().strip()
            self.assertIsInstance(output.getvalue().strip(), str)
            self.assertNotEqual(output.getvalue().strip(), "")
            self.assertNotIn("**", output.getvalue().strip())
        command = f"BaseModel.destroy({instance_id})"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(command)
            self.assertEqual("", output.getvalue().strip())
        command = f"BaseModel.show({instance_id})"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(command)
            self.assertEqual("** no instance found **",
                             output.getvalue().strip())

    def test_all(self):
        try:
            os.remove(objects_path)
        except FileNotFoundError:
            pass
        for _ in range(5):
            command = "create BaseModel"
            instance_id = ""
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd(command)
                instance_id = output.getvalue().strip()
                self.assertIsInstance(output.getvalue().strip(), str)
                self.assertNotEqual(output.getvalue().strip(), "")
                self.assertNotEqual(output.getvalue().strip(), "\n")
        command = "all"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(command)
            self.assertIn("BaseModel", output.getvalue().strip())

    def test_all_class(self):
        try:
            os.remove(objects_path)
        except FileNotFoundError:
            pass
        for _ in range(5):
            command = "BaseModel.create()"
            instance_id = ""
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd(command)
                instance_id = output.getvalue().strip()
                self.assertIsInstance(output.getvalue().strip(), str)
                self.assertNotEqual(output.getvalue().strip(), "")
                self.assertNotEqual(output.getvalue().strip(), "\n")
        command = "all BaseModel"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(command)
            self.assertIn("BaseModel", output.getvalue().strip())

    def test_all_class_method(self):
        try:
            os.remove(objects_path)
        except FileNotFoundError:
            pass
        for _ in range(5):
            command = "User.create()"
            instance_id = ""
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd(command)
                instance_id = output.getvalue().strip()
                self.assertIsInstance(output.getvalue().strip(), str)
                self.assertNotEqual(output.getvalue().strip(), "")
                self.assertNotEqual(output.getvalue().strip(), "\n")
        command = "User.all()"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(command)
            self.assertIn("User", output.getvalue().strip())

    def test_count(self):
        try:
            os.remove(objects_path)
        except FileNotFoundError:
            pass
        for _ in range(5):
            command = "create User"
            instance_id = ""
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd(command)
                instance_id = output.getvalue().strip()
                self.assertIsInstance(output.getvalue().strip(), str)
                self.assertNotEqual(output.getvalue().strip(), "")
                self.assertNotEqual(output.getvalue().strip(), "\n")
        command = "User.count()"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(command)
            self.assertIsInstance(int(output.getvalue().strip()), int)
            self.assertGreaterEqual(int(output.getvalue().strip()), 5)

    def test_count_method(self):
        try:
            os.remove(objects_path)
        except FileNotFoundError:
            pass
        for _ in range(5):
            command = "User.create()"
            instance_id = ""
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd(command)
                instance_id = output.getvalue().strip()
                self.assertIsInstance(output.getvalue().strip(), str)
                self.assertNotEqual(output.getvalue().strip(), "")
                self.assertNotEqual(output.getvalue().strip(), "\n")
        command = "User.count()"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(command)
            self.assertIsInstance(int(output.getvalue().strip()), int)
            self.assertGreaterEqual(int(output.getvalue().strip()), 5)

    def tearDown(self):
        try:
            os.remove(objects_path)
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    unittest.main()
