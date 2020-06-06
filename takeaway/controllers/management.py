
# from .commands import  Operation

class BaseComand:

    def __init__(self,app,folder_name):
        self.app = app
        self.folder_name = folder_name

    
    def fastapi_execution(self):
        pass


    
    def flask_execution(self):
        pass

    
    def django_execution(self):
        pass


    def start(self):
        pass

