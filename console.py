#!/usr/bin/python3
"""console.py that contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models import storage
import shlex
import json


class HBNBCommand(cmd.Cmd):
    """[HBNBCommand]
       The console contains the entry point of the command interpreter
    Args:
        cmd: [input from command line]
    """

    prompt = "(hbnb) "
    c = ("BaseModel", "User", "Place", "City", "Amenity", "Review", "State")

    def emptyline(self):
        """Emtyline function"""
        return

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """EOF exit the program"""
        return True

    def do_create(self, line):
        """
        Creates a new instance of
        (BaseModel, User, State, City, Amenity, Place or Review),
        saves it (to the JSON file) and prints the id

        Documented commands:
        =======================================================
        type (create <class_name>) or (<class_name>.create())

        Example:

        (hbnb) BaseModel.create()
        8153f2d6-d7ca-4bd9-ad61-e892d5c560f9
        (hbnb)
        """
        if line == "":
            print("** class name missing **")
        elif line in type(self).c:
            new_obj = globals()[line]()
            new_obj.save()
            print("{}".format(new_obj.id))
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        Prints the string representation of an
        instance based on the class name and id

        Documented commands:
        =======================================================
        type (show <class_name(id)>) or (<class_name>.show(id))

        Example:
        (hbnb) BaseModel.show("8153f2d6-d7ca-4bd9-ad61-e892d5c560f9")
        [BaseModel] (8153f2d6-d7ca-4bd9-ad61-e892d5c560f9) {...}
        (hbnb)
        """
        data = line.split(" ")
        if line == "":
            print("** class name missing **")
        elif data[0] in type(self).c:
            if len(data) < 2:
                print("** instance id missing **")
            elif storage.find(data[1], data[0]) is None:
                print("** no instance found **")
            else:
                print(storage.find(data[1], data[0]))

        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file). """
        data = line.split(" ")
        if line == "":
            print("** class name missing **")
        elif data[0] in type(self).c:
            if len(data) < 2:
                print("** instance id missing **")
            elif storage.find(data[1], data[0]) is None:
                print("** no instance found **")
            else:
                storage.delete(data[1])
                storage.save()
        else:
            print("** class doesn't exist **")

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name.

        Documented commands:
        =======================================================
        type (all) or (<class_name>.all())

        Example 1
        * Print all classes created *:

        (hbnb) all
        [BaseModel] (8153f2d6-d7ca-4bd9-ad61-e892d5c560f9) {...}
        [Place] (118f7a06-ab4f-4112-bfc4-8cdab1aefe96) {...}
        [User] (55baa4fe-3f29-4c06-90e8-9fd2539aff27) {...}
        (hbnb)

        Example 2
        * Print all classes created by the same type *:

        (hbnb) BaseModel.all()
        [BaseModel] (8153f2d6-d7ca-4bd9-ad61-e892d5c560f9) {...}
        (hbnb)
        """
        if line == "":
            storage.print_all()
        elif line in type(self).c:
            storage.print_all(line)
        else:
            print("** class doesn't exist **")

    @staticmethod
    def isfloat(x):
        """check float"""
        try:
            float(x)
        except:
            return False
        else:
            return True

    @staticmethod
    def isint(x):
        """check int"""
        try:
            a = float(x)
            b = int(a)
        except:
            return False
        else:
            return a == b

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)."""
        data = shlex.split(line)
        if line == "":
            print("** class name missing **")
        elif data[0] not in type(self).c:
            print("** class doesn't exist **")
        elif len(data) < 2:
            print("** instance id missing **")
        elif storage.find(data[1], data[0]) is None:
            print("** no instance found **")
        elif len(data) < 3:
            print("** attribute name missing **")
        elif len(data) < 4:
            print("** value missing **")
        else:
            if type(self).isfloat(data[3]):
                num = data[3]
                if "." in data[3]:
                    try:
                        num = float(data[3])
                    except:
                        pass
                else:
                    try:
                        num = int(data[3])
                    except:
                        pass
                storage.find(data[1], data[0]).update(data[2], num)
            else:
                storage.find(data[1], data[0]).update(data[2], data[3])

    def do_count(self, class_name):
        """ retrieve the number of instances of a class """
        print(storage.count_list(class_name))

    def default(self, line):
        """ Default function """
        data = line.split(".")
        class_name = data[0]
        func_arg = data[1]
        aux = func_arg.replace(")", "")
        values = aux.split("(")
        name_func = values[0]
        args = values[1]

        if values[len(values) - 1] == "":
            del values[len(values) - 1]

        try:
            if class_name in type(self).c:
                """ get name of the function"""
                func = getattr(type(self), "do_" + str(name_func))
                f_line = str(class_name)
                if len(values) > 1:
                    try:
                        list_args = args.split(",", 1)
                        """ check if update + dictionary """
                        dict_args = list_args[1].replace("'", "\"")
                        dict_args = json.loads(dict_args)
                        f_line += " " + str(list_args[0])
                        for key, value in dict_args.items():
                            f_line_aux = f_line
                            f_line_aux += " " + str(key) + " " + str(value)
                            func(self, f_line_aux)
                        return
                    except:
                        pass
                    list_args = args.split(",")
                    if len(list_args) != 0:
                        list_args[0] = list_args[0].replace('"', '')
                    for i in range(0, len(list_args)):
                        f_line += " " + str(list_args[i])
                func(self, f_line)
        except:
            pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
