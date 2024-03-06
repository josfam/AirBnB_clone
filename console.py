#!/usr/bin/python3

"""The entry point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command processor class"""

    # custom prompt
    prompt = '(hbnb) '

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
