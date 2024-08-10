from .engine.file_storage import FileStorage


# Create an instance of FileStorage
storage = FileStorage()  

storage.reload() # Call reload() method to load existing objects from the JSON file