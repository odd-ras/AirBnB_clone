#!/usr/bin/env python3
"""Console program main file."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Define a command-line interpreter."""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Exit gracefully."""
        return True

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
