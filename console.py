#!/usr/bin/env python3
"""Console program main file."""
import cmd
import re
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from typing import Callable, Any


class HBNBCommand(cmd.Cmd):
    """Define a command-line interpreter."""

    prompt = "(hbnb) "
    models = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }
    update_dict = {}

    def do_create(self, line: str):
        """Create an object.

        Usage:
        create <class>
        <class>.create()
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
        <class>.show(<id>)
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
        <class>.destroy(<id>)
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
        <class>.all()
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

    def do_count(self, line: str):
        """Count all instances of a model.

        Usage:
        count [class]
        <class>.count()
        """
        instances = storage.all()
        if not self.__validate(line):
            return
        class_name = line.strip().split(" ")[0]
        count = 0
        for key in instances:
            if class_name in key:
                count += 1
        print(count)

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
                for key in self.update_dict:
                    setattr(instance, key, type(
                        getattr(instance, key, ""))(self.update_dict[key]))
                self.update_dict = {}
                instance.save()
        self.__on_found(key, callback)

    def do_EOF(self, line: str):
        """Exit gracefully."""
        return True

    def do_quit(self, line: str):
        """Quit command to exit the program."""
        return True

    def parseline(self, line: str):
        """Before running input command."""
        match = re.search(r"^(\w+)\.(\w+)\((.*)\)$", line)
        if match is None:
            return cmd.Cmd.parseline(self, line)
        matches = list(filter(lambda x: x != "", list(match.groups())))
        if len(matches) > 2:
            args = matches[2:][0]
            args_list = args.split(",", maxsplit=1)
            if len(args_list) > 1:
                payload = args_list[1].strip()
                if re.match(r"^{.*}$", payload):
                    payload = re.sub(r"'", "\"", payload)
                    payload = json.loads(payload)
                    args = args_list[:1]
                    self.update_dict = payload
                    for key, value in payload.items():
                        args.append(key)
                        args.append(value)
                else:
                    args = args.split(",")
            else:
                args = args.split(",")
            args = list(map(lambda x: x.strip(), args))
            matches = matches[:2] + args
        if len(matches) > 1:
            tmp = matches[0]
            matches[0] = matches[1]
            matches[1] = tmp
            args = [" ".join(matches[1:])]
            matches = matches[:1] + args
        return tuple(matches + [" ".join(matches)])

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
