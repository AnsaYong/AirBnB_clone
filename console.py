#!/usr/bin/python3
"""
This module provides a python command line interpreter
"""
import cmd
import sys
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
    """Provides methods that ensure proper functioning of
    the interpreter
    """
    prompt = "(hbnb) "
    all_classes = [
            "BaseModel",
            "User",
            "State",
            "City",
            "Amenity",
            "Place",
            "Review"
            ]

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """(Ctrl + D) to force the program to exit
        """
        return True

    def do_create(self, arg):
        """Creates a new instance of the specified class;
        Ex: $ create BaseModel
        """
        if not arg:
            print("** class name missing **")
            return

        if arg in HBNBCommand.all_classes and isinstance(globals()[arg], type):
            my_instance = globals()[arg]()  # Equivalent to my_instance = arg()
            my_instance.save()
            print(my_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id.
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]

            if (
                class_name in globals()
                and isinstance(globals()[class_name], type)
            ):
                all_objs = storage.all()
                instance_found = False
                for obj_id, obj in all_objs.items():
                    if obj.id == instance_id:
                        print(str(obj))
                        instance_found = True
                        break

                if not instance_found:
                    print("** no instance found **")

            else:
                print("** class doesn't exist **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (and saves the changes). Ex: $ destroy BaseModel 1234-1234-1234
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        all_objs = storage.all()

        key = f"{class_name}.{obj_id}"
        if key in all_objs:
            del all_objs[key]   # Delete the instance from storage
            storage.save()      # Save the changes to the storage
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name.
        """
        list = []
        if not arg or arg in globals() and isinstance(globals()[arg], type):
            all_objs = storage.all()
            for obj_id, obj in all_objs.items():
                list.append(str(obj))
            print(list)
        else:
            print("** class doesn't exist **")
            return

    def do_update(self, arg):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if (class_name in globals() and
                    isinstance(globals()[class_name], type)):
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    instance_id = args[1]
                    all_objs = storage.all()
                    instance_found = False
                    for obj_id, obj in all_objs.items():
                        if obj.id == instance_id:
                            if len(args) < 3:
                                print("** attribute name missing **")
                            else:
                                if len(args) < 4:
                                    print("** value missing **")
                                else:
                                    attr_name = args[2]
                                    attr_value = args[3]
                                    if (attr_name not in
                                            ('id',
                                             'created_at',
                                             'updated_at')):
                                        if (isinstance(attr_value,
                                                       (str, int, float))):
                                            setattr(obj, attr_name, attr_value)
                                            obj.save()

                            instance_found = True
                            break
                    if not instance_found:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def emptyline(self):
        """
        Prevents the previous command from being executed again if
        no command is given.
        """
        pass

    def precmd(self, line):
        """
        Add an empty line before executing command in non-interactive
        mode (only) so that the output mimics that of the interactive
        mode
        """
        if not sys.stdin.isatty():
            print()
        return line


if __name__ == '__main__':
    HBNBCommand().cmdloop()
