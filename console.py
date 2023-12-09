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
        """delete"""
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
                del storage.all()[key]
                storage.save()
            else:
                print('** no instance found **')

    def do_all(self, arg):
        """ Prints all instances based or not on the class name. """
        ars = split(arg)
        if  len(ars) == 0:
            for inst in storage.all().values():
                print(str(inst))
        elif ars[0] not in self.all_classes:
            print("** class doesn't exist **")
        else:
            print([str(v) for k, v in storage.all().items() if ars[0] in k])

    def do_update(self, arg):
        """update by adding attributes"""
        ars = split(arg)
        if len(ars) == 0:
            print("** class name missing **")
        elif ars[0] not in self.all_classes:
            print("** class doesn't exist **")
        elif len(ars) < 2:
            print("** instance id missing **")
        elif len(ars) < 3:
            print("** attribute name missing **")
        elif len(ars) < 4:
            print("** value missing **")
        else:
            cls = ars[0]
            id = ars[1]
            new_key = ars[2]
            new_val = ars[3]
            storage.reload()
            key = f"{cls}.{id}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                instance = storage.all()[key]
                new_key = ars[2]
                new_val = ars[3]
                try:
                    new_val = eval(new_val)
                except Exception:
                    pass
                setattr(instance, new_key, new_val)
                instance.save()
                
                



if __name__ == '__main__':
    HBNBCommand().cmdloop()