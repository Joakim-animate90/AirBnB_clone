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
    def do_destroy(self, line):
        """Deletes an instance.
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
                    del storage.all()[key]
                    storage.save()
    def do_all(self, line):
        """Prints all string representation of all instances.
        """
        if line != "":
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                l = [str(obj) for key, obj in storage.all().items()
                     if type(obj).__name__ == words[0]]
                print(l)
        else:
            l = [str(obj) for key, obj in storage.all().items()]
            print(l)


    def do_update(self, line):

        """Updates an instance by adding or updating an attribute.
        """
        if line == "" or line is None:
            print("** class name missing **")
            return
            
            rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
            match = re.search(rex, line)
            classname = match.group(1)
            uid = match.group(2)
            attribute = match.group(3)
            value = match.group(4)
            if not match:
                print("** class name missing **")
            elif classname not in storage.classes():
                print("** class doesn't exist **")
            elif uid is None:
                print("** instance id missing **")
            else:
                key ="{}.{}".format(classname, uid)
                if key not in storage.all():
                    print("** no instance found **")
                elif not attribute:
                    print("** attribute name missing **")
                elif not value:
                    print("** value missing **")
                else:
                    cast = None
                    if not re.search('^".*"$', value):
                        if '.' in value:
                            cast = float
                        else:
                            cast = int
                    else:
                        value = value.replace('"','')
                    attributes = storage.all()[classname]
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    elif cast:
                        try:
                            value = cast(value)
                        except ValueError:
                            pass  # fine, stay a string then
                    setattr(storage.all()[key], attribute, value)
                    storage.all()[key].save()






if __name__ == '__main__':
    HBNBCommand().cmdloop()   
