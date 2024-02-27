#!/usr/bin/python3
"""Command interpreter for HBnB"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter prompt"""

    prompt = '(hbnb)'

    def emptyline(self):
        """Does nothing when it receibes an empty line"""
        pass

    def do_quit(self, *args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, *args):
        """EOF command to exit the program"""
        return True

    def do_help(self, *args):
        """Help command"""
        print("Quit command to exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
