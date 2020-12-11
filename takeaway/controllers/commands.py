import os
import sys
import string
from .management import BaseComand


class Operation:
    def __init__(self, app, folder_name, db_driver, db_name, testdb_name,git_repo):
        self.app = app
        self.folder_name = folder_name
        self.program = "takeaway"
        self.db_driver = db_driver
        self.db_name = db_name
        self.testdb_name = testdb_name
        self.git_repo = git_repo
        self.issue_url = "https://github.com/marlin-dev/startapp"
        self.PR = "https://github.com/marlin-dev/startapp/pulls"

    def check_file(self):
        try:
            self.directory = True if os.path.isdir(self.folder_name) else False
            if os.path.isdir(self.folder_name) or os.path.isfile(self.folder_name):
                sys.stdout.write(self.file_exist())
                sys.exit(1)
            else:
                pass

        except FileExistsError as err:
            print(err)

    def file_exist(self):
        """This will be executed if there is file or folder with named application name"""
        usage = [
            "",
            "😭 Error:  '%s' %s already exist "
            % (self.folder_name, "folder" if self.directory else "file"),
            "",
            "Run '%s --help' for usage." % self.program,
            "",
            "🥳  if you think something is wrong please feel free to open issues 👉'%s'👈 "
            % self.issue_url,
            "",
        ]
        return "\n".join(usage)

    def thanks_using(self):
        """Thanks response at the end"""
        text = [
            "",
            "%s  CLI tool" % self.program,
            "",
            "Thanks for using! 👋😋😎 feel free to contribute 🙏 👉 '%s' 👈 " % self.PR,
            "",
        ]

        sys.stdout.write("\n".join(text))

    def execute(self):
        """Main execution function"""
        self.check_file()

        comand = BaseComand(self.app, self.folder_name, self.db_driver, self.db_name, self.testdb_name, self.git_repo)
        comand.start()
        self.thanks_using()
