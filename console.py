#!/usr/bin/python3

import cmd
from .models.base_model import BaseModel

create = BaseModel()
create.save()

class HBNBCommand(cmd.Cmd):
    """HBNB command interpreter"""
    
    prompt = "(hbnb) "
    
    def do_EOF(self, line):
        """Quit command to exit the program.
        """
        
        return True
    
    def do_quit(self, line):
        """Quit command to exit the program.
        """
        
        return True
    
    def emptyline(self) -> bool:
        pass
    
if __name__ == "__main__":
    HBNBCommand().cmdloop(
        # "Welcome to the HBNB command interpreter. Type help or ? to list commands.\n"
    )