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

    def precmd(self, line):
        """Split the input into command and arguments
        and returns the modified arguments
        """
        if not sys.stdin.isatty():
            print()
        return line

    def default(self, line):
        """Handles commands with the form
        `<class_name>.<method> (<arg1>, arg2>, ...)`
        """
        command_parts = line.split(".")

        # Map method names to corresponding methods
        method_mapping = {
                "all()": self.do_all,
                "count()": self.do_count
            }

        # Check if the class (first arg) is valid
        if any(command_parts[0] == class_name for
               class_name in self.all_classes):
            # Get the method and required arguments to execute
            if command_parts[1] in method_mapping:
                method = method_mapping[command_parts[1]]
                method(f"{command_parts[0]} {command_parts[1]}")
            elif command_parts[1].startswith("show"):
                # Extract the ID from the show command
                id_show = command_parts[1].split('"')[1]
                self.do_show(f"{command_parts[0]} {id_show}")
            elif command_parts[1].startswith("destroy"):
                # Extract the ID from the destroy command
                id_destroy = command_parts[1].split('"')[1]
                self.do_destroy(f"{command_parts[0]} {id_destroy}")
            elif command_parts[1].startswith("update"):
                # Extract various parts of the update command
                args_update = command_parts[1].split('"')
                _class, _id, _attr, _value = (
                        command_parts[0],
                        args_update[1],
                        args_update[3],
                        args_update[5]
                    )
                self.do_update(f"{_class} {_id} {_attr} {_value}")

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
                    if (
                        obj.id == instance_id
                        and isinstance(obj, globals()[class_name])
                    ):
                        print(str(obj))
                        instance_found = True
                        break

                if not instance_found:
                    print("** no instance found **")

            else:
                print("** class doesn't exist **")

    def do_count(self, line):
        """Returns the number of instances of a class
        Usage: <class_name>.count()
        """
        numb_instances = len([value for key, value in storage.all().items()
                              if key.startswith(line[0])])
        print(numb_instances)

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

    def do_all(self, line):
        """Prints all string representation of all
        instances based or not on the class name.
        """
        args = line.split()
        list = []

        if not args:
            all_objs = storage.all().values()
        else:
            class_name = args[0]
            if class_name not in self.all_classes:
                print("** class doesn't exist **")
                return
            all_objs = [obj for obj in storage.all().values()
                        if obj.__class__.__name__ == class_name]

        objs_formatted = [f"[{str(obj)} {obj.to_dict()}]"
                          for obj in all_objs]

        for obj in objs_formatted:
            print(obj)

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
