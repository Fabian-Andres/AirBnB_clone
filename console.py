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
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""
        if line == "":
            print("** class name missing **")
        elif line in type(self).c:
            new_obj = globals()[line]()
            new_obj.save()
            print("{}".format(new_obj.id))
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an
        instance based on the class name and id"""
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
        """Prints all string representation of all instances
        based or not on the class name."""
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

    def default(self, line):
        data = line.split(".")
        try:
            if data[0] in type(self).c:
                func = getattr(type(self), "do_" + str(data[1][:-2]))
                func(self, data[0])
        except:
            pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
