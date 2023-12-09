""" Cmd hbnbClass """
import cmd
from shlex import split
from models import storage
from models.base_model import BaseModel
import json



class HBNBCommand(cmd.Cmd):
    """ cmd """
    prompt = "(hbnb) "
    all_classes = ["BaseModel"]

    def do_quit(self, arg):
        """" Quit hbnb """
        return True
    
    do_EOF = do_quit

    def do_help(self, arg):
        """" help hbnb """
        cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        pass

    def do_create(self, arg):
        """create new instance of BaseModels and create to JSON file"""
        args = split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.all_classes:
            print("** class doesn't exist **")
        else:
            new_inst = BaseModel()
            new_inst.save()
            print(new_inst.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        ars = split(arg)
        if len(ars) == 0:
            print("** class name missing **")
        elif ars[0] not in self.all_classes:
            print("** class doesn't exist **")
        elif not ars[1]:
            print("** instance id missing **")
        else:
            key = f"{ars[0]}.{ars[1]}"
            if key in storage.all():
                print(storage.all()[key])
            else:
                print('** no instance found **')
        
    def do_destroy(self, arg):
        ars = split(arg)
        if len(ars) == 0:
            print("** class name missing **")
        elif ars[0] not in self.all_classes:
            print("** class doesn't exist **")
        elif not ars[1]:
            print("** instance id missing **")
        else:
            key = f"{ars[0]}.{ars[1]}"
     
if __name__ == '__main__':
    HBNBCommand().cmdloop()