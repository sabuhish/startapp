test = """

import unittest
import warnings
from app_init.app_factory import create_app
from extensions.extensions import db


class TestUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app("test")
        cls.client = cls.app.test_client()
        cls.db = db

        warnings.filterwarnings("ignore", category=ResourceWarning)
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        cls.db.create_all()
    
    @classmethod
    def tearDownClass(cls):
        cls.db.session.remove()
        cls.db.drop_all()

"""