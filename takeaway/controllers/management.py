from .app import FastApiApp, FlaskApp
import sys


class BaseComand:
    def __init__(self, app, folder_name, db_driver, db_name):
        self.app = app
        self.folder_name = folder_name
        self.db_driver = db_driver
        self.db_name = db_name

    def start(self):
        if self.app == "fastapi":

            app = FastApiApp(self.app, self.folder_name, self.db_driver, self.db_name)
            app.start()

        elif self.app == "flask":

            app = FlaskApp(self.app, self.folder_name, self.db_driver, self.db_name)
            app.start()
