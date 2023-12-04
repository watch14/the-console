import cmd

class Console(cmd.Cmd):
    prompt = "(hbnb) "

    def do_exit(self):
        return True

Console().cmdloop()