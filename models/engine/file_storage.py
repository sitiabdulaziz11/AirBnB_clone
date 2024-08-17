#!/usr/bin/python3

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ FileStorage class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self) -> dict:
        """ Returns the dictionary __objects
        """
        return self.__objects
    
    def new(self, obj):
        """" Sets in __objects the obj with key <obj class name>.id"""
        
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj
    
    def save(self) -> None:
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as f:
            json_objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(json_objects, f) #  writes the json_objects
            # dictionary to the file f in JSON format
            # f: The file object where the JSON data will be written which is file.json.
           
        
    def reload(self) -> None:
        """" Deserializes the JSON file to __objects
        """
        try:  
            with open(self.__file_path, 'r') as f:  # Open the JSON file in read mode ('r')
                if os.path.getsize(self.__file_path) == 0:
                        print("The JSON file is empty.")
                        return
                    
                if os.path.getsize(self.__file_path) != 0:
                    json_objects = json.load(f) # Load the JSON content from the file
                    for key, obj_dict in json_objects.items(): # Extract the class name from the key
                        class_name = key.split('.')[0]  
                        self.__objects[key] = globals() [class_name](**obj_dict) # Instantiate the object using the dictionary
        except (FileNotFoundError, json.JSONDecodeError):
            pass  # If the file is not found

