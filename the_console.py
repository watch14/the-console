import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        return True
    
    do_EOF = do_quit

    def do_help(self, arg):
        cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        pass
     
HBNBCommand().cmdloop()

if __name__ == '__main__':
    HBNBCommand().cmdloop()