#!/usr/bin/python3

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
    
classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Amenity": Amenity,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State
        # Add other class mappings here
    }

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
        
        args = user_input.split()
        if not args:
            print("** class name missing **")
            return
        
        class_name = args[0]
        
        if class_name not in classes:
            print("** class doesn't exist **")
            return
    
        new_instance = classes[class_name]()
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
        elif args[0] not in globals():
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
        
        if len(args) == 0:
            print('** class name missing **')
            return
        
        class_name = args[0]
        # class_names_in_storage = {key.split('.')[0]for key in storage.all().keys()} used to check classes in storage
        # if class_name not in classes: # to check classes in the actual class definitions
        if args[0] not in globals():
                print("** class doesn't exist **")
                return
            
        if len(args) == 1:
            print("** instance id missing **")
        else:
            isinstance_id = args[1]
            
            key = f"{class_name}.{isinstance_id}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()
    
    def do_State(self, user_input):
        """Prints the string representation of an instance based on the class"""
        
        args = user_input.split( )
        if args:
        # elif user_input or args[0] != "BaseModel":
            if args[0] == "State":
                instances = [str(obj) for obj in storage.all().values()]
                print(instances)
    
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
            class_names_in_storage = {key.split('.')[0] for key in storage.all().keys()}

            if class_name not in class_names_in_storage:
            # if class_name not in globals(): this 3 work
            # if user_input != "BaseModel":
             print("** class doesn't exist **")
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
            return
        
        if args[0] not in globals():
            print("** class doesn't exist **")
            return
        
        elif len(args) == 1:
            print("** instance id missing **")
            return
        
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        
        elif len(args) == 3:
            print("** value missing **")
            return
      
        class_name = args[0]
        isinstance_id = args[1]
        
        instance_id = args[1]
        key = f"{class_name}.{isinstance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
            
        attribute_name = args[2]
        attribute_value = ' '.join(args[3:]).strip('"')
        instance = storage.all()[key]
        
        # print(f"Updating {attribute_name} of instance {instance_id} with value: {attribute_value}")  # Debug print
        
        # Handle type casting
        if attribute_value.isdigit():
            attribute_value = int(attribute_value)
        else:
            try:
                attribute_value = float(attribute_value)
            except ValueError:
                pass
        setattr(instance, attribute_name, attribute_value)
        storage.save()
        # print(f"Instance {instance_id} updated successfully.")  # Success print
    
    def default(self, user_input: str) -> None:
        """Handle unrecognized or default behavior for unknown commands
        """

        if user_input.endswith(".all()"):
            class_name = user_input.split(".")[0]
            self.do_all(class_name)
        
        # elif len(args) == 2 and args[1] == "count()":
        elif user_input.endswith(".count()"):
            class_name = user_input.split(".")[0]
            count = 0
            for obj in storage.all().values():
                # if type(obj).__name__ == class_name:
                if obj.__class__.__name__ == class_name:
                    count += 1
            print(count)
        
        if ".show(" in user_input and user_input.endswith(")"):
            try:
                # Split input to get class name and command with ID
                class_name, rest = user_input.split(".", 1)
                command = rest.strip(")")
                if command.startswith("show("):
                    # Extract ID from the command
                    instance_id = command[5:].strip('"')
                    # Pass class name and ID to do_show
                    self.do_show(f"{class_name} {instance_id}")
            except ValueError:
                print("** Invalid command **")
            
        

if __name__ == "__main__":
    HBNBCommand().cmdloop() # "Welcome to the HBNB command interpreter. Type help or ? to list commands.\n"
