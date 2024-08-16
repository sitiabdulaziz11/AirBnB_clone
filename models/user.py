from .base_model import BaseModel

class User(BaseModel):
    """User class that inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    
    def __init__(self, *args, **kwargs):
        """Initialize a new user
        """
        
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        