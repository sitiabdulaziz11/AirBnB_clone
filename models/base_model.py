import uuid
from datetime import datetime
from models import storage # Import the storage instance


class BaseModel:
    """My base class for all models
    """
    
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance with id, created_at, updated_at
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            # Assign values from kwargs
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "created_at":   
                    self.created_at = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "__class__":
                    continue
                else:
                    setattr(self, key, value)
    
    def save(self):
        self.updated_at = datetime.now()
        storage.save()
    
    def to_dict(self):
        """Create a dictionary from instance __dict__
        """
        dict_repr = self.__dict__.copy()
        # Add the class name
        dict_repr['__class__'] = self.__class__.__name__
        # Convert datetime attributes to ISO format
        dict_repr['created_at'] = self.created_at.isoformat()
        dict_repr['updated_at'] = self.updated_at.isoformat()
        return dict_repr
    
    def __str__(self):
        # Return the string representation of the instance
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)