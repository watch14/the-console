import cmd

class Console(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self):
        return True

Console().cmdloop()