from .base_model import BaseModel

class State(BaseModel):
    """State class"""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        name = ""