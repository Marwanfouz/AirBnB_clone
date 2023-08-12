#!/usr/bin/python3
""" Console Module """
import cmd
"""by mr-you"""
import sys
import json
import os

from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.state import State
from models.city import City

from models.base_model import BaseModel
from models.user import User
# from models import storage

class HBNBCommand(cmd.Cmd):
    """Define HBNB console"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quits the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def emptyline(self):
        """an empty line + ENTER shouldnot execute anything"""
        pass
    

    """ add by mr you """
    def create(self, arg):
        """  Creates a new instance of BaseModel """
        if len(arg) ==  0:
            print("** class name missing **")
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
