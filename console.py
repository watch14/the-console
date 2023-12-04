""" Cmd hbnbClass """
import cmd

class HBNBCommand(cmd.Cmd):
    """ cmd """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """" Quit hbnb """
        return True
    
    do_EOF = do_quit

    def do_help(self, arg):
        """" help hbnb """
        cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        pass
     
     
if __name__ == '__main__':
    HBNBCommand().cmdloop()