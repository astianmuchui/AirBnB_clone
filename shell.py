#!/usr/bin/python3

import cmd, sys, readline

class Interpreter(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "(hbnb) "
        self.intro  = "Welcome to the hbnb shell.   Type help or ? to list commands.\n"
    @classmethod
    def do_foo(self, arg):
        print("foo!")
    @classmethod
    def do_EOF(self, arg):
        print("^D")
        exit(0)
        return True

intp = Interpreter()
intp.cmdloop()