 # def reload(self) -> None:
    #     """" Deserializes the JSON file to __objects
    #     """
    #     try:
    #         with open(self.__file_path, 'r') as f:
    #             if os.path.getsize(self.__file_path) == 0:
    #                 print("The JSON file is empty.")
    #                 return
                
    #             json_objects = json.load(f)
    #             for key, obj_dict in json_objects.items():  # Extract the class name from the key
    #                 class_name = key.split('.')[0]
                    
    #                 from models.base_model import BaseModel
    #                 from models.user import User
    #                 # from models.amenity import Amenity
                    
    #                 class_mapping = {
    #                     "BaseModel": BaseModel,
    #                     "User": User,
    #                     # "Amenity": Amenity
    #                     # Add other models here
    #                 }
    #                 if class_name in class_mapping:
    #                     self.__objects[key] = class_mapping[class_name](**obj_dict)
    #                 else:
    #                     print(f"Class {class_name} not found.")
    #     except (FileNotFoundError, json.JSONDecodeError):
    #         pass # If the file is not found, do nothing (pass)
    # when i imported from models import storage in base_model, it caused crcular import error and this was fix it, but when i imported import models, it gone.