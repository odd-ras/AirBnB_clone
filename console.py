#!/usr/bin/env python3
"""Console program main file."""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from typing import Callable, Any


class HBNBCommand(cmd.Cmd):
    """Define a command-line interpreter."""

    prompt = "(hbnb) "
    models = {
        "BaseModel": BaseModel,
        "User": User
    }

    def do_create(self, line: str):
        """Create an object.

        Usage:
        create <class>
        """
        if not self.__validate(line):
            return
        line = line.strip()
        obj = self.models[line]()
        obj.save()
        print(obj.id)

    def do_show(self, line: str):
        """Print an object.

        Usage:
        show <class> <id>
        """
        if not self.__validate(line, withId=True):
            return
        key = ".".join(line.strip().split(" "))

        def callback(instance): print(instance.__str__())
        self.__on_found(key, callback)

    def do_destroy(self, line: str):
        """Destroy an object.

        Usage:
        destroy <class> <id>
        """
        if not self.__validate(line, withId=True):
            return
        key = ".".join(line.strip().split(" "))

        def callback(key):
            del storage.all()[key]
            storage.save()
        self.__on_found(key, callback, returnKey=True)

    def do_all(self, line: str):
        """Print all instances.

        Usage:
        all [class]
        """
        instances = storage.all()
        if not line:
            for key in instances:
                print(instances[key])
            return
        if not self.__validate(line):
            return
        class_name = line.strip().split(" ")[0]
        for key in instances:
            if class_name in key:
                print(instances[key])

    def do_update(self, line: str):
        """Update an object.

        Usage:
        update <class> <id> <attribute> "<value>"
        """
        if not self.__validate(line, withAttr=True):
            return
        [command, instance_id, attr, value] = line.strip().split(" ")[:4]
        key = ".".join([command, instance_id])

        def callback(instance):
            try:
                setattr(instance, attr, type(
                    getattr(instance, attr, ""))(value))
            except (TypeError, ValueError):
                setattr(instance, attr, value)
            finally:
                instance.save()
        self.__on_found(key, callback)

    def do_EOF(self, line: str):
        """Exit gracefully."""
        return True

    def do_quit(self, line: str):
        """Quit command to exit the program."""
        return True

    def emptyline(self):
        """Don't execute anything."""
        pass

    def __validate(self, line: str, **kwargs):
        if kwargs.get("withAttr"):
            kwargs["withId"] = True

        if not line:
            print("** class name missing **")
            return False
        line = line.strip()
        command = line.split(" ")[0]

        if command not in self.models.keys():
            print("** class doesn't exist **")
            return False
        if kwargs.get("withId"):
            try:
                instance_id = line.split(" ")[1]
            except IndexError:
                instance_id = None
            if instance_id is None:
                print("** instance id missing **")
                return False
        if kwargs.get("withAttr"):
            try:
                attribute = line.split(" ")[2]
            except IndexError:
                attribute = None
            try:
                value = line.split(" ")[3]
            except IndexError:
                value = None
            if attribute is None:
                print("** attribute name missing **")
                return False
            if value is None:
                print("** value missing **")
                return False
        return True

    def __on_found(self, key: str, callback: Callable[[Any], Any], **kwargs):
        instances = storage.all()
        for _key in instances:
            if _key == key:
                if kwargs.get("returnKey"):
                    callback(_key)
                else:
                    callback(instances[_key])
                return True
        else:
            print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
