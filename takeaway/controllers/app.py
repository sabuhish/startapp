# from .management import  BaseComand
import  os

from takeaway.settings.fastapi import  docker
from takeaway.settings.flask import  docker
from takeaway.settings.django import  docker


class FastApiApp():
    def __init__(self,app,folder_name):
        self.app = app
        self.folder_name = folder_name
        
    
    def start(self):
        pass


    def folder_create(self):
        os.makedirs(self.folder_name)


    def create_app_structure(self):
        '''This will initilaze the boilerplate of the project'''
        pass 


    def activate_pipenv(self):
        '''This will activate pipenv'''

        pass

    def install_dependencies(self):
    
        '''This will install all dependencies the app require'''
        pass


    




class FlaskApp:
    
    def __init__(self,app,folder_name):
        self.app = app
        self.folder_name = folder_name
        
    
    def start(self):
        print(self.app)
        print(self.folder_name)


    def folder_create(self):
        os.makedirs(self.folder_name)






class DjangoApp:
    def __init__(self,app,folder_name):
        self.app = app
        self.folder_name = folder_name
        
    
    def start(self):
        print(self.app)
        print(self.folder_name)