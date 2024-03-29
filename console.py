#!/usr/bin/python3

"""The entry point of the command interpreter"""

import os
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command processor class"""

    # custom prompt
    prompt = '(hbnb) '
    __legal_objs = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review,
    }

    def precmd(self, line):
        """Routines that pre-process the line, before it is passed on to the
        normal processing
        """
        if '.' not in line:
            return line

        parts = line.split('.')
        if len(parts) == 2:  # the format is Class.action
            class_type, action = parts
            if action == 'all()':
                return 'all {}'.format(class_type)
            if action == 'count()':
                self.count_instances(class_type)
                return ''
            if action.startswith('show('):
                obj_id = action[6:-2]
                return 'show {} {}'.format(class_type, obj_id)
            if action.startswith('destroy('):
                obj_id = action[9:-2]
                return 'destroy {} {}'.format(class_type, obj_id)
        return line

    def do_create(self, line):
        """Creates a new instance of an object, saves it (to the JSON file)
        and prints the id"""
        command = shlex.split(line)

        if len(line) == 0:
            print('** class name missing **')
            return
        to_create = command[0]
        if to_create not in HBNBCommand.__legal_objs:
            print("** class doesn't exist **")
            return

        obj = HBNBCommand.__legal_objs[to_create]()
        obj.save()
        print(obj.id)

    def count_instances(self, line):
        """Counts the number of instances of this class that exist in the
        storage engine
        """
        count = 0
        for k, v in storage.all().items():
            this_class = k.split('.')[0]
            if this_class == line:
                count += 1
        print(count)

    def do_show(self, line):
        """Prints the string representation of an instance based on the
        class name and id"""
        command = shlex.split(line)
        if len(line) == 0:
            print('** class name missing **')
            return

        to_show = command[0]
        if to_show not in HBNBCommand.__legal_objs:
            print("** class doesn't exist **")
            return

        if len(command) == 1:
            print("** instance id missing **")
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
        command = shlex.split(line)
        if len(line) == 0:
            print('** class name missing **')
            return

        to_destroy = command[0]
        if to_destroy not in HBNBCommand.__legal_objs:
            print("** class doesn't exist **")
            return

        if len(command) == 1:
            print("** instance id missing **")
            return

        obj_id = command[1]
        key = '{}.{}'.format(to_destroy, obj_id)  # predefined key format
        if key in storage.all():
            del storage.all()[key]
            storage.save()
            return

        print('** no instance found **')

    def do_all(self, line):
        """Prints all string representation of all instances based or not on
        the class name
        """
        if len(line) == 0:
            # print all the objects of all kinds
            all_instances = [
                obj.__str__() for key, obj in storage.all().items()
            ]
            print(all_instances)
            return

        to_print = shlex.split(line)[0]
        if to_print not in HBNBCommand.__legal_objs:
            print("** class doesn't exist **")
            return

        # only print this specific type of object
        specific_instances = [
            obj.__str__()
            for key, obj in storage.all().items()
            if key.split('.')[0] == to_print
        ]
        print(specific_instances)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or
        updating attribute. Saves the changes to the JSON file.
        """
        command = shlex.split(line)
        if len(line) == 0:
            print('** class name missing **')
            return

        to_update = command[0]
        if to_update not in HBNBCommand.__legal_objs:
            print("** class doesn't exist **")
            return

        if len(command) == 1:
            print('** instance id missing **')
            return

        obj_id = command[1]
        # check that the id exists
        obj_key = '{}.{}'.format(to_update, obj_id)
        if obj_key not in storage.all().keys():
            print('** no instance found **')
            return

        if len(command) == 2:
            print('** attribute name missing **')
            return

        obj_attr = command[2]
        if len(command) == 3:
            print('** value missing **')
            return

        new_value = command[3]
        new_value = self.get_real_datatype(new_value)

        # update the attribute and update the json file
        obj = storage.all()[obj_key]
        obj.__dict__[obj_attr] = new_value
        storage.all().update({obj_key: obj})
        storage.save()

    def get_real_datatype(self, value):
        """Returns the value, after it has been transformed into its
        most natural datatype. If no transformation was made, then the value
        is returned in its original string form
        """
        real_type = value
        try:
            real_type = int(value)
        except ValueError:
            try:
                real_type = float(value)
            except ValueError:
                pass
        return real_type

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

    def postloop(self):
        """Routines to perform after every loop in the program"""
        # print a newline after execution of the command, if the console
        # program was called in non-interactive mode
        if not os.isatty(0):
            print()
        else:
            pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
