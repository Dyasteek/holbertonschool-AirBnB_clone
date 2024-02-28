#!/usr/bin/python3
"""Command interpreter for HBnB"""
import cmd
from models.base_model import BaseModel
from models import storage


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
        
    def do_create(self, *args):
        """Create a new instance of BaseModel subclass"""
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        if args != "BaseModel":
            print("** class doesn't exist **")
            return
        else:
            model = BaseModel()
            print(model.id)
        
    def do_show(self, *args):
        """Show all instances of a given class"""
        model = BaseModel()
        if not args:
            print("** class name missing **")
            return
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if args[1] != model.id:
            model_id = args[1]
        if model_id not in storage.get(args[0], model_id):
            print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
