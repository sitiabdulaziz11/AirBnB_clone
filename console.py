#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage
    

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
    
    def do_create(self, user_input):
        """Creates a new instance of BaseModel, saves it, and prints the id.
        """
        class_name = user_input.split()
        
        if not user_input:
            print("** class name missing **")
        elif user_input != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
            
    def do_show(self, user_input):
        """Prints the string representation of an instance based on the class
        name and id
        """
        args = user_input.split()
        
        if not user_input or len(args) == 0:
            print('** class name missing **')
        # elif user_input or args[0] != "BaseModel":
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            class_name = args[0]
            isinstance_id = args[1]
            
            key = f"{class_name}.{isinstance_id}"
            if key in storage.all():
                print(storage.all()[key])    
            else:
                print("** no instance found **")
    
    def do_destroy(self, user_input):
        """Deletes an instance based on the class name and id
        """
        args = user_input.split()
        
        if not user_input:
            print('** class name missing **')
        elif user_input != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            class_name = args[0]
            isinstance_id = args[1]
            
            key = f"{class_name}.{isinstance_id}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()
    
    def do_all(self, user_input):
        """Prints all string representation of all instances based or not only
        on the class name
        """
        args = user_input.split()
        
        if len(args) == 0:
            # No class name provided, print all instances
            instances = [str(obj) for obj in storage.all().values()]
            print(instances)
        else:
            class_name = args[0]
            # if args[0] not in storage.all():
            #     print("** class doesn't exist **")
            if class_name not in globals():
                print("** class doesn't exist **")
                return
            else:
                # Print all instances of the specified class
                instances = [str(obj) for obj in storage.all().values() if type(obj).__name__ == class_name]
                print(instances)
                
                # instances = [str(obj) for key, obj in storage.all().items() if key.startswith(class_name + ".")]
                # print(instances)
                
    def do_update(self, user_input):
        """ Updates an instance based on the class name and id
        """
        args = user_input.split()
        
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in storage.all():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
      
        class_name = args[0]
        isinstance_id = args[1]
        
        key = f"{class_name}.{isinstance_id}"
        if key not in storage.all():
            print("** no instance found **")
            
        attribute_value = ' '.join(args[3:]).strip('"')
        isinstance = storage.all()[key]
        
        # Handle type casting
        if isinstance(attribute_value, str):
            if attribute_value.isdigit():
                attribute_value = int(attribute_value)
            else:
                attribute_value = float(attribute_value)

        setattr(isinstance, args[2], attribute_value)
        storage.save()
        
                
    
if __name__ == "__main__":
    HBNBCommand().cmdloop(
        # "Welcome to the HBNB command interpreter. Type help or ? to list commands.\n"
    )