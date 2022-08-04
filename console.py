#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
class HBNBCommand(cmd.Cmd):
    

    """Class for the command interpreter."""

    prompt = "(hbnb) "
    
    def do_quit(self,line):
        """
        Exits the program.
        """
        return True
    
    def do_EOF(self,line):
        """Handles End Of File character.
        """
        print()
        return True    
   
    def emptyline(self):
        """Doesn't do anything on ENTER.
        """
        pass
    def do_create(self, line):

        """Creates an Instance.
        """
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            b = storage.classes()[line]()
            b.save()
            print(b.id)
    def do_show(self, line):
        """Prints the string representation of an instance based on class name and id.
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
           words = line.split(' ')
           if words[0] not in storage.classes():
               print("** class doesn't exist **")
           elif len(words) < 2:
               print("** instance id missing **")
           else:
               key = "{}.{}".format(words[0], words[1])
               if key not in storage.all():
                   print("** no instance found **")
               else:
                   print(storage.all()[key])





if __name__ == '__main__':
    HBNBCommand().cmdloop()   
