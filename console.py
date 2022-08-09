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

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id"""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            words = line.split.(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist**")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
