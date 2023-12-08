""" Cmd hbnbClass """
import cmd
from shlex import split
from models import storage
from models.base_model import BaseModel



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

    def do_show(self, args):
        """Prints the string representation of an instance based on the class name and id"""
        pass
     
     
if __name__ == '__main__':
    HBNBCommand().cmdloop()