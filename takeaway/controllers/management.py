from .app import  FastApiApp, FlaskApp, DjangoApp
import sys
class BaseComand:

    def __init__(self,app,folder_name):
        self.app = app
        self.folder_name = folder_name
        
    
    def start(self):
        if self.app == "fastapi":

            app = FastApiApp(self.app, self.folder_name)
            app.start()

        elif self.app == "flask":
            
            app = FlaskApp(self.app, self.folder_name)
            app.start()


        elif self.app == "django":
            print("")
            print("😭 Error: Django is not ready yet")
            sys.exit(1)
            
            app = DjangoApp(self.app, self.folder_name)
            app.start()
