#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
import shlex


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "
    c = ("BaseModel",)

    def do_quit(self, *args):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        return True

    def do_create(self, line):
        if line == "":
            print("** class name missing **")
        elif line in type(self).c:
            new_obj = globals()[line]()
            new_obj.save()
            print("{}".format(new_obj.id))
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        data = line.split(" ")
        if len(data) == 0:
            print("** class name missing **")
        elif data[0] in type(self).c:
            if len(data) < 2:
                print("** instance id missing **")
            elif storage.find(data[1]) == None:
                print("** no instance found **")
            else:
                print(storage.find(data[1]))

        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        data = line.split(" ")
        if len(data) == 0:
            print("** class name missing **")
        elif data[0] in type(self).c:
            if len(data) < 2:
                print("** instance id missing **")
            elif storage.find(data[1]) == None:
                print("** no instance found **")
            else:
                storage.delete(data[1])
                storage.save()
        else:
            print("** class doesn't exist **")

    def do_all(self, line):
        if line == "":
            storage.print_all()
        elif line in type(self).c:
            storage.print_all(line)
        else:
            print("** class doesn't exist **")

    @staticmethod
    def isfloat(x):
        try:
            float(x)
        except:
            return False
        else:
            return True

    @staticmethod
    def isint(x):
        try:
            a = float(x)
            b = int(a)
        except:
            return False
        else:
            return a == b

    def do_update(self, line):
        data = shlex.split(line)
        if len(data) == 0:
            print("** class name missing **")
        elif data[0] not in type(self).c:
            print("** class doesn't exist **")
        elif len(data) < 2:
            print("** instance id missing **")
        elif storage.find(data[1]) == None:
            print("** no instance found **")
        elif len(data) < 3:
            print("** attribute name missing **")
        elif len(data) < 4:
            print("** value missing **")
        else:
            if type(self).isfloat(data[3]):
                num = float(data[3])
                if self.isint(data[3]):
                    num = int(data[3])
                storage.find(data[1]).update(data[2], num)
            else:
                storage.find(data[1]).update(data[2], data[3])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
