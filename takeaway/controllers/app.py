# from .management import  BaseComand
import  os
from takeaway.settings.fastapi.docker import  Dockerfile
from takeaway.settings.fastapi.requirements import  requirements


from takeaway.settings.flask import  docker
from takeaway.settings.django import  docker


class FastApiApp():
    def __init__(self,app,folder_name):

        self.app = app
        self.folder_name = folder_name
        self.root_directory = f'{self.folder_name}/'
        
        self.core = f'{self.root_directory}core'
        self.settings = f'{self.core}/settings'

        self.app_folder = f'{self.root_directory}app'
        self.controllers = f'{self.app_folder}/controllers'
        self.controller = f'{self.controllers}/controller'

        self.data = f'{self.app_folder}/data'
        self.utils = f'{self.app_folder}/utils'


    def start(self):
        self.create_app_structure()

    def file_create(self,directory,filename,content):
        with open(f"{directory}/{filename}","w") as file:
            file.write(content.strip())


    def root_folder_create(self):
        os.makedirs(self.folder_name)


    def create_app_structure(self):
        '''This will initilaze the boilerplate of the project'''

        self.root_folder_create()

        
        os.makedirs(self.core)
        os.makedirs(self.settings)
        os.makedirs(self.app_folder)
        os.makedirs(self.controllers)
        os.makedirs(self.controller)
        os.makedirs(self.data)
        os.makedirs(self.utils)


        self.create_init_file(self.core)
        self.create_init_file(self.settings)
        self.create_init_file(self.app_folder)
        self.create_init_file(self.controllers)
        self.create_init_file(self.data)
        self.create_init_file(self.utils)

        self.file_create(self.root_directory,"Dockerfile",Dockerfile)
    #    self.file_create()
    #    self.file_create()
    #    self.file_create()
    #    self.file_create()

    def create_init_file(self,directory):

        with open(f"{directory}/__init__.py", "a") as file:
            file.write("")


    

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
        
    # promt ele app name burda
    def start(self):
        print(self.app)
        print(self.folder_name)