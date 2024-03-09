#!/usr/bin/python3

"""The entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command processor class"""

    # custom prompt
    prompt = '(hbnb) '
    __legal_objs = {'BaseModel': BaseModel}

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id"""
        command = line.split()
        to_create = command[0]
        if len(line) == 0:
            print('** class name missing **')
        elif to_create not in HBNBCommand.__legal_objs:
            print("** class doesn't exist **")
        else:
            obj = HBNBCommand.__legal_objs[to_create]()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on the
        class name and id"""
        command = line.split()
        if len(line) == 0:
            print('** class name missing **')
            return
        if len(line) == 1:
            print("** instance id missing **")
            return
        to_show = command[0]
        if to_show not in HBNBCommand.__legal_objs:
            print("** class doesn't exist **")
            return

        obj_id = command[1]
        key = '{}.{}'.format(to_show, obj_id)  # predefined key format
        if key in storage.all():
            print(storage.all()[key])
        else:
            print('** no instance found **')

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id, and updates
        the json file to reflect the deletion"""
        command = line.split()
        if len(line) == 0:
            print('** class name missing **')
            return
        if len(line) == 1:
            print("** instance id missing **")
            return
        to_destroy = command[0]
        if to_destroy not in HBNBCommand.__legal_objs:
            print("** class doesn't exist **")
            return

        obj_id = command[1]
        key = '{}.{}'.format(to_destroy, obj_id)  # predefined key format
        if key in storage.all():
            ...
        else:
            print('** no instance found **')

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exits the program with CTRL + D"""
        return True

    def emptyline(self):
        """Causes nothing to be executed if nothing is provided
        at the prompt"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
