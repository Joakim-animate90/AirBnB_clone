#!/usr/bin/python3
import cmd
class HBNBCommand(cmd.Cmd):
    

    """Class for the command interpreter."""

    prompt = "(hbnb) "
    
    def do_quit(self):
        """
        Exits the program.
        """
        return True
    
    def do_EOF(self):
        """Handles End Of File character.
        """
        print()
        return True    
   
    def emptyline(self):
        """Doesn't do anything on ENTER.
        """
        pass
if __name__ == '__main__':
    HBNBCommand().cmdloop()   
