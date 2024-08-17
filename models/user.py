from .base_model import BaseModel

class User(BaseModel):
    """User class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    
    def __init__(self, *args, **kwargs):
        """Initialize a new user
        """
        
        super().__init__(self, *args, **kwargs)
         