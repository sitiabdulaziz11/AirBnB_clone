#!/usr/bin/python3

import json
import os

class FileStorage:
    """ FileStorage class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects
        """
        return self.__objects
    
    def new(self, obj):
        """" Sets in __objects the obj with key <obj class name>.id"""
        
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj
    
    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path)"""
        
        def save(self):
            """Serializes __objects to the JSON file (path: __file_path)"""
            with open(self.__file_path, 'w') as f:
                json_objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
                json.dump(json_objects, f) #  writes the json_objects
                # dictionary to the file f in JSON format
                # f: The file object where the JSON data will be written which is file.json.
        
    def reload(self):
        """"
        Deserializes the JSON file to __objects
        """
        try:  # Open the JSON file in read mode ('r')
            with open(self.__file_path, 'r') as f:  # Load the JSON content from the file
                json_objects = json.load(f)
                for key, obj_dict in json_objects.items():  # Extract the class name from the key
                    class_name = key.split('.')[0]  # Instantiate the object using the dictionary
                    self.__objects[key] = globals()[class_name](**obj_dict)
                    # self.__objects[key] = obj_dict
        except FileNotFoundError:
            pass # If the file is not found, do nothing (pass)
           
