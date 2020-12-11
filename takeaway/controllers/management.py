from .app import FastApiApp, FlaskApp
import sys


class BaseComand:
    def __init__(self, app, folder_name, db_driver, db_name, testdb_name, git_repo):
        self.app = app
        self.folder_name = folder_name
        self.db_driver = db_driver
        self.db_name = db_name
        self.testdb_name = testdb_name
        self.git_repo = git_repo

    def start(self):
        if self.app == "fastapi":

            app = FastApiApp(self.app, self.folder_name, self.db_driver, self.db_name,self.git_repo)
            app.start()

        elif self.app == "flask":

            app = FlaskApp(self.app, self.folder_name, self.db_driver, self.db_name, self.testdb_name, self.git_repo)
            app.start()
