#!/usr/bin/env python3
"""Console program main file."""
import cmd
from models import storage
from models.base_model import BaseModel
from typing import Callable, Any


class HBNBCommand(cmd.Cmd):
    """Define a command-line interpreter."""

    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel}

    def do_create(self, line: str):
        """Create an object.

        Usage:
        create <class>
        """
        if not self.__validate(line):
            return
        line = line.strip()
        obj = self.classes[line]()
        obj.save()
        print(obj.id)

    def do_show(self, line: str):
        """Print an object.

        Usage:
        show <class> <id>
        """
        if not self.__validate(line, withId=True):
            return
        instance_id = line.strip().split(" ")[1]

        def callback(instance): print(instance.__str__())

        self.__on_found(instance_id, callback)

    def do_destroy(self, line):
        """Destroy an object.

        Usage:
        destroy <class> <id>
        """
        if not self.__validate(line, withId=True):
            return
        instance_id = line.strip().split(" ")[1]

        def callback(key):
            del storage.all()[key]
            storage.save()

        self.__on_found(instance_id, callback, key=True)

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

        def callback(instance):
            try:
                setattr(instance, attr, type(
                    getattr(instance, attr, ""))(value))
            except (TypeError, ValueError):
                setattr(instance, attr, value)
            finally:
                instance.save()

        self.__on_found(instance_id, callback)

    def do_EOF(self, line):
        """Exit gracefully."""
        return True

    def do_quit(self, line):
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

        if command not in self.classes.keys():
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

    def __on_found(self, id: str, callback: Callable[[Any], Any], **kwargs):
        instances = storage.all()
        for key in instances:
            if id == instances[key].id:
                if kwargs and kwargs["key"]:
                    callback(key)
                else:
                    callback(instances[key])
                return True
        else:
            print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
