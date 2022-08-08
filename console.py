
import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
