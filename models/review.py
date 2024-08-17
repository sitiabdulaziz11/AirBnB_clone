from .base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
    
    def __init__(self, *args, **kwards):
        """Initialize Place
        """
        super().__init__(*args, **kwards)