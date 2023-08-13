#!/usr/bin/python3
""" Console Module """
import cmd
import sys
import json
import os
import re
from shlex import split
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.state import State
from models.city import City
from models.base_model import BaseModel
from models.user import User
from models import storage

def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    print(curly_braces)
    brackets = re.search(r"\[(.*?)\]", arg)
    print(brackets)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            print(lexer)
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        print(lexer)
        retl = [i.strip(",") for i in lexer]
        print(retl)
        retl.append(curly_braces.group())
        print(retl)
        return retl

class HBNBCommand(cmd.Cmd):
    """Define HBNB console"""

    prompt = "(hbnb) "
    classes = {'BaseModel': BaseModel, 'User': User, 'City': City,
               'Place': Place, 'Amenity': Amenity, 'Review': Review,
               'State': State}

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

    def create(self, arg):
        """  Creates a new instance of BaseModel """
        if len(arg) == 0:
            print("** class name missing **")
            return

    def do_create(self, arg):
        """
        Usage: create <class>
        Create a new class instance and print its id 
        and 
        """
        if len(arg) == 0:
            print("** class name missing **")
            return
        new_li = None
        if arg:
            arg_li = arg.split()
            if len(arg_li) == 1:
                if arg in self.classes.keys():
                    new_li = self.classes[arg]()
                    new_li.save()
                    print(new_li.id)
                else:
                    print("** class doesn't exist **")
    def do_show(self,arg):
        """Prints the string representation of an instance based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif arg.split(" ")[0] == "":
            print("** class name missing **")
            return
        elif arg.split(" ")[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(arg.split()) > 1 and arg.split(" ")[1] != "":
            key = arg.split(" ")[0] + '.' + arg.split(" ")[1]
            if key in storage.all():
                all_ = storage.all()
                print(all_[key])
            else:
                print("** no instance found **")
        else:
            print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()



