#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd

from models import storage


class HBNBCommand(cmd.Cmd):
    """class for the command interpreter"""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """handles end of file character"""
        print()
        return True

    def do_quit(self, line):
        """exits the program"""
        return True

    def emptyline(self):
        """Doesn't do anything on ENTER"""
        pass

    def do_create(self, line):
        """creates an instance of base model, saves it to json file and prints the id"""
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            b = storage.classes()[line]()
            b.save()
            print(b.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
