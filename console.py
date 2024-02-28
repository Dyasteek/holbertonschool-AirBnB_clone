#!/usr/bin/python3
"""Command interpreter for HBnB"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBnB"""

    prompt = '(hbnb) '

    def emptyline(self):
        """Empty line or spaces do nothing."""
        pass

    def do_quit(self, *args):
        """Command to exit."""
        return True

    def do_EOF(self, *args):
        """Another command that exit the program."""
        return True
    
    def do_help(self, *args):
        """Help command"""
        print("Quit command to exit the program")

    def do_create(self, *args):
        """Creates a new instance of an object"""
        arg = args[0].split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.models:
            print("** class doesn't exist **")
        else:
            class_name = arg[0]
        if class_name in globals():
            obj = globals()[class_name]()
            obj.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, *args):
        """Prints the string representation of an instance"""
        arg = args[0].split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.models:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            obj_dict = storage.all()
            key = "{}.{}".format(arg[0], arg[1])
            if key not in obj_dict:
                print("** no instance found **")
            else:
                print(obj_dict[key])
                

if __name__ == '__main__':
    HBNBCommand().cmdloop()
